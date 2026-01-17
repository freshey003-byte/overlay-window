from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen

class Overlay(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool
        )

        self.setAttribute(Qt.WA_TranslucentBackground)

        self.drawing = False
        self.last_point = None
        self.lines = []

        screen = QApplication.primaryScreen().geometry()
        toolbar_height = 60

        self.setGeometry(
            screen.x(),
            screen.y() + toolbar_height,
            screen.width(),
            screen.height() - toolbar_height
        )

        self.show()

    def enable_drawing(self, enable: bool):
        self.drawing = enable
        if enable:
            self.show()
        else:
            self.hide()
        self.last_point = None
        self.lines = []

    def mousePressEvent(self, event):
        print("PRESS at", event.pos())
        if self.drawing:
            self.last_point = event.pos()

    def mouseMoveEvent(self, event):
        print("MOVE at", event.pos())
        if self.drawing and self.last_point:
            self.lines.append((self.last_point, event.pos()))
            self.last_point = event.pos()
            self.update()

    def paintEvent(self, event):
        from PyQt5.QtGui import QColor
        painter = QPainter(self)
     
        painter.fillRect(self.rect(), QColor(0, 0, 0, 20))
        
        pen = QPen(Qt.red, 3)
        painter.setPen(pen)
        for p1, p2 in self.lines:
            painter.drawLine(p1, p2)
