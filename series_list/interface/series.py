# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'series.ui'
#
# Created: Wed Jan 15 19:20:45 2014
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.scrollArea = QtGui.QScrollArea(Form)
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.seriesContainer = QtGui.QWidget()
        self.seriesContainer.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.seriesContainer.setObjectName(_fromUtf8("seriesContainer"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.seriesContainer)
        self.verticalLayout_3.setContentsMargins(0, 0, 9, 0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.loading = QtGui.QLabel(self.seriesContainer)
        self.loading.setAlignment(QtCore.Qt.AlignCenter)
        self.loading.setObjectName(_fromUtf8("loading"))
        self.verticalLayout_3.addWidget(self.loading)
        self.nothingFound = QtGui.QLabel(self.seriesContainer)
        self.nothingFound.setAlignment(QtCore.Qt.AlignCenter)
        self.nothingFound.setObjectName(_fromUtf8("nothingFound"))
        self.verticalLayout_3.addWidget(self.nothingFound)
        self.somethingWrong = QtGui.QLabel(self.seriesContainer)
        self.somethingWrong.setAlignment(QtCore.Qt.AlignCenter)
        self.somethingWrong.setObjectName(_fromUtf8("somethingWrong"))
        self.verticalLayout_3.addWidget(self.somethingWrong)
        self.scrollArea.setWidget(self.seriesContainer)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.loading.setText(_translate("Form", "Loading...", None))
        self.nothingFound.setText(_translate("Form", "Series not found", None))
        self.somethingWrong.setText(_translate("Form", "Somthing going wrong", None))


if __name__ == "__main__":
    # Obtaning the system local settings
    local = unicode(QtCore.QLocale.system().name())
    import sys
    app = QtGui.QApplication(sys.argv)
    #Aplying the translations made with Qt Linguist.
    traductor = QtCore.QTranslator()
    traductor.load(os.path.join(os.path.abspath(os.path.dirname(__file__)),"series_" + local))
    aplicacion.installTranslator(traductor)

    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

