from planner.storage import load_data, save_data


def add_task():
    """Add a new study task."""

    data = load_data()

    subject = input("Enter subject: ")
    topic = input("Enter topic: ")
    priority = input("Enter priority (Low/Medium/High): ")

    task = {
        "subject": subject,
        "topic": topic,
        "priority": priority,
        "completed": False
    }

    data["tasks"].append(task)
    save_data(data)

    print("\nTask added successfully!")


def view_tasks():
    """Display all study tasks."""

    data = load_data()

    if not data["tasks"]:
        print("\nNo study tasks found.")
        return

    print("\n===== STUDY TASKS =====")

    for number, task in enumerate(data["tasks"], start=1):
        status = "Completed" if task["completed"] else "Pending"

        print(f"\n{number}. {task['subject']} - {task['topic']}")
        print(f"   Priority: {task['priority']}")
        print(f"   Status: {status}")


def complete_task():
    """Mark a task as completed."""

    data = load_data()

    if not data["tasks"]:
        print("\nNo tasks available.")
        return

    view_tasks()

    try:
        task_number = int(input("\nEnter task number to complete: "))

        if 1 <= task_number <= len(data["tasks"]):
            data["tasks"][task_number - 1]["completed"] = True
            save_data(data)
            print("\nTask marked as completed!")
        else:
            print("\nInvalid task number.")

    except ValueError:
        print("\nPlease enter a valid number.")


def delete_task():
    """Delete a study task."""

    data = load_data()

    if not data["tasks"]:
        print("\nNo tasks available.")
        return

    view_tasks()

    try:
        task_number = int(input("\nEnter task number to delete: "))

        if 1 <= task_number <= len(data["tasks"]):
            deleted_task = data["tasks"].pop(task_number - 1)
            save_data(data)

            print(f"\nDeleted: {deleted_task['topic']}")
        else:
            print("\nInvalid task number.")

    except ValueError:
        print("\nPlease enter a valid number.")