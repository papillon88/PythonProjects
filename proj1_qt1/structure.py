from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys


class HelloWorld(QDialog):
    def __init__(self):
        super().__init__()
        # self.layout = QHBoxLayout()
        # self.layout = QVBoxLayout()
        self.layout = QGridLayout()

        self.label = QLabel("Hello world")
        self.line_edit = QLineEdit()
        self.button = QPushButton("Close")

        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.line_edit, 0, 1)
        self.layout.addWidget(self.button, 1, 1)

        self.setLayout(self.layout)

        self.button.clicked.connect(self.close)
        self.line_edit.textChanged.connect(self.change_text_label)

    def change_text_label(self, text):
        self.label.setText(text)


app = QApplication(sys.argv)
dialog = HelloWorld()
dialog.show()
app.exec_()