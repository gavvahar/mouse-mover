import sys
import pyautogui
import pytz
from datetime import datetime
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox,
)
from PyQt5.QtCore import QThread, pyqtSignal


class MouseMoverThread(QThread):
    status_signal = pyqtSignal(str)

    def __init__(self, end_time_str):
        super().__init__()
        self.end_time_str = end_time_str
        self.running = True

    def run(self):
        est = pytz.timezone("US/Eastern")
        end_time = datetime.strptime(self.end_time_str, "%I:%M %p")
        end_time = est.localize(
            datetime.combine(datetime.now(est).date(), end_time.time())
        )

        start_time = datetime.now(est)
        self.status_signal.emit(
            f"Script started at: {start_time.strftime('%B %d, %Y %I:%M:%S %p %Z')}"
        )

        initial_x, initial_y = pyautogui.position()
        initial_x = max(20, initial_x)
        initial_y = max(20, initial_y)
        shift_pressed = False

        while datetime.now(est) < end_time and self.running:
            if not shift_pressed:
                pyautogui.keyDown("shift")
                shift_pressed = True

            pyautogui.moveTo(initial_x + 10, initial_y, duration=0.5)
            pyautogui.moveTo(initial_x - 10, initial_y, duration=0.5)

        if shift_pressed:
            pyautogui.keyUp("shift")

        if datetime.now(est) >= end_time:
            self.status_signal.emit("Script has finished running.")
        else:
            self.status_signal.emit("Script stopped.")

    def stop(self):
        self.running = False


class MouseMoverApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.thread = None

    def initUI(self):
        self.setWindowTitle("Mouse Mover Application")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.label = QLabel("End Time (e.g., 4:00 PM):", self)
        layout.addWidget(self.label)

        self.end_time_input = QLineEdit(self)
        layout.addWidget(self.end_time_input)

        self.start_button = QPushButton("Start Script", self)
        self.start_button.clicked.connect(self.start_script)
        layout.addWidget(self.start_button)

        self.stop_button = QPushButton("Stop Script", self)
        self.stop_button.clicked.connect(self.stop_script)
        layout.addWidget(self.stop_button)

        self.response_label = QLabel("", self)
        layout.addWidget(self.response_label)

        self.setLayout(layout)

    def start_script(self):
        end_time = self.end_time_input.text()
        if not end_time:
            QMessageBox.warning(self, "Input Error", "Please enter a valid end time.")
            return

        self.thread = MouseMoverThread(end_time)
        self.thread.status_signal.connect(self.update_status)
        self.thread.start()
        self.response_label.setText("Script started")

    def stop_script(self):
        if self.thread:
            self.thread.stop()
            self.thread = None
            self.response_label.setText("Script stopped")

    def update_status(self, message):
        self.response_label.setText(message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MouseMoverApp()
    ex.show()
    sys.exit(app.exec_())
