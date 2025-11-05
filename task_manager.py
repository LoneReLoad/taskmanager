import json


class Task:
    def __init__(self, id, description, completed=False):
        self.id = id
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "✓" if self.completed else " "
        return f"[{status}] #{self.id}: {self.description}"


class TaskManager:

    FILENAME = "tasks.json"

    def __init__(self):
        self._tasks = []
        self._next_id = 1
        self.load_tasks()

    def add_task(self, description):
        task = Task(self._next_id, description)
        self._tasks.append(task)
        self._next_id += 1
        self.save_tasks()
        print(f"Tarea anadida: {description}")

    def list_tasks(self):
        if not self._tasks:
            print("No hay tareas pendientes.")
        else:
            for task in self._tasks:
                print(task)

    def complete_task(self, task_id):
        for task in self._tasks:
            if task.id == task_id:
                task.completed = True
                self.save_tasks()
                print(f"Tarea completada: {task.description}")
                return
        print(f"Tarea con ID {task_id} no encontrada.")

    def delete_task(self, task_id):
        for task in self._tasks:
            if task.id == task_id:
                self._tasks.remove(task)
                self.save_tasks()
                print(f"Tarea eliminada: {task.description}")
                print(f"Tarea eliminada: #{task_id}")
                return
        print(f"Tarea con ID {task_id} no encontrada.")

    def load_tasks(self):

        try:
            with open(self.FILENAME, "r") as file:
                tasks_data = json.load(file)
                # self._tasks = [Task(**data) for data in tasks_data]
                self._tasks = [
                    Task(
                        task_data["id"],
                        task_data["description"],
                        task_data["completed"],
                    )
                    for task_data in tasks_data
                ]
                if self._tasks:
                    # self._next_id = max(task.id for task in self._tasks) + 1
                    self._next_id = self._tasks[-1].id + 1
                else:
                    self._next_id = 1

                print(f"Tareas cargadas desde {self.FILENAME}.")

        except FileNotFoundError:
            print(
                f"No se encontro el archivo {self.FILENAME}. Iniciando con una lista vacia."
            )
            self._tasks = []
            self._next_id = 1
        except json.JSONDecodeError:
            print(
                f"Error al decodificar el archivo {self.FILENAME}. Iniciando con una lista vacia."
            )
            self._tasks = []
            self._next_id = 1

    def save_tasks(self):
        with open(self.FILENAME, "w") as file:
            # json.dump([task.__dict__ for task in self._tasks], file, indent=4)
            json.dump(
                [
                    {
                        "id": task.id,
                        "description": task.description,
                        "completed": task.completed,
                    }
                    for task in self._tasks
                ],
                file,
                indent=4,
            )
        print(f"Tareas guardadas en {self.FILENAME}.")
