from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import time
from qtui2 import Ui_Dialog as MainLogin
from qtui3_browser import Ui_browser as Browser


class MainApp(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        self.master_url = ""
        self.main_login = MainLogin()
        self.main_login.setupUi(self)
        self.main_login.facebook.clicked.connect(self.set_fb_url)
        self.main_login.twitter.clicked.connect(self.set_tw_url)
        self.main_login.google.clicked.connect(self.set_gp_url)
        self.main_login.login.clicked.connect(self.open_in_browser)

        self.browser_window = Browser()
        # self.browser_window.setupUi(self)
        # self.browser_window.address.returnPressed.connect(self.load_url)

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

        self.main_login.progress.setContextMenuPolicy(Qt.CustomContextMenu)
        self.main_login.progress.customContextMenuRequested.connect(self.show_context_menu)

    def show_context_menu(self, position):
        menu = QMenu(self)
        reset_ac = QAction("Reset", self)
        menu.addActions([reset_ac])
        reset_ac.triggered.connect(self.main_login.progress.reset)
        menu.popup(self.main_login.progress.mapToGlobal(position))

    def load_url(self):
        url = self.browser_window.address.text()
        self.browser_window.webview.load(QUrl(url))
        self.browser_window.webview.show()

    def set_fb_url(self):
        self.master_url = "http://www.facebook.com"
        # print(self.master_url)

    def set_tw_url(self):
        self.master_url = "https://twitter.com/"
        # print(self.master_url)

    def set_gp_url(self):
        self.master_url = "https://plus.google.com/"
        # print(self.master_url)

    def open_in_browser(self):
        time.sleep(2)
        # authentication required here
        # if successful, then
        #self.main_login
        self.browser_window.setupUi(QObject)
        # else error
        # print(self.master_url)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = MainApp()

    splash_image = QPixmap(".\other_icons\welcome.jpg")
    splash = QSplashScreen(splash_image)
    splash.show()
    time.sleep(2)
    dialog.show()
    splash.finish(dialog)
    app.exec_()