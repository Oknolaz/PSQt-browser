import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWebEngineWidgets import * 
import design

class MainWindow(design.Ui_MainWindow, QtWidgets.QMainWindow, QtCore.QUrl):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tabWidget.removeTab(1)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.currentChanged.connect(self.setLineURL)
        self.tabWidget.tabCloseRequested.connect(self.closeTab)
        pageUrl = "https://searx.xyz/"
        self.progressBar.hide()
        self.webUrl.setText(pageUrl)
        self.l.clicked.connect(self.backBrowse)
        self.right.clicked.connect(self.nextBrowse)
        self.reload.clicked.connect(self.reloadPage)
        self.home.clicked.connect(self.goHome)
        self.webUrl.editingFinished.connect(self.changeUrl)
        self.newWindow.clicked.connect(self.addNewTab)
        self.addNewTab()
        self.show()
        
    def backBrowse(self):
        self.tabWidget.currentWidget().back()
    
    def nextBrowse(self):
        self.tabWidget.currentWidget().forward()
    
    def reloadPage(self):
        self.tabWidget.currentWidget().reload()
    
    def goHome(self):
        self.tabWidget.currentWidget().setUrl(QtCore.QUrl("https://searx.xyz"))
    
    def changeUrl(self):
        searchLine = self.webUrl.text()
        
        if searchLine == '' or searchLine == ' ':
            self.tabWidget.currentWidget().setUrl(QtCore.QUrl("https://searx.xyz"))
            
        elif " " in searchLine or "." not in searchLine:
            self.tabWidget.currentWidget().setUrl(QtCore.QUrl(f"https://searx.xyz/search?q={searchLine}&categories=general&language=en"))
        
        else:
            if "https://" not in searchLine and "http://" not in searchLine:
                self.tabWidget.currentWidget().setUrl(QtCore.QUrl(f"https://{searchLine}"))
            else:
                self.tabWidget.currentWidget().setUrl(QtCore.QUrl(searchLine))
    
    def setLineURL(self):
        pageUrl = str(self.tabWidget.currentWidget().url())
        pageUrl = pageUrl.replace('PyQt5.QtCore.QUrl', '').replace('(', '').replace("'", '').replace(")", '')
        self.webUrl.setText(pageUrl)
        
    def loadProgress(self):
        self.progressBar.show()
        self.tabWidget.currentWidget().loadProgress.connect(self.progressBar.setValue)
        self.tabWidget.currentWidget().loadFinished.connect(self.progressBar.hide)
        
    def addNewTab(self):
        browser = QWebEngineView()
        browser.setUrl(QtCore.QUrl("https://searx.xyz/"))
        title = browser.title()
        
        index = self.tabWidget.addTab(browser, title)
        self.tabWidget.setCurrentIndex(index)
        
        browser.urlChanged.connect(self.setLineURL)
        browser.loadStarted.connect(self.loadProgress)
        
    def closeTab(self, index):
        if self.tabWidget.count() == 1:
            exit()
        else:
            self.tabWidget.removeTab(index)
        

app = QtWidgets.QApplication(sys.argv)

my_mainWindow = MainWindow()
my_mainWindow.show()

sys.exit(app.exec_())
