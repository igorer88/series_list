# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filter.ui'
#
# Created: Wed Jan 15 19:22:14 2014
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

class Ui_Filter(object):
    def setupUi(self, Filter):
        Filter.setObjectName(_fromUtf8("Filter"))
        Filter.resize(191, 45)
        Filter.setMaximumSize(QtCore.QSize(16777215, 45))
        self.horizontalLayout = QtGui.QHBoxLayout(Filter)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.filterEdit = QtGui.QLineEdit(Filter)
        self.filterEdit.setObjectName(_fromUtf8("filterEdit"))
        self.horizontalLayout.addWidget(self.filterEdit)
        self.filterButton = QtGui.QPushButton(Filter)
        self.filterButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("view-refresh"))
        self.filterButton.setIcon(icon)
        self.filterButton.setObjectName(_fromUtf8("filterButton"))
        self.horizontalLayout.addWidget(self.filterButton)

        self.retranslateUi(Filter)
        QtCore.QMetaObject.connectSlotsByName(Filter)

    def retranslateUi(self, Filter):
        Filter.setWindowTitle(_translate("Filter", "Form", None))
        self.filterEdit.setPlaceholderText(_translate("Filter", "Enter search text here", None))
        self.filterButton.setToolTip(_translate("Filter", "Refresh results", None))


if __name__ == "__main__":
    # Obtaning the system local settings
    local = unicode(QtCore.QLocale.system().name())
    import sys
    app = QtGui.QApplication(sys.argv)
    #Aplying the translations made with Qt Linguist.
    traductor = QtCore.QTranslator()
    traductor.load(os.path.join(os.path.abspath(os.path.dirname(__file__)),"filter_" + local))
    aplicacion.installTranslator(traductor)

    app = QtGui.QApplication(sys.argv)
    Filter = QtGui.QWidget()
    ui = Ui_Filter()
    ui.setupUi(Filter)
    Filter.show()
    sys.exit(app.exec_())

