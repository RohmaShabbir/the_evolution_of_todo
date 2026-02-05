"""
Main Entry Point - Console Todo Application
"""

from src.repositories.todo_repository import TodoRepository
from src.services.todo_service import TodoService
from src.cli.menu import TodoMenu


def main():
    """
    Main function to run the console todo application.
    """
    # Initialize the application components following clean architecture
    repository = TodoRepository()
    service = TodoService(repository)
    menu = TodoMenu(service)

    # Run the menu interface
    menu.run()


if __name__ == "__main__":
    main()