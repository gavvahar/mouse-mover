import pyautogui, time, pytz
from datetime import datetime


def move_mouse_and_type():
    est = pytz.timezone("US/Eastern")
    start_time = datetime.now(est)
    print(f"Script started at: {start_time.strftime('%B %d, %Y %I:%M:%S %p %Z')}")

    # Get the end time from the user, convert to uppercase for consistency
    end_time_input = input("Enter the end time (HH:MM AM/PM): ").upper()
    end_time = datetime.strptime(end_time_input, "%I:%M %p")
    end_time = est.localize(
        end_time.replace(
            year=start_time.year, month=start_time.month, day=start_time.day
        )
    )

    initial_x, initial_y = pyautogui.position()
    initial_x = max(100, initial_x)
    initial_y = max(100, initial_y)

    while datetime.now(est) < end_time:
        # Simulate mouse movement
        pyautogui.moveTo(initial_x + 100, initial_y + 100, duration=0.5)
        time.sleep(1)
        pyautogui.moveTo(initial_x - 100, initial_y - 100, duration=0.5)
        time.sleep(1)

        # Simulate a harmless keyboard press
        pyautogui.press("shift")
        time.sleep(1)

    print(f"Stopping script at {end_time.strftime('%I:%M %p %Z')}")


if __name__ == "__main__":
    move_mouse_and_type()
