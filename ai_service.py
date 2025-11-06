import os
import re
import traceback
from dotenv import load_dotenv
import openai as openai_sdk
from openai import OpenAI

load_dotenv()

# Allow selecting a model via environment (falls back to a conservative default).
MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def create_simple_tasks(description):

    if not client.api_key:
        return ["Error: La API key de OpenAI no está configurada."]

    try:

        prompt = f"""Desglosa la siguiente tarea compleja en una lista de 3 a 5 subtareas simples y accionables.

Tarea: {description}

Formato de respuesta:
- Subtarea 1
- Subtarea 2
- Subtarea 3
- etc.

Responde solo con la lista de subtareas, una por línea, empezando cada línea con un guión."""

        # Use a minimal, standard set of parameters to avoid SDK/API errors.
        params = {
            "model": MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": "Eres un asistente experto en gestión de tareas que ayuda a dividir tareas complejas en pasos simples y accionables.",
                },
                {"role": "user", "content": prompt},
            ],
            # standard param name expected by most OpenAI-compatible SDKs
            "max_tokens": 300,
        }

        # Call the API and handle rate/quotas specifically.
        try:
            response = client.chat.completions.create(**params)
        except openai_sdk.RateLimitError as e:
            # Specific guidance when quota or rate limits are hit.
            print("Rate limit / cuota excedida al llamar a la API de OpenAI:", str(e))
            traceback.print_exc()
            # Provide a helpful error message and a local fallback so the app sigue funcionando.
            return [
                "Error: Se ha excedido la cuota de OpenAI (429). Revisa tu plan y detalles de facturación en https://platform.openai.com/account/billing."
            ] + _fallback_subtasks(description)
        except Exception as e:
            # Other unexpected errors
            print("Error al llamar a la API de OpenAI:", str(e))
            traceback.print_exc()
            return [
                f"Error: No se ha podido realizar la conexión a OpenAI. Detalle: {e}"
            ] + _fallback_subtasks(description)

        # Depending on SDK version/shape, the content path may vary slightly.
        # We try to read the common location used by the OpenAI Python SDK v1.
        content = ""
        try:
            content = response.choices[0].message.content.strip()
        except Exception:
            # fallback: try alternative attribute paths
            try:
                content = response.choices[0].text.strip()
            except Exception:
                content = str(response)

        subtasks = []

        for line in content.split("\n"):
            line = line.strip()
            if line and line.startswith("-"):
                subtask = line[1:].strip()
                if subtask:
                    subtasks.append(subtask)

        return (
            subtasks if subtasks else ["Error: No se han podido generar las subtareas."]
        )

    except Exception as e:
        # Catch-all safety net (should be rare because inner try handles API errors).
        print("Error inesperado en create_simple_tasks:", str(e))
        traceback.print_exc()
        return [f"Error inesperado: {e}"] + _fallback_subtasks(description)


def _fallback_subtasks(description: str):
    """Genera una lista de subtareas simple como fallback cuando la API no está disponible.

    Este método intenta dividir la descripción por comas/puntos/" y " para crear 2-4 pasos
    sin depender de la API externa, de forma que la aplicación siga usable offline.
    """
    # Intenta dividir en partes razonables
    parts = [p.strip() for p in re.split(r",| y |;|\.|-", description) if p.strip()]
    subtasks = []
    if len(parts) >= 2:
        for i, p in enumerate(parts[:5]):
            subtasks.append(f"(Fallback) Subtarea {i+1}: {p}")
    else:
        # Si no hay partes claras, crea 3 subtareas genéricas
        subtasks = [
            f"(Fallback) Analizar: {description}",
            f"(Fallback) Preparar recursos para: {description}",
            f"(Fallback) Ejecutar la primera acción de: {description}",
        ]

    return subtasks
