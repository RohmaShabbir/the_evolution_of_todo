# Quickstart Guide: Console Todo Application

## Setup

1. Ensure Python 3.13+ is installed on your system
2. Clone the repository
3. Navigate to the project directory

## Running the Application

Execute the main application file:

```bash
python src/main.py
```

## Basic Usage

Once the application starts, you'll see a menu with the following options:

1. **Add Task** - Create a new todo task
   - Enter a title (required)
   - Optionally enter a description
   - Task is created with "incomplete" status

2. **View All Tasks** - Display all tasks
   - Shows ID, title, description, and status for each task
   - Incomplete tasks marked with ○
   - Complete tasks marked with ✓

3. **Update Task** - Modify an existing task
   - Enter the task ID
   - Update title and/or description
   - Task details are updated in the system

4. **Delete Task** - Remove a task
   - Enter the task ID
   - Task is permanently removed from the system

5. **Toggle Task Status** - Mark complete/incomplete
   - Enter the task ID
   - Task status toggles between "incomplete" and "complete"

6. **Exit** - Quit the application
   - Safely exit the application

## Example Session

```
Welcome to the Todo Application!
1. Add Task
2. View All Tasks
3. Update Task
4. Delete Task
5. Toggle Task Status
6. Exit

Choose an option: 1
Enter task title: Buy groceries
Enter task description: Milk, bread, eggs
Task added with ID: 1

Choose an option: 2
ID: 1 | Title: Buy groceries | Description: Milk, bread, eggs | Status: ○ incomplete
```

## Error Handling

- Invalid task IDs will show an error message
- Empty titles will be rejected when adding/updating tasks
- Unknown commands will prompt for valid options