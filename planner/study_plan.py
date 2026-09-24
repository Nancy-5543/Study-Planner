from planner.storage import load_data, save_data


def create_study_plan():
    """Create a study plan for a task."""

    data = load_data()

    if not data["tasks"]:
        print("\nNo study tasks available.")
        print("Add a task first.")
        return

    print("\n===== CREATE STUDY PLAN =====")

    for number, task in enumerate(data["tasks"], start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(
            f"{number}. {task['subject']} - "
            f"{task['topic']} ({status})"
        )

    try:
        task_number = int(input("\nEnter task number: "))

        if 1 <= task_number <= len(data["tasks"]):
            study_date = input("Enter study date (YYYY-MM-DD): ")
            duration = input("Enter study duration in minutes: ")

            task = data["tasks"][task_number - 1]

            task["study_date"] = study_date
            task["duration"] = duration

            save_data(data)

            print("\nStudy plan created successfully!")

        else:
            print("\nInvalid task number.")

    except ValueError:
        print("\nPlease enter a valid number.")


def view_study_plan():
    """Display the study plan."""

    data = load_data()

    planned_tasks = [
        task for task in data["tasks"]
        if "study_date" in task
    ]

    if not planned_tasks:
        print("\nNo study plans found.")
        return

    print("\n===== STUDY PLAN =====")

    for number, task in enumerate(planned_tasks, start=1):
        print(f"\n{number}. {task['subject']} - {task['topic']}")
        print(f"   Date: {task['study_date']}")
        print(f"   Duration: {task['duration']} minutes")