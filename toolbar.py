from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtCore import Qt

class Toolbar(QWidget):
    def __init__(self, overlay):
        super().__init__()
        self.overlay = overlay
        self.drawing = False

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool
        )

        self.setGeometry(0, 0, 200, 50)
        self.setStyleSheet("background:#222;")

        self.btn = QPushButton("DRAW", self)
        self.btn.setGeometry(20, 10, 160, 30)
        self.btn.clicked.connect(self.toggle)

        self.show()

    def toggle(self):
        self.drawing = not self.drawing
        self.overlay.enable_drawing(self.drawing)
        self.btn.setText("DRAWING" if self.drawing else "NORMAL")
