from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import urllib.request as ur


class Downloader(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Downloader")
        self.setFocus()

        self.layout = QVBoxLayout()

        self.url = QLineEdit()
        self.url.setPlaceholderText("URL")

        self.location = QLineEdit()
        self.location.setPlaceholderText("Save Location")
        self.browse = QPushButton("Browse")

        self.progress = QProgressBar()
        self.progress.setValue(0)
        self.progress.setAlignment(Qt.AlignHCenter)

        self.button = QPushButton("Download")

        self.layout.addWidget(self.url)
        self.layout.addWidget(self.location)
        self.layout.addWidget(self.browse)
        self.layout.addWidget(self.progress)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.download)
        self.browse.clicked.connect(self.browse_func)

    def download(self):
        url_str = self.url.text()
        loc_str = self.location.text()
        try:
            ur.urlretrieve(url_str, loc_str, self.report)
        except:
            QMessageBox.warning(self, "Warning", "Cannot fetch URL")
            self.progress.setValue(0)
            self.url.setText("")
            self.location.setText("")
        else:
            QMessageBox.information(self, "Information", "The download is complete")
            self.progress.setValue(0)
            self.url.setText("")
            self.location.setText("")

    def report(self, block_num, block_size, total_size):
        read_so_far = block_num * block_size
        if total_size > 0:
            percent = read_so_far * 100 / total_size
            if percent > 100:
                self.progress.setValue(100)
            else:
                self.progress.setValue(int(percent))

    def browse_func(self):
        save_file = QFileDialog.getSaveFileName(self,
                                                caption = "Save File As",
                                                directory = ".",
                                                filter = "All Files(*.*)")
        self.location.setText(QDir.toNativeSeparators(save_file))

app = QApplication(sys.argv)
dialog = Downloader()
dialog.show()
app.exec_()