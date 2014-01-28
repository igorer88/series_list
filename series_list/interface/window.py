# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created: Tue Jan 14 19:20:04 2014
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuSeries_list = QtGui.QMenu(self.menubar)
        self.menuSeries_list.setObjectName(_fromUtf8("menuSeries_list"))
        MainWindow.setMenuBar(self.menubar)
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionOpenDownloads = QtGui.QAction(MainWindow)
        self.actionOpenDownloads.setObjectName(_fromUtf8("actionOpenDownloads"))
        self.menuSeries_list.addAction(self.actionSettings)
        self.menuSeries_list.addAction(self.actionOpenDownloads)
        self.menuSeries_list.addAction(self.actionExit)
        self.menubar.addAction(self.menuSeries_list.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menuSeries_list.setTitle(_translate("MainWindow", "Series List", None))
        self.actionSettings.setText(_translate("MainWindow", "Settings", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionOpenDownloads.setText(_translate("MainWindow", "Open downloads path", None))


if __name__ == "__main__":
    # Obtaning the system local settings
    local = unicode(QtCore.QLocale.system().name())
    import sys
    app = QtGui.QApplication(sys.argv)
    #Aplying the translations made with Qt Linguist.
    traductor = QtCore.QTranslator()
    traductor.load(os.path.join(os.path.abspath(os.path.dirname(__file__)),"window_" + local))
    aplicacion.installTranslator(traductor)
    
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

