import pyautogui, time, pytz
from datetime import datetime


def move_mouse():
    est = pytz.timezone("US/Eastern")
    start_time = datetime.now(est)
    print(f"Script started at: {start_time.strftime('%B %d, %Y %I:%M:%S %p %Z')}")

    while datetime.now(est).hour < 17:
        for x, y in [(100, 100), (200, 100), (200, 200), (100, 200)]:
            pyautogui.moveTo(x, y, duration=1)
            time.sleep(1)

    print("Stopping script at 5 PM EST")


if __name__ == "__main__":
    move_mouse()
