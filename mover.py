import pyautogui, time, pytz
from datetime import datetime


def move_mouse():
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

    # Get the initial mouse position, ensuring it's not too close to the screen edges
    initial_x, initial_y = pyautogui.position()
    initial_x = max(
        20, initial_x
    )  # Ensures X position is at least 20 pixels from the left edge
    initial_y = max(
        20, initial_y
    )  # Ensures Y position is at least 20 pixels from the top edge

    while datetime.now(est) < end_time:
        # Move the mouse slightly left and right
        pyautogui.moveTo(initial_x + 10, initial_y, duration=0.5)
        time.sleep(0.5)
        pyautogui.moveTo(initial_x - 10, initial_y, duration=0.5)
        time.sleep(0.5)

    print(f"Stopping script at {end_time.strftime('%I:%M %p %Z')}")


if __name__ == "__main__":
    move_mouse()
