"""
Todo Entity - Domain Model for Console Todo Application
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class TodoTask:
    """
    Represents a single todo item with unique ID, title, description, and completion status.
    """
    id: int
    title: str
    description: str
    status: str = "incomplete"

    def __post_init__(self):
        """Validate the TodoTask upon instantiation."""
        if not self.title or not self.title.strip():
            raise ValueError("Title cannot be empty")

        if self.status not in ["incomplete", "complete"]:
            raise ValueError(f"Status must be 'incomplete' or 'complete', got '{self.status}'")

        # Ensure description is never None
        if self.description is None:
            self.description = ""

    def toggle_status(self) -> None:
        """Toggle the completion status of the task."""
        if self.status == "incomplete":
            self.status = "complete"
        else:
            self.status = "incomplete"

    def update_data(self, title: Optional[str] = None, description: Optional[str] = None) -> None:
        """Update the title and/or description of the task."""
        if title is not None:
            if not title.strip():
                raise ValueError("Title cannot be empty")
            self.title = title

        if description is not None:
            # Ensure description is never None
            if description is None:
                self.description = ""
            else:
                self.description = description