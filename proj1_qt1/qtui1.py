# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtui1.ui'
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

class Ui_downloader(object):
    def setupUi(self, downloader):
        downloader.setObjectName(_fromUtf8("downloader"))
        downloader.resize(151, 149)
        downloader.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.verticalLayout = QtGui.QVBoxLayout(downloader)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.url = QtGui.QLineEdit(downloader)
        self.url.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.url.setObjectName(_fromUtf8("url"))
        self.verticalLayout.addWidget(self.url)
        self.location = QtGui.QLineEdit(downloader)
        self.location.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.location.setObjectName(_fromUtf8("location"))
        self.verticalLayout.addWidget(self.location)
        self.browse = QtGui.QPushButton(downloader)
        self.browse.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.browse.setObjectName(_fromUtf8("browse"))
        self.verticalLayout.addWidget(self.browse)
        self.progress = QtGui.QProgressBar(downloader)
        self.progress.setProperty("value", 0)
        self.progress.setAlignment(QtCore.Qt.AlignCenter)
        self.progress.setObjectName(_fromUtf8("progress"))
        self.verticalLayout.addWidget(self.progress)
        self.download = QtGui.QPushButton(downloader)
        self.download.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.download.setObjectName(_fromUtf8("download"))
        self.verticalLayout.addWidget(self.download)

        self.retranslateUi(downloader)
        QtCore.QMetaObject.connectSlotsByName(downloader)

    def retranslateUi(self, downloader):
        downloader.setWindowTitle(_translate("downloader", "Downloader", None))
        self.url.setPlaceholderText(_translate("downloader", "URL", None))
        self.location.setPlaceholderText(_translate("downloader", "File save location", None))
        self.browse.setText(_translate("downloader", "Browse", None))
        self.download.setText(_translate("downloader", "Download", None))

