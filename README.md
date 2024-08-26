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

2. Install virtual environment and activate it:
    ```sh
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`

3. Install the required packages:
    ```sh
    pip3 install -r app/requirements.txt

## Usage

1. Start the FastAPI server:
    ```sh
    uvicorn app.main:app --reload

2. Open your web browser and navigate to the site:
    ```sh
    http://localhost:8000

3. Enter the end time and click "Start Script" to start the mouse mover script
    ```sh
    e.g., 4:00 PM

4. Click "Stop Script" to stop the script manually