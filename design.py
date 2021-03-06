# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(871, 696)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.l = QtWidgets.QPushButton(self.centralwidget)
        self.l.setText("")
        icon = QtGui.QIcon.fromTheme("back")
        self.l.setIcon(icon)
        self.l.setObjectName("l")
        self.horizontalLayout.addWidget(self.l)
        self.right = QtWidgets.QPushButton(self.centralwidget)
        self.right.setText("")
        icon = QtGui.QIcon.fromTheme("next")
        self.right.setIcon(icon)
        self.right.setObjectName("right")
        self.horizontalLayout.addWidget(self.right)
        self.reload = QtWidgets.QPushButton(self.centralwidget)
        self.reload.setText("")
        icon = QtGui.QIcon.fromTheme("reload")
        self.reload.setIcon(icon)
        self.reload.setObjectName("reload")
        self.horizontalLayout.addWidget(self.reload)
        self.home = QtWidgets.QPushButton(self.centralwidget)
        self.home.setText("")
        icon = QtGui.QIcon.fromTheme("user-home")
        self.home.setIcon(icon)
        self.home.setObjectName("home")
        self.horizontalLayout.addWidget(self.home)
        self.newWindow = QtWidgets.QPushButton(self.centralwidget)
        self.newWindow.setText("")
        icon = QtGui.QIcon.fromTheme("add")
        self.newWindow.setIcon(icon)
        self.newWindow.setObjectName("newWindow")
        self.horizontalLayout.addWidget(self.newWindow)
        self.webUrl = QtWidgets.QLineEdit(self.centralwidget)
        self.webUrl.setClearButtonEnabled(True)
        self.webUrl.setObjectName("webUrl")
        self.horizontalLayout.addWidget(self.webUrl)
        self.settings = QtWidgets.QPushButton(self.centralwidget)
        self.settings.setText("")
        icon = QtGui.QIcon.fromTheme("settings")
        self.settings.setIcon(icon)
        self.settings.setObjectName("settings")
        self.horizontalLayout.addWidget(self.settings)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.verticalLayout.addWidget(self.tabWidget)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setCursor(QtGui.QCursor(QtCore.Qt.BusyCursor))
        self.progressBar.setLocale(QtCore.QLocale(QtCore.QLocale.C, QtCore.QLocale.AnyCountry))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.about = QtWidgets.QAction(MainWindow)
        self.about.setObjectName("about")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PSQt Browser"))
        self.l.setToolTip(_translate("MainWindow", "<html><head/><body><p>Back page</p></body></html>"))
        self.right.setToolTip(_translate("MainWindow", "<html><head/><body><p>Forward page</p></body></html>"))
        self.reload.setToolTip(_translate("MainWindow", "<html><head/><body><p>Reload page</p></body></html>"))
        self.home.setToolTip(_translate("MainWindow", "<html><head/><body><p>Home</p></body></html>"))
        self.newWindow.setToolTip(_translate("MainWindow", "<html><head/><body><p>Forward page</p></body></html>"))
        self.settings.setToolTip(_translate("MainWindow", "<html><head/><body><p>Settings</p></body></html>"))
        self.about.setText(_translate("MainWindow", "About PSQt Browser"))
from PyQt5 import QtWebEngineWidgets
