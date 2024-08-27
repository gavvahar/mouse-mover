import sys, pyautogui, pytz
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
from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtCore import QThread, pyqtSignal, Qt


class MouseMoverThread(QThread):
    status_signal = pyqtSignal(str)

    def __init__(self, end_time_str):
        super().__init__()
        self.end_time_str = end_time_str
        self.running = True

    def run(self):
        est = pytz.timezone("US/Eastern")
        end_time = est.localize(
            datetime.combine(
                datetime.now(est).date(),
                datetime.strptime(self.end_time_str, "%I:%M %p").time(),
            )
        )
        initial_x, initial_y, shift_pressed = (
            max(20, pyautogui.position()[0]),
            max(20, pyautogui.position()[1]),
            False,
        )
        self.status_signal.emit(
            f"Script started at: {datetime.now(est).strftime('%B %d, %Y %I:%M:%S %p %Z')}"
        )

        while datetime.now(est) < end_time and self.running:
            if not shift_pressed:
                pyautogui.keyDown("shift")
                shift_pressed = True
            pyautogui.moveTo(initial_x + 10, initial_y, duration=0.5)
            pyautogui.moveTo(initial_x - 10, initial_y, duration=0.5)

        if shift_pressed:
            pyautogui.keyUp("shift")
        self.status_signal.emit(
            "Script finished." if datetime.now(est) >= end_time else "Script stopped."
        )

    def stop(self):
        self.running = False


class MouseMoverApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Mouse Mover App")
        self.setGeometry(100, 100, 400, 250)
        self.setPalette(QPalette(QColor("#2E2E2E"), QColor(Qt.white)))

        layout = QVBoxLayout(self)
        self.label, self.end_time_input = (
            QLabel("End Time (e.g., 4:00 PM):"),
            QLineEdit(),
        )
        for widget in [self.label, self.end_time_input]:
            widget.setFont(QFont("Arial", 12))
            layout.addWidget(widget)

        style = "QLineEdit {padding: 8px; border: 2px solid #3498db; border-radius: 10px; background-color: #1C1C1C; color: white;}"
        self.end_time_input.setStyleSheet(style)

        self.start_button, self.stop_button = QPushButton("Start Script"), QPushButton(
            "Stop Script"
        )
        for btn, color in [
            (self.start_button, "#3498db"),
            (self.stop_button, "#e74c3c"),
        ]:
            btn.setFont(QFont("Arial", 12))
            btn.setStyleSheet(
                f"QPushButton {{padding: 10px; background-color: {color}; color: white; border-radius: 10px;}} QPushButton:hover {{background-color: {color[:-2]}80;}}"
            )
            layout.addWidget(btn)

        self.response_label = QLabel("")
        self.response_label.setFont(QFont("Arial", 11))
        layout.addWidget(self.response_label)

        self.start_button.clicked.connect(self.start_script)
        self.stop_button.clicked.connect(self.stop_script)

    def start_script(self):
        if not self.end_time_input.text():
            QMessageBox.warning(self, "Input Error", "Please enter a valid end time.")
            return
        self.thread = MouseMoverThread(self.end_time_input.text())
        self.thread.status_signal.connect(self.response_label.setText)
        self.thread.start()
        self.response_label.setText("Script started")

    def stop_script(self):
        if hasattr(self, "thread") and self.thread:
            self.thread.stop()
            self.thread = None
            self.response_label.setText("Script stopped")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MouseMoverApp()
    ex.show()
    sys.exit(app.exec_())
