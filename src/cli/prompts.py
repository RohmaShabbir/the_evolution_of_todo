"""
CLI Prompts - User Input Helpers for Console Todo Application
"""


def get_user_input(prompt: str) -> str:
    """
    Get input from the user with a prompt.
    """
    return input(prompt).strip()


def get_task_details_from_user() -> tuple[str, str]:
    """
    Get task title and description from user input.
    Returns tuple of (title, description).
    """
    title = get_user_input("Enter task title: ").strip()
    if not title:
        raise ValueError("Title cannot be empty")

    description = get_user_input("Enter task description (optional): ").strip()
    return title, description


def get_task_id_from_user() -> int:
    """
    Get task ID from user input and validate it's a positive integer.
    """
    try:
        task_id = int(get_user_input("Enter task ID: "))
        if task_id <= 0:
            raise ValueError("Task ID must be a positive integer")
        return task_id
    except ValueError as e:
        if "invalid literal" in str(e):
            raise ValueError("Task ID must be a number")
        raise e


def get_choice_from_user() -> str:
    """
    Get menu choice from user input.
    """
    return get_user_input("Choose an option: ").strip().lower()


def display_message(message: str) -> None:
    """
    Display a message to the user.
    """
    print(message)


def confirm_action(prompt: str) -> bool:
    """
    Ask the user to confirm an action.
    """
    response = get_user_input(f"{prompt} (y/N): ").strip().lower()
    return response in ['y', 'yes']