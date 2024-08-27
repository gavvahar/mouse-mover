# Mouse Mover Application

This is a simple desktop application that allows you to start and stop a script that moves the mouse cursor back and forth until a specified end time. The application is built using PyQt for the GUI.

## Features

- Start the mouse mover script with a specified end time.
- Stop the mouse mover script manually.
- Real-time status updates within the application.

## Requirements

- Python 3.7+
- The following Python packages (listed in `requirements.txt`):
  - `pyautogui`
  - `pytz`
  - `PyQt5`

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/gavvahar/mouse-mover.git
   cd mouse-mover

2. Install virtual environment and activate it:
    ```sh
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`

3. Install the required packages:
    ```sh
    pip3 install -r app/requirements.txt

## Usage

1. Run the application:
    ```sh
    python3 main.py
    
2. Enter the end time and click "Start Script" to start the mouse mover script
    ```sh
    e.g., 4:00 PM

3. Click "Stop Script" to stop the script manually