# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created: Wed Jan 15 18:57:37 2014
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 334)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.downloadsPathLabel = QtGui.QLabel(Dialog)
        self.downloadsPathLabel.setObjectName(_fromUtf8("downloadsPathLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.downloadsPathLabel)
        self.changeDownloadsPath = QtGui.QPushButton(Dialog)
        self.changeDownloadsPath.setObjectName(_fromUtf8("changeDownloadsPath"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.changeDownloadsPath)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.seriesTimeout = QtGui.QSpinBox(Dialog)
        self.seriesTimeout.setMaximum(1000)
        self.seriesTimeout.setObjectName(_fromUtf8("seriesTimeout"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.seriesTimeout)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.subtitlesTimeout = QtGui.QSpinBox(Dialog)
        self.subtitlesTimeout.setMaximum(1000)
        self.subtitlesTimeout.setObjectName(_fromUtf8("subtitlesTimeout"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.subtitlesTimeout)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.posterTimeout = QtGui.QSpinBox(Dialog)
        self.posterTimeout.setMaximum(1000)
        self.posterTimeout.setObjectName(_fromUtf8("posterTimeout"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.posterTimeout)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_5)
        self.seriesProviders = QtGui.QComboBox(Dialog)
        self.seriesProviders.setObjectName(_fromUtf8("seriesProviders"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.seriesProviders)
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_6)
        self.subtitlesProviders = QtGui.QComboBox(Dialog)
        self.subtitlesProviders.setObjectName(_fromUtf8("subtitlesProviders"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.subtitlesProviders)
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_7)
        self.postersProviders = QtGui.QComboBox(Dialog)
        self.postersProviders.setObjectName(_fromUtf8("postersProviders"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.postersProviders)
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_8)
        self.previewPercent = QtGui.QSpinBox(Dialog)
        self.previewPercent.setMinimum(1)
        self.previewPercent.setMaximum(100)
        self.previewPercent.setObjectName(_fromUtf8("previewPercent"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.previewPercent)
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.label_9)
        self.retryCount = QtGui.QSpinBox(Dialog)
        self.retryCount.setMinimum(1)
        self.retryCount.setMaximum(10)
        self.retryCount.setObjectName(_fromUtf8("retryCount"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.retryCount)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Settings", None))
        self.downloadsPathLabel.setText(_translate("Dialog", "Downloads path", None))
        self.changeDownloadsPath.setText(_translate("Dialog", "Change", None))
        self.label.setText(_translate("Dialog", "Series loading timeout", None))
        self.label_2.setText(_translate("Dialog", "Subtitles timeout", None))
        self.label_3.setText(_translate("Dialog", "Poster timeout", None))
        self.label_4.setText(_translate("Dialog", "0 = without timeout", None))
        self.label_5.setText(_translate("Dialog", "Series provider", None))
        self.label_6.setText(_translate("Dialog", "Subtitles provider", None))
        self.label_7.setText(_translate("Dialog", "Posters provider", None))
        self.label_8.setText(_translate("Dialog", "Play available after %", None))
        self.label_9.setText(_translate("Dialog", "Max retry count", None))


if __name__ == "__main__":
        # Obtaning the system local settings
    local = unicode(QtCore.QLocale.system().name())
    import sys
    app = QtGui.QApplication(sys.argv)
    #Aplying the translations made with Qt Linguist.
    traductor = QtCore.QTranslator()
    traductor.load(os.path.join(os.path.abspath(os.path.dirname(__file__)),"settings_" + local))
    aplicacion.installTranslator(traductor)

    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

