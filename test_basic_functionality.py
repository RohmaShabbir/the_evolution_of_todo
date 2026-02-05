"""
Basic functionality test for the Console Todo Application
"""

import sys
import os
sys.path.insert(0, os.path.abspath('.'))

def test_imports():
    """Test that all modules can be imported correctly."""
    try:
        from src.repositories.todo_repository import TodoRepository
        from src.services.todo_service import TodoService
        from src.domain.todo import TodoTask
        from src.cli.menu import TodoMenu
        from src.cli.prompts import get_user_input

        print("[PASS] All modules imported successfully")

        # Test basic functionality
        repo = TodoRepository()
        service = TodoService(repo)

        # Test creating a task
        task = service.create_task("Test Task", "This is a test description")
        print(f"[PASS] Task created successfully with ID: {task.id}")

        # Test retrieving the task
        retrieved_task = service.get_task_by_id(task.id)
        assert retrieved_task is not None
        assert retrieved_task.title == "Test Task"
        assert retrieved_task.description == "This is a test description"
        assert retrieved_task.status == "incomplete"
        print("[PASS] Task retrieved and verified successfully")

        # Test updating task status
        toggled_task = service.toggle_task_status(task.id)
        assert toggled_task is not None
        assert toggled_task.status == "complete"
        print("[PASS] Task status toggled successfully")

        # Test getting all tasks
        all_tasks = service.get_all_tasks()
        assert len(all_tasks) == 1
        print("[PASS] All tasks retrieved successfully")

        # Test updating task
        updated_task = service.update_task(task.id, "Updated Test Task", "Updated description")
        assert updated_task is not None
        assert updated_task.title == "Updated Test Task"
        print("[PASS] Task updated successfully")

        # Test deleting task
        deleted = service.delete_task(task.id)
        assert deleted is True
        print("[PASS] Task deleted successfully")

        # Verify task is gone
        all_tasks_after_delete = service.get_all_tasks()
        assert len(all_tasks_after_delete) == 0
        print("[PASS] Task confirmed deleted from repository")

        print("\n[SUCCESS] All basic functionality tests passed!")
        return True

    except Exception as e:
        print(f"[FAIL] Test failed with error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_imports()
    if success:
        print("\n[SUCCESS] Console Todo Application is working correctly!")
    else:
        print("\n[ERROR] Console Todo Application has issues!")
        sys.exit(1)