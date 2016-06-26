from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import urllib.request as ur
import qtui1


class Downloader(QDialog, qtui1.Ui_downloader):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        self.url.setText("www.google.com")
        self.progress.setValue(50)


app = QApplication(sys.argv)
dialog = Downloader()
dialog.show()
app.exec_()