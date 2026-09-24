import time
import winsound



def start_pomodoro():
    """Start a Pomodoro study session."""

    study_minutes = 25
    break_minutes = 5

    print("\n===== POMODORO TIMER =====")
    print(f"Study session: {study_minutes} minutes")

    for remaining in range(study_minutes * 60, 0, -1):
        minutes = remaining // 60
        seconds = remaining % 60

        print(
            f"\rTime remaining: {minutes:02d}:{seconds:02d}",
            end="",
            flush=True
        )

        time.sleep(1)

    print("\n\nStudy session complete!")

    for _ in range(3):
        winsound.Beep(1000, 500)
        time.sleep(0.2)
        
    print(f"Take a {break_minutes}-minute break.")


if __name__ == "__main__":
    start_pomodoro()