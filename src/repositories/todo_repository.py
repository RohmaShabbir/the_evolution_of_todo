"""
Todo Repository - In-Memory Storage Abstraction for Console Todo Application
"""

from typing import Dict, List, Optional
from src.domain.todo import TodoTask


class TodoRepository:
    """
    In-memory repository for storing and managing TodoTask entities.
    """

    def __init__(self):
        self._tasks: Dict[int, TodoTask] = {}
        self._next_id = 1

    def add_task(self, task: TodoTask) -> TodoTask:
        """
        Add a new task to the repository.
        """
        if task.id == 0:  # Auto-assign ID if not provided
            task.id = self._next_id
            self._next_id += 1
        elif task.id >= self._next_id:
            self._next_id = task.id + 1

        self._tasks[task.id] = task
        return task

    def get_task_by_id(self, task_id: int) -> Optional[TodoTask]:
        """
        Retrieve a task by its ID.
        """
        return self._tasks.get(task_id)

    def get_all_tasks(self) -> List[TodoTask]:
        """
        Retrieve all tasks.
        """
        return list(self._tasks.values())

    def update_task(self, task_id: int, updated_task: TodoTask) -> Optional[TodoTask]:
        """
        Update a task with the given ID.
        """
        if task_id not in self._tasks:
            return None

        self._tasks[task_id] = updated_task
        return updated_task

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.
        """
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False

    def get_next_id(self) -> int:
        """
        Get the next available ID for a new task.
        """
        return self._next_id