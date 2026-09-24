from planner.task_manager import (
    add_task,
    view_tasks,
    complete_task,
    delete_task
)

from planner.spaced_repetition import (
    add_revision,
    view_revisions,
    complete_revision,
    delete_revision
)

from planner.study_plan import (
    create_study_plan,
    view_study_plan
)

from planner.pomodoro import start_pomodoro

def main():
    while True:
        print("\n===== STUDY PLANNER =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Start Pomodoro")
        print("6. Add Revision")
        print("7. View Revisions")
        print("8. Complete Revision")
        print("9. Delete Revision")
        print("10. Create Study Plan")
        print("11. View Study Plan")
        print("12. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            complete_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            start_pomodoro()

        elif choice =="6":
            add_revision()

        elif choice == "7":
            view_revisions()

        elif choice == "8":
            complete_revision()

        elif choice == "9":
            delete_revision()

        elif choice == "10":
            create_study_plan()

        elif choice == "11":
            view_study_plan()

        elif choice == "12":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()