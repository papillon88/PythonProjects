from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import time
import qtui2


class MainApp(QDialog, qtui2.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        self.sys_tray_icon = QIcon(".\other_icons\py.png")
        self.sys_tray = QSystemTrayIcon(self.sys_tray_icon, self)
        self.menu = QMenu()
        self.restore_ac = QAction("Restore", self)
        self.close_ac = QAction("Close", self)
        self.menu.addActions([self.restore_ac, self.close_ac])
        self.sys_tray.setContextMenu(self.menu)
        self.sys_tray.show()
        self.sys_tray.showMessage("Booting", "Starting app now", QSystemTrayIcon.Information)
        self.close_ac.triggered.connect(self.close)

        self.progress.setContextMenuPolicy(Qt.CustomContextMenu)
        self.progress.customContextMenuRequested.connect(self.show_context_menu)

    def show_context_menu(self, position):
        menu = QMenu(self)
        reset_ac = QAction("Reset", self)
        menu.addActions([reset_ac])
        reset_ac.triggered.connect(self.progress.reset)
        menu.popup(self.progress.mapToGlobal(position))

app = QApplication(sys.argv)
dialog = MainApp()

splash_image = QPixmap(".\other_icons\welcome.jpg")
splash = QSplashScreen(splash_image)
splash.show()
time.sleep(2)
dialog.show()
splash.finish(dialog)
app.exec_()