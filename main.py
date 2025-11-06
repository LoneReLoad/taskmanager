from task_manager import TaskManager
from ai_service import create_simple_tasks


def print_menu():
    print("\n ---- Gestor de Tareas Inteligente ----\n")
    print("1. Añadir tarea ")
    print("2. Añadir tarea compleja (con IA)")
    print("3. Listar tareas ")
    print("4. Completar tarea ")
    print("5. Eliminar tarea ")
    print("6. Salir ")


def main():
    task_manager = TaskManager()
    while True:
        print_menu()

        try:
            choice = int(input("\nSeleccione una opción (1-6): "))

            match choice:
                case 1:
                    description = input("Ingrese la descripción de la tarea: ")
                    task_manager.add_task(description)
                case 2:
                    description = input("Ingrese la descripción de la tarea compleja: ")
                    subtasks = create_simple_tasks(description)
                    for subtask in subtasks:
                        if not subtask.startswith("Error:"):
                            task_manager.add_task(subtask)
                        else:
                            print(subtask)
                            break

                case 3:
                    task_manager.list_tasks()

                case 4:
                    task_id = int(input("Ingrese el ID de la tarea a completar: "))
                    task_manager.complete_task(task_id)

                case 5:
                    task_id = int(input("Ingrese el ID de la tarea a eliminar: "))
                    task_manager.delete_task(task_id)

                case 6:
                    print("Saliendo del gestor de tareas. ¡Hasta luego!")
                    break
                case _:
                    print("Opción no válida. Seleccione una opción del 1 al 6.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número de ID")


if __name__ == "__main__":
    main()
