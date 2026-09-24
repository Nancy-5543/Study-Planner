from datetime import date, timedelta

from planner.storage import load_data, save_data


REVISION_INTERVALS = [1, 3, 7, 14, 30]


def add_revision():
    """Add a topic to the spaced repetition schedule."""

    data = load_data()

    subject = input("Enter subject: ")
    topic = input("Enter topic: ")

    revision = {
        "subject": subject,
        "topic": topic,
        "revision_number": 1,
        "next_revision": str(
            date.today() + timedelta(days=REVISION_INTERVALS[0])
        )
    }

    data["revisions"].append(revision)
    save_data(data)

    print("\nRevision topic added successfully!")
    print(f"Next revision: {revision['next_revision']}")


def view_revisions():
    """Display scheduled revisions."""

    data = load_data()

    if not data["revisions"]:
        print("\nNo revision topics found.")
        return

    print("\n===== SPACED REPETITION =====")

    for number, revision in enumerate(data["revisions"], start=1):
        print(f"\n{number}. {revision['subject']} - {revision['topic']}")
        print(f"   Revision: {revision['revision_number']}")
        print(f"   Next revision: {revision['next_revision']}")


def complete_revision():
    """Complete a revision and schedule the next one."""

    data = load_data()

    if not data["revisions"]:
        print("\nNo revision topics found.")
        return

    view_revisions()

    try:
        revision_number = int(input("\nEnter revision number completed: "))

        if 1 <= revision_number <= len(data["revisions"]):

            revision = data["revisions"][revision_number - 1]

            current_number = revision["revision_number"]

            if current_number < len(REVISION_INTERVALS):
                current_number += 1

            revision["revision_number"] = current_number

            interval = REVISION_INTERVALS[current_number - 1]

            revision["next_revision"] = str(
                date.today() + timedelta(days=interval)
            )

            save_data(data)

            print("\nRevision completed!")
            print(f"Next revision: {revision['next_revision']}")

        else:
            print("\nInvalid revision number.")

    except ValueError:
        print("\nPlease enter a valid number.")

def delete_revision():
    """Delete a revision topic."""

    data = load_data()

    if not data["revisions"]:
        print("\nNo revision topics found.")
        return

    view_revisions()

    try:
        revision_number = int(input("\nEnter revision number to delete: "))

        if 1 <= revision_number <= len(data["revisions"]):
            deleted_revision = data["revisions"].pop(revision_number - 1)

            save_data(data)

            print(
                f"\nDeleted revision: "
                f"{deleted_revision['subject']} - "
                f"{deleted_revision['topic']}"
            )

        else:
            print("\nInvalid revision number.")

    except ValueError:
        print("\nPlease enter a valid number.")


if __name__ == "__main__":
    add_revision()
    view_revisions()
    complete_revision()
    delete_revision()