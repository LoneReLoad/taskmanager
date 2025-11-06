# Gestor de Tareas Inteligente

Este proyecto es una aplicación de consola en Python para gestionar tareas, con integración opcional de IA (OpenAI) para desglosar tareas complejas en subtareas simples.

## Características principales
- Añadir tareas manualmente
- Añadir tareas complejas y desglosarlas en subtareas usando IA (OpenAI)
- Listar tareas pendientes y completadas
- Marcar tareas como completadas
- Eliminar tareas
- Persistencia automática en `tasks.json`
- Pruebas unitarias con `pytest`

## Requisitos
- Python 3.8+
- (Opcional) API Key de OpenAI para usar la función de IA
- Recomendado: entorno virtual (`venv`)

## Instalación
1. Clona el repositorio:
   ```powershell
   git clone https://github.com/LoneReLoad/taskmanager.git
   cd taskmanager
   ```
2. Crea y activa un entorno virtual:
   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   ```
3. Instala las dependencias:
   ```powershell
   pip install -r requirements.txt
   ```
   Si no existe `requirements.txt`, instala manualmente:
   ```powershell
   pip install openai python-dotenv pytest
   ```
4. (Opcional) Configura la API Key de OpenAI:
   - Crea un archivo `.env` en la raíz con:
     ```
     OPENAI_API_KEY=tu_clave_openai
     OPENAI_MODEL=gpt-4o-mini
     ```

## Uso
Ejecuta la aplicación principal:
```powershell
python Main.py
```

### Ejemplos de uso

**Añadir tarea manual:**
```
Seleccione una opción (1-6): 1
Ingrese la descripción de la tarea: Comprar pan
Tarea anadida: Comprar pan
```

**Añadir tarea compleja (con IA):**
```
Seleccione una opción (1-6): 2
Ingrese la descripción de la tarea compleja: Organizar evento de cumpleaños
Tarea anadida: Reservar local
Tarea anadida: Comprar decoración
Tarea anadida: Enviar invitaciones
Tarea anadida: Preparar comida
```

**Listar tareas:**
```
Seleccione una opción (1-6): 3
[ ] #1: Comprar pan
[ ] #2: Reservar local
[ ] #3: Comprar decoración
[ ] #4: Enviar invitaciones
[ ] #5: Preparar comida
```

**Completar tarea:**
```
Seleccione una opción (1-6): 4
Ingrese el ID de la tarea a completar: 1
Tarea completada: Comprar pan
```

**Eliminar tarea:**
```
Seleccione una opción (1-6): 5
Ingrese el ID de la tarea a eliminar: 2
Tarea eliminada: Reservar local
Tarea eliminada: #2
```

**Salir:**
```
Seleccione una opción (1-6): 6
Saliendo del gestor de tareas. ¡Hasta luego!
```

---

## Roadmap de futuras tareas

- [ ] Exportar e importar tareas en formato CSV/JSON
- [ ] Interfaz gráfica (GUI) con Tkinter o PyQt
- [ ] Sincronización en la nube (Google Drive, Dropbox)
- [ ] Notificaciones por correo electrónico
- [ ] Integración con asistentes de voz
- [ ] Etiquetas y prioridades para tareas
- [ ] Filtrado y búsqueda avanzada de tareas
- [ ] Soporte multiusuario
- [ ] API REST para integración con otras apps
- [ ] Mejorar la integración con IA (más modelos, sugerencias contextuales)

## Pruebas
Ejecuta los tests unitarios con:
```powershell
pytest test_task_manager.py
```

Las pruebas usan un archivo temporal `test_tasks.json` para no afectar tus tareas reales.

## Estructura de archivos
- `Main.py`: interfaz principal y menú
- `task_manager.py`: lógica de gestión y persistencia de tareas
- `ai_service.py`: integración con OpenAI para desglosar tareas complejas
- `test_task_manager.py`: pruebas unitarias
- `tasks.json`: almacenamiento de tareas
- `.env`: credenciales de OpenAI (opcional)

## Notas
- Si no tienes API Key de OpenAI, la función de IA usará un fallback local para generar subtareas.
- El símbolo ✓ indica tareas completadas.
- El proyecto está listo para ampliarse con nuevas funcionalidades.

## Licencia
MIT
