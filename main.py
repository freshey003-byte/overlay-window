import sys
from PyQt5.QtWidgets import QApplication
from overlay import Overlay
from toolbar import Toolbar

app = QApplication(sys.argv)

overlay = Overlay()
toolbar = Toolbar(overlay)

sys.exit(app.exec_())
