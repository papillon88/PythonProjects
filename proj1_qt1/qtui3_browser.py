# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtui3_browser.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_browser(object):
    def setupUi(self, browser):
        browser.setObjectName(_fromUtf8("browser"))
        browser.resize(534, 387)
        self.verticalLayout = QtGui.QVBoxLayout(browser)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.address = QtGui.QLineEdit(browser)
        self.address.setObjectName(_fromUtf8("address"))
        self.verticalLayout.addWidget(self.address)
        self.webview = QtWebKit.QWebView(browser)
        self.webview.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webview.setObjectName(_fromUtf8("webview"))
        self.verticalLayout.addWidget(self.webview)

        self.retranslateUi(browser)
        QtCore.QMetaObject.connectSlotsByName(browser)

    def retranslateUi(self, browser):
        browser.setWindowTitle(_translate("browser", "Browser", None))

from PyQt4 import QtWebKit
