from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys


class HelloWorld(QDialog):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        label = QLabel("Hello world")
        line_edit = QLineEdit()
        button = QPushButton("Close")

        layout.addWidget(label)
        layout.addWidget(line_edit)
        layout.addWidget(button)

        self.setLayout(layout)


app = QApplication(sys.argv)
dialog = HelloWorld()
dialog.show()
app.exec_()