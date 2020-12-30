import sys
from PyQt5 import QtWidgets, QtCore
import design

class MainWindow(design.Ui_MainWindow, QtWidgets.QMainWindow, QtCore.QUrl):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        pageUrl = str(self.webView.url())
        pageUrl = pageUrl.replace('PyQt5.QtCore.QUrl', '').replace('(', '').replace("'", '').replace(")", '')
        self.webView.setFocus()
        self.progressBar.hide()
        self.webUrl.setText(pageUrl)
        self.l.clicked.connect(self.backBrowse)
        self.right.clicked.connect(self.nextBrowse)
        self.reload.clicked.connect(self.reloadPage)
        self.home.clicked.connect(self.goHome)
        self.webUrl.editingFinished.connect(self.changeUrl)
        self.webView.urlChanged.connect(self.setLineURL)
        self.webView.loadStarted.connect(self.loadProgress)
        self.newWindow.clicked.connect(self.openNewWindow)
        self.webView.settings().PluginsEnabled = True
        self.webView.settings().FullScreenSupportEnabled = True
        self.nw1 = NewWindow()
        self.nw2 = NewWindow()
        self.nw3 = NewWindow()
        self.nw4 = NewWindow()
        self.nw5 = NewWindow()
        self.nw6 = NewWindow()
        

    def backBrowse(self):
        self.webView.back()
    
    def nextBrowse(self):
        self.webView.forward()
    
    def reloadPage(self):
        self.webView.reload()
    
    def goHome(self):
        self.webView.setUrl(QtCore.QUrl("https://searx.xyz"))
    
    def changeUrl(self):
        searchLine = self.webUrl.text()
        if searchLine == '' or searchLine == ' ':
            self.webView.setUrl(QtCore.QUrl("https://searx.xyz"))
        elif " " in searchLine or "." not in searchLine:
            self.webView.setUrl(QtCore.QUrl(f"https://searx.xyz/search?q={searchLine}&categories=general&language=en"))
        else:
            if "https://" not in searchLine and "http://" not in searchLine:
                self.webView.setUrl(QtCore.QUrl(f"https://{searchLine}"))
            else:
                self.webView.setUrl(QtCore.QUrl(searchLine))
    
    def setLineURL(self):
        pageUrl = str(self.webView.url())
        pageUrl = pageUrl.replace('PyQt5.QtCore.QUrl', '').replace('(', '').replace("'", '').replace(")", '')
        self.webUrl.setText(pageUrl)
        
    def loadProgress(self):
        self.progressBar.show()
        self.webView.loadProgress.connect(self.progressBar.setValue)
        self.webView.loadFinished.connect(self.progressBar.hide)
        
    def openNewWindow(self):
        if self.nw1.isVisible():
            self.nw2.show()
        elif self.nw2.isVisible():
            self.nw3.show()
        elif self.nw3.isVisible():
            self.nw4.show()
        elif self.nw4.isVisible():
            self.nw5.show()
        elif self.nw5.isVisible():
            self.nw6.show()
        else:
            self.nw1.show()

        
class NewWindow(design.Ui_MainWindow, QtWidgets.QMainWindow, QtCore.QUrl):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        pageUrl = str(self.webView.url())
        pageUrl = pageUrl.replace('PyQt5.QtCore.QUrl', '').replace('(', '').replace("'", '').replace(")", '')
        self.webView.setFocus()
        self.progressBar.hide()
        self.webUrl.setText(pageUrl)
        self.l.clicked.connect(self.backBrowse)
        self.right.clicked.connect(self.nextBrowse)
        self.reload.clicked.connect(self.reloadPage)
        self.home.clicked.connect(self.goHome)
        self.webUrl.editingFinished.connect(self.changeUrl)
        self.webView.urlChanged.connect(self.setLineURL)
        self.webView.loadStarted.connect(self.loadProgress)
        self.newWindow.hide()
        self.webView.settings().PluginsEnabled = True
        self.webView.settings().FullScreenSupportEnabled = True
        

    def backBrowse(self):
        self.webView.back()
    
    def nextBrowse(self):
        self.webView.forward()
    
    def reloadPage(self):
        self.webView.reload()
    
    def goHome(self):
        self.webView.setUrl(QtCore.QUrl("https://searx.xyz"))
    
    def changeUrl(self):
        searchLine = self.webUrl.text()
        if searchLine == '' or searchLine == ' ':
            self.webView.setUrl(QtCore.QUrl("https://searx.xyz"))
        elif " " in searchLine or "." not in searchLine:
            self.webView.setUrl(QtCore.QUrl(f"https://searx.xyz/search?q={searchLine}&categories=general&language=en"))
        else:
            if "https://" not in searchLine and "http://" not in searchLine:
                self.webView.setUrl(QtCore.QUrl(f"https://{searchLine}"))
            else:
                self.webView.setUrl(QtCore.QUrl(searchLine))
    
    def setLineURL(self):
        pageUrl = str(self.webView.url())
        pageUrl = pageUrl.replace('PyQt5.QtCore.QUrl', '').replace('(', '').replace("'", '').replace(")", '')
        self.webUrl.setText(pageUrl)
        
    def loadProgress(self):
        self.progressBar.show()
        self.webView.loadProgress.connect(self.progressBar.setValue)
        self.webView.loadFinished.connect(self.progressBar.hide)
        

app = QtWidgets.QApplication(sys.argv)

my_mainWindow = MainWindow()
my_mainWindow.show()

sys.exit(app.exec_())
