# Mouse Mover Application

This is a simple web application that allows you to start and stop a script that moves the mouse cursor back and forth until a specified end time. The application is built using FastAPI for the backend and vanilla JavaScript for the frontend.

## Features

- Start the mouse mover script with a specified end time.
- Stop the mouse mover script manually.
- Real-time status updates via WebSocket.

## Requirements

- Python 3.7+
- The following Python packages (listed in `requirements.txt`):
  - `pyautogui`
  - `pytz`
  - `fastapi`
  - `uvicorn`
  - `pynput`
  - `jinja2`
  - `websockets`

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/mouse-mover.git
   cd mouse-mover