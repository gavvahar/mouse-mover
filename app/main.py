import asyncio
from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import pyautogui
import pytz
from datetime import datetime
import threading

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


class EndTime(BaseModel):
    end_time: str


# Global variable to manage script status
script_status = {"running": False, "message": ""}


def run_mouse_script(end_time_str: str):
    est = pytz.timezone("US/Eastern")
    end_time = datetime.strptime(end_time_str, "%I:%M %p")
    end_time = est.localize(datetime.combine(datetime.now(est).date(), end_time.time()))

    global script_status
    script_status["running"] = True
    script_status["message"] = ""

    start_time = datetime.now(est)
    print(f"Script started at: {start_time.strftime('%B %d, %Y %I:%M:%S %p %Z')}")

    initial_x, initial_y = pyautogui.position()
    initial_x = max(20, initial_x)
    initial_y = max(20, initial_y)
    shift_pressed = False

    while datetime.now(est) < end_time:
        if not shift_pressed:
            pyautogui.keyDown("shift")
            shift_pressed = True

        pyautogui.moveTo(initial_x + 10, initial_y, duration=0.5)
        pyautogui.moveTo(initial_x - 10, initial_y, duration=0.5)

        # Check if the script has been stopped by the user
        if not script_status["running"]:
            break

    if shift_pressed:
        pyautogui.keyUp("shift")

    script_status["running"] = False
    if datetime.now(est) >= end_time:
        script_status["message"] = "Script has finished running."
    else:
        script_status["message"] = "Script stopped."


@app.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/start")
async def start_script(end_time: EndTime):
    if script_status["running"]:
        return {"status": "Script already running"}

    thread = threading.Thread(target=run_mouse_script, args=(end_time.end_time,))
    thread.start()
    return {"status": "Script started"}


@app.post("/stop")
async def stop_script():
    if not script_status["running"]:
        return {"status": "No script is currently running"}

    # Just setting the message here. You would need a mechanism to force stop
    script_status["message"] = "Script stopped by user"
    script_status["running"] = False
    return {"status": "Script stopped"}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            if script_status["running"]:
                await websocket.send_text("Script is running")
            elif script_status["message"]:
                await websocket.send_text(script_status["message"])
            await asyncio.sleep(1)
    except WebSocketDisconnect:
        print("WebSocket connection closed")
