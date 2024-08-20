import pyautogui, time, pytz
from datetime import datetime


def move_mouse():
    est = pytz.timezone("US/Eastern")
    start_time = datetime.now(est)
    print(f"Script started at: {start_time.strftime('%B %d, %Y %I:%M:%S %p %Z')}")

    # Get the initial mouse position
    initial_x, initial_y = pyautogui.position()

    while datetime.now(est).hour < 17:
        # Move the mouse slightly left and right
        pyautogui.moveTo(initial_x + 10, initial_y, duration=0.5)
        time.sleep(0.5)
        pyautogui.moveTo(initial_x - 10, initial_y, duration=0.5)
        time.sleep(0.5)

    print("Stopping script at 5 PM EST")


if __name__ == "__main__":
    move_mouse()
