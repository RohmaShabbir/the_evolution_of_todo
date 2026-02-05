# Data Model: Console Todo Application

## TodoTask Entity

**Fields:**
- `id`: int - Unique identifier for the task (auto-generated incremental integer)
- `title`: str - Title of the todo task (required, non-empty)
- `description`: str - Description of the todo task (optional, can be empty)
- `status`: str - Completion status of the task (values: "incomplete", "complete")

**Validation Rules:**
- `title` must not be empty or None
- `id` must be unique within the system
- `status` must be either "incomplete" or "complete"
- `description` can be empty but not None

**State Transitions:**
- From "incomplete" to "complete" when task is marked as done
- From "complete" to "incomplete" when task is marked as undone

## TaskList Container

**Fields:**
- `tasks`: list - Collection of TodoTask objects stored in memory
- `next_id`: int - Counter for generating unique IDs for new tasks

**Operations:**
- Add task to collection
- Remove task by ID
- Find task by ID
- Get all tasks
- Update task by ID

## Relationships
- TaskList contains multiple TodoTask entities
- Each TodoTask has a unique ID within the TaskList