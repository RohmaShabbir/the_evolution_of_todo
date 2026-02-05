"""
Todo Service - Application Layer for Console Todo Application
"""

from typing import List, Optional
from src.domain.todo import TodoTask
from src.repositories.todo_repository import TodoRepository


class TodoService:
    """
    Application service for managing todo tasks.
    Orchestrates domain logic and repository operations.
    """

    def __init__(self, repository: TodoRepository):
        self.repository = repository

    def create_task(self, title: str, description: str = "") -> TodoTask:
        """
        Create a new todo task.
        """
        # Create a task with a temporary ID (0) to let repository auto-assign
        task = TodoTask(id=0, title=title, description=description, status="incomplete")
        return self.repository.add_task(task)

    def get_all_tasks(self) -> List[TodoTask]:
        """
        Get all tasks.
        """
        return self.repository.get_all_tasks()

    def get_task_by_id(self, task_id: int) -> Optional[TodoTask]:
        """
        Get a task by its ID.
        """
        return self.repository.get_task_by_id(task_id)

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> Optional[TodoTask]:
        """
        Update a task's title and/or description.
        """
        task = self.repository.get_task_by_id(task_id)
        if not task:
            return None

        # Update task data
        task.update_data(title=title, description=description)

        # Save the updated task
        return self.repository.update_task(task_id, task)

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.
        """
        return self.repository.delete_task(task_id)

    def update_task_status(self, task_id: int, status: str) -> Optional[TodoTask]:
        """
        Update a task's completion status.
        """
        task = self.repository.get_task_by_id(task_id)
        if not task:
            return None

        # Validate status
        if status not in ["incomplete", "complete"]:
            raise ValueError(f"Status must be 'incomplete' or 'complete', got '{status}'")

        task.status = status
        return self.repository.update_task(task_id, task)

    def toggle_task_status(self, task_id: int) -> Optional[TodoTask]:
        """
        Toggle a task's completion status.
        """
        task = self.repository.get_task_by_id(task_id)
        if not task:
            return None

        task.toggle_status()
        return self.repository.update_task(task_id, task)