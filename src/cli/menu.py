"""
CLI Menu - Main Interface for Console Todo Application
"""

from typing import Optional
from src.services.todo_service import TodoService
from src.cli.prompts import (
    get_user_input, get_task_details_from_user, get_task_id_from_user,
    get_choice_from_user, display_message, confirm_action
)


class TodoMenu:
    """
    Main menu interface for the todo application.
    """

    def __init__(self, todo_service: TodoService):
        self.service = todo_service

    def display_menu(self) -> None:
        """
        Display the main menu options.
        """
        print("\n" + "="*50)
        print("TODO APPLICATION")
        print("="*50)
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Toggle Task Status")
        print("6. Help")
        print("7. Exit")
        print("-"*50)

    def display_help(self) -> None:
        """
        Display help information.
        """
        help_text = """
        HELP - Todo Application

        This is a simple console-based todo application.

        Available Commands:
        1. Add Task - Create a new todo task with title and description
        2. View All Tasks - List all tasks with their status
        3. Update Task - Modify an existing task's title or description
        4. Delete Task - Remove a task by its ID
        5. Toggle Task Status - Mark a task as complete/incomplete
        6. Help - Show this help information
        7. Exit - Quit the application

        Task Status Indicators:
        - ○ incomplete: Task is not yet completed
        - ✓ complete: Task has been completed

        Each task has a unique ID that is displayed when viewing tasks.
        """
        display_message(help_text)

    def add_task(self) -> None:
        """
        Handle adding a new task.
        """
        try:
            title, description = get_task_details_from_user()
            task = self.service.create_task(title, description)
            display_message(f"\n✓ Task added successfully with ID: {task.id}")
        except ValueError as e:
            display_message(f"\n✗ Error: {str(e)}")
        except Exception as e:
            display_message(f"\n✗ Unexpected error: {str(e)}")

    def view_tasks(self) -> None:
        """
        Handle viewing all tasks.
        """
        tasks = self.service.get_all_tasks()
        if not tasks:
            display_message("\nNo tasks found.")
            return

        display_message("\nTASK LIST:")
        for task in tasks:
            status_indicator = "✓" if task.status == "complete" else "○"
            print(f"ID: {task.id} | {status_indicator} {task.status.upper()} | "
                  f"Title: {task.title} | Description: {task.description}")

    def update_task(self) -> None:
        """
        Handle updating a task.
        """
        try:
            task_id = get_task_id_from_user()
            task = self.service.get_task_by_id(task_id)
            if not task:
                display_message(f"\n✗ No task found with ID: {task_id}")
                return

            print(f"Current task: ID {task.id} | {task.title} | {task.description}")

            title_input = get_user_input("Enter new title (leave empty to keep current): ").strip()
            description_input = get_user_input("Enter new description (leave empty to keep current): ").strip()

            # Only update fields that were provided
            title = title_input if title_input else None
            description = description_input if description_input else None

            updated_task = self.service.update_task(task_id, title, description)
            if updated_task:
                display_message(f"\n✓ Task updated successfully")
            else:
                display_message(f"\n✗ Failed to update task with ID: {task_id}")
        except ValueError as e:
            display_message(f"\n✗ Error: {str(e)}")
        except Exception as e:
            display_message(f"\n✗ Unexpected error: {str(e)}")

    def delete_task(self) -> None:
        """
        Handle deleting a task.
        """
        try:
            task_id = get_task_id_from_user()
            task = self.service.get_task_by_id(task_id)
            if not task:
                display_message(f"\n✗ No task found with ID: {task_id}")
                return

            print(f"Task to delete: ID {task.id} | {task.title}")
            if confirm_action("Are you sure you want to delete this task?"):
                success = self.service.delete_task(task_id)
                if success:
                    display_message(f"\n✓ Task with ID {task_id} deleted successfully")
                else:
                    display_message(f"\n✗ Failed to delete task with ID: {task_id}")
            else:
                display_message("\n✗ Deletion cancelled")
        except ValueError as e:
            display_message(f"\n✗ Error: {str(e)}")
        except Exception as e:
            display_message(f"\n✗ Unexpected error: {str(e)}")

    def toggle_task_status(self) -> None:
        """
        Handle toggling a task's status.
        """
        try:
            task_id = get_task_id_from_user()
            task = self.service.get_task_by_id(task_id)
            if not task:
                display_message(f"\n✗ No task found with ID: {task_id}")
                return

            current_status = task.status
            updated_task = self.service.toggle_task_status(task_id)
            if updated_task:
                new_status = updated_task.status
                display_message(f"\n✓ Task status changed from '{current_status}' to '{new_status}'")
            else:
                display_message(f"\n✗ Failed to update task status for ID: {task_id}")
        except ValueError as e:
            display_message(f"\n✗ Error: {str(e)}")
        except Exception as e:
            display_message(f"\n✗ Unexpected error: {str(e)}")

    def run(self) -> None:
        """
        Main loop to run the menu interface.
        """
        display_message("Welcome to the Todo Application!")
        while True:
            self.display_menu()
            try:
                choice = get_choice_from_user()

                if choice in ['1', 'add', 'a']:
                    self.add_task()
                elif choice in ['2', 'view', 'v']:
                    self.view_tasks()
                elif choice in ['3', 'update', 'u']:
                    self.update_task()
                elif choice in ['4', 'delete', 'd']:
                    self.delete_task()
                elif choice in ['5', 'toggle', 't']:
                    self.toggle_task_status()
                elif choice in ['6', 'help', 'h']:
                    self.display_help()
                elif choice in ['7', 'exit', 'quit', 'q']:
                    display_message("\nThank you for using the Todo Application. Goodbye!")
                    break
                else:
                    display_message(f"\n✗ Invalid choice: '{choice}'. Please select a valid option.")

            except KeyboardInterrupt:
                display_message("\n\nOperation cancelled by user. Exiting...")
                break
            except Exception as e:
                display_message(f"\n✗ Unexpected error occurred: {str(e)}")
                display_message("Please try again.")