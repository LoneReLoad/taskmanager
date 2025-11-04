class Task:
    def __init__(self, id, description, completed=False):
        self.id = id
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "✓" if self.completed else " "
        return f"[{status}] #{self.id}: {self.description}"


class TaskManager:
    def __init__(self):
        self._tasks = []
        self._next_id = 1

    def add_task(self, description):
        task = Task(self._next_id, description)
        self._tasks.append(task)
        self._next_id += 1
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
                print(f"Tarea completada: {task.description}")
                return
        print(f"Tarea con ID {task_id} no encontrada.")

    def delete_task(self, task_id):
        for task in self._tasks:
            if task.id == task_id:
                self._tasks.remove(task)
                print(f"Tarea eliminada: {task.description}")
                print(f"Tarea eliminada: #{task_id}")
                return
        print(f"Tarea con ID {task_id} no encontrada.")
