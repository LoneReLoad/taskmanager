from task_manager import TaskManager


def print_menu():
    print("\n ---- Gestor de Tareas Inteligente ----\n")
    print("1. Añadir tarea ")
    print("2. Listar tareas ")
    print("3. Completar tarea ")
    print("4. Eliminar tarea ")
    print("5. Salir ")


def main():
    task_manager = TaskManager()

    print_menu()
    choice = input("\nSeleccione una opción (1-5): ")

    match choice:
        case "1":
            description = input("Ingrese la descripción de la tarea: ")
            task_manager.add_task(description)

        case "2":
            task_manager.list_tasks()

        case "3":
            task_id = int(input("Ingrese el ID de la tarea a completar: "))
            task_manager.complete_task(task_id)

        case "4":
            task_id = int(input("Ingrese el ID de la tarea a eliminar: "))
            task_manager.delete_task(task_id)

        case "5":
            print("Saliendo del gestor de tareas. ¡Hasta luego!")
            break
        case _:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")


if __name__ == "__main__":
    main()
