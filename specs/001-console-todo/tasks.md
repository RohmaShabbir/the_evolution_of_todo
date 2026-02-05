# Task List: Console Todo Application

**Feature**: console-todo
**Created**: 2026-02-04
**Input**: Feature specification from `/specs/001-console-todo/spec.md`

## Phase 1: Setup

Initialize project structure and foundational components per implementation plan.

- [X] T001 Create project directory structure with src/, tests/ folders
- [X] T002 Initialize Python project with appropriate directory structure
- [X] T003 Create empty __init__.py files in all directories for importability
- [X] T004 Create README.md with project description and setup instructions
- [X] T005 Create requirements.txt with no external dependencies (standard library only)

## Phase 2: Foundation

Establish foundational components required for all user stories.

- [X] T006 [P] Create TodoTask data model in src/domain/todo.py
- [X] T007 [P] Create TodoRepository in-memory implementation in src/repositories/todo_repository.py
- [X] T008 [P] Create TodoService application layer in src/services/todo_service.py
- [X] T009 [P] Create CLI menu interface in src/cli/menu.py
- [X] T010 [P] Create CLI prompts helper in src/cli/prompts.py
- [X] T011 Create main application entry point in src/main.py

## Phase 3: User Story 1 - Add Todo Task (Priority: P1)

User can add a new todo task with a title and description via the console interface. Independent test: Can be fully tested by entering "add" command and verifying the task appears in the task list with a unique ID.

- [X] T012 [P] [US1] Implement TodoTask constructor with validation in src/domain/todo.py
- [X] T013 [P] [US1] Implement add_task method in TodoRepository in src/repositories/todo_repository.py
- [X] T014 [P] [US1] Implement create_task method in TodoService in src/services/todo_service.py
- [X] T015 [P] [US1] Implement add task functionality in CLI menu src/cli/menu.py
- [X] T016 [US1] Test add task functionality end-to-end

## Phase 4: User Story 2 - View All Tasks (Priority: P1)

User can view a list of all todo tasks with their current status indicators. Independent test: Can be fully tested by entering "view" or "list" command and seeing all tasks with their IDs, titles, descriptions, and completion status.

- [X] T017 [P] [US2] Implement get_all_tasks method in TodoRepository in src/repositories/todo_repository.py
- [X] T018 [P] [US2] Implement get_all_tasks method in TodoService in src/services/todo_service.py
- [X] T019 [P] [US2] Implement view tasks functionality in CLI menu src/cli/menu.py
- [X] T020 [US2] Test view tasks functionality end-to-end

## Phase 5: User Story 5 - Toggle Task Completion Status (Priority: P1)

User can mark tasks as complete or incomplete by specifying their unique ID. Independent test: Can be fully tested by toggling a task's status and verifying the change in the task list.

- [X] T021 [P] [US5] Implement toggle_status method in TodoTask entity in src/domain/todo.py
- [X] T022 [P] [US5] Implement update_task method in TodoRepository in src/repositories/todo_repository.py
- [X] T023 [P] [US5] Implement update_task_status method in TodoService in src/services/todo_service.py
- [X] T024 [P] [US5] Implement toggle task status functionality in CLI menu src/cli/menu.py
- [X] T025 [US5] Test toggle task status functionality end-to-end

## Phase 6: User Story 3 - Update Task Details (Priority: P2)

User can update the title and/or description of an existing task by specifying its unique ID. Independent test: Can be fully tested by selecting a task by ID and modifying its properties, then verifying the changes are reflected.

- [X] T026 [P] [US3] Implement update_task_data method in TodoTask entity in src/domain/todo.py
- [X] T027 [P] [US3] Implement update_task_by_id method in TodoRepository in src/repositories/todo_repository.py
- [X] T028 [P] [US3] Implement update_task method in TodoService in src/services/todo_service.py
- [X] T029 [P] [US3] Implement update task functionality in CLI menu src/cli/menu.py
- [X] T030 [US3] Test update task functionality end-to-end

## Phase 7: User Story 4 - Delete Tasks (Priority: P2)

User can remove tasks by specifying their unique ID. Independent test: Can be fully tested by selecting a task by ID and deleting it, then verifying it no longer appears in the task list.

- [X] T031 [P] [US4] Implement delete_task method in TodoRepository in src/repositories/todo_repository.py
- [X] T032 [P] [US4] Implement delete_task method in TodoService in src/services/todo_service.py
- [X] T033 [P] [US4] Implement delete task functionality in CLI menu src/cli/menu.py
- [X] T034 [US4] Test delete task functionality end-to-end

## Phase 8: Polish & Cross-Cutting Concerns

Finalize implementation with error handling, validation, and user experience improvements.

- [X] T035 [P] Add input validation for all user inputs across CLI layer
- [X] T036 [P] Add error handling for invalid IDs and non-existent tasks
- [X] T037 [P] Improve user interface with clear status indicators and feedback
- [X] T038 [P] Add help documentation and menu navigation instructions
- [X] T039 [P] Implement graceful exit functionality
- [X] T040 Conduct full integration testing of all user stories

## Dependencies

- User Story 1 (Add Task) → Foundational components (T006-T011)
- User Story 2 (View Tasks) → Foundational components and TodoTask (T006-T011, T012)
- User Story 5 (Toggle Status) → Foundational components and TodoTask (T006-T011, T012)
- User Story 3 (Update Task) → Foundational components and TodoTask (T006-T011, T012)
- User Story 4 (Delete Task) → Foundational components and TodoRepository (T006-T011, T007)

## Parallel Execution Examples

Within User Story 1:
- T012, T013, T014 can run in parallel (different files: todo.py, todo_repository.py, todo_service.py)
- T015 can run after T014 (depends on service implementation)

Within User Story 2:
- T017, T018 can run in parallel (repository and service layers)
- T019 depends on T018 (CLI needs service methods)

## Implementation Strategy

1. **MVP First**: Complete Phase 1 (Setup) and Phase 2 (Foundation) to establish basic architecture
2. **Incremental Delivery**: Implement high-priority user stories (P1) first - Add Task, View Tasks, Toggle Status
3. **Iterative Enhancement**: Add lower-priority stories (P2) - Update Task, Delete Task
4. **Polish Phase**: Complete cross-cutting concerns and error handling