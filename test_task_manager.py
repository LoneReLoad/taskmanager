import os
import json
import pytest
from task_manager import TaskManager, Task

TEST_FILENAME = "test_tasks.json"


@pytest.fixture(autouse=True)
def setup_and_teardown(monkeypatch):
    # Patch the filename to avoid interfering with real data
    monkeypatch.setattr(TaskManager, "FILENAME", TEST_FILENAME)
    # Remove test file before and after each test
    yield
    if os.path.exists(TEST_FILENAME):
        os.remove(TEST_FILENAME)


def test_add_task_creates_new_task():
    tm = TaskManager()
    tm.add_task("Test task 1")
    assert len(tm._tasks) == 1
    assert tm._tasks[0].description == "Test task 1"
    assert not tm._tasks[0].completed


def test_list_tasks_prints_tasks(capsys):
    tm = TaskManager()
    tm.add_task("Task A")
    tm.list_tasks()
    captured = capsys.readouterr()
    assert "Task A" in captured.out


def test_complete_task_marks_as_completed(capsys):
    tm = TaskManager()
    tm.add_task("Task to complete")
    task_id = tm._tasks[0].id
    tm.complete_task(task_id)
    assert tm._tasks[0].completed
    captured = capsys.readouterr()
    assert "Tarea completada" in captured.out


def test_complete_task_invalid_id(capsys):
    tm = TaskManager()
    tm.add_task("Task")
    tm.complete_task(999)
    captured = capsys.readouterr()
    assert "no encontrada" in captured.out


def test_delete_task_removes_task(capsys):
    tm = TaskManager()
    tm.add_task("Task to delete")
    task_id = tm._tasks[0].id
    tm.delete_task(task_id)
    assert len(tm._tasks) == 0
    captured = capsys.readouterr()
    assert "Tarea eliminada" in captured.out


def test_delete_task_invalid_id(capsys):
    tm = TaskManager()
    tm.add_task("Task")
    tm.delete_task(999)
    captured = capsys.readouterr()
    assert "no encontrada" in captured.out


def test_save_and_load_tasks_persist_data():
    tm = TaskManager()
    tm.add_task("Persisted task")
    tm.complete_task(tm._tasks[0].id)
    # Create a new manager to load from file
    tm2 = TaskManager()
    assert len(tm2._tasks) == 1
    assert tm2._tasks[0].description == "Persisted task"
    assert tm2._tasks[0].completed


def test_list_tasks_empty_prints_message(capsys):
    tm = TaskManager()
    tm.list_tasks()
    captured = capsys.readouterr()
    assert "No hay tareas pendientes" in captured.out


def test_load_tasks_file_not_found(monkeypatch, capsys):
    # Remove file if exists
    if os.path.exists(TEST_FILENAME):
        os.remove(TEST_FILENAME)
    tm = TaskManager()
    captured = capsys.readouterr()
    assert "No se encontro el archivo" in captured.out


def test_load_tasks_json_decode_error(monkeypatch, capsys):
    with open(TEST_FILENAME, "w") as f:
        f.write("invalid json")
    tm = TaskManager()
    captured = capsys.readouterr()
    assert "Error al decodificar" in captured.out
