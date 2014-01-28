# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'series_entry.ui'
#
# Created: Wed Jan 15 19:16:56 2014
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

class Ui_SeriesEntry(object):
    def setupUi(self, SeriesEntry):
        SeriesEntry.setObjectName(_fromUtf8("SeriesEntry"))
        SeriesEntry.resize(319, 87)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SeriesEntry.sizePolicy().hasHeightForWidth())
        SeriesEntry.setSizePolicy(sizePolicy)
        SeriesEntry.setMinimumSize(QtCore.QSize(0, 0))
        SeriesEntry.setMaximumSize(QtCore.QSize(16777215, 87))
        self.horizontalLayout = QtGui.QHBoxLayout(SeriesEntry)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.poster = QtGui.QLabel(SeriesEntry)
        self.poster.setObjectName(_fromUtf8("poster"))
        self.horizontalLayout.addWidget(self.poster)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.title = QtGui.QLabel(SeriesEntry)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        self.title.setScaledContents(False)
        self.title.setWordWrap(True)
        self.title.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.title.setObjectName(_fromUtf8("title"))
        self.horizontalLayout_2.addWidget(self.title)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.download = QtGui.QPushButton(SeriesEntry)
        self.download.setText(_fromUtf8(""))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("application-x-bittorrent"))
        self.download.setIcon(icon)
        self.download.setIconSize(QtCore.QSize(24, 24))
        self.download.setFlat(False)
        self.download.setObjectName(_fromUtf8("download"))
        self.horizontalLayout_2.addWidget(self.download)
        self.openButton = QtGui.QPushButton(SeriesEntry)
        self.openButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("media-playback-start"))
        self.openButton.setIcon(icon)
        self.openButton.setIconSize(QtCore.QSize(24, 24))
        self.openButton.setObjectName(_fromUtf8("openButton"))
        self.horizontalLayout_2.addWidget(self.openButton)
        self.pauseButton = QtGui.QPushButton(SeriesEntry)
        self.pauseButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("media-playback-pause"))
        self.pauseButton.setIcon(icon)
        self.pauseButton.setIconSize(QtCore.QSize(24, 24))
        self.pauseButton.setCheckable(True)
        self.pauseButton.setChecked(False)
        self.pauseButton.setObjectName(_fromUtf8("pauseButton"))
        self.horizontalLayout_2.addWidget(self.pauseButton)
        self.stopButton = QtGui.QPushButton(SeriesEntry)
        self.stopButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("process-stop"))
        self.stopButton.setIcon(icon)
        self.stopButton.setIconSize(QtCore.QSize(24, 24))
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.horizontalLayout_2.addWidget(self.stopButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.progress = QtGui.QProgressBar(SeriesEntry)
        self.progress.setProperty("value", 0)
        self.progress.setObjectName(_fromUtf8("progress"))
        self.verticalLayout.addWidget(self.progress)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(SeriesEntry)
        QtCore.QMetaObject.connectSlotsByName(SeriesEntry)

    def retranslateUi(self, SeriesEntry):
        SeriesEntry.setWindowTitle(_translate("SeriesEntry", "Form", None))
        self.poster.setText(_translate("SeriesEntry", "Poster", None))
        self.title.setText(_translate("SeriesEntry", "Title", None))
        self.download.setToolTip(_translate("SeriesEntry", "Download video and subtitle", None))
        self.openButton.setToolTip(_translate("SeriesEntry", "Play downloaded video", None))
        self.pauseButton.setToolTip(_translate("SeriesEntry", "Pause or resume downloading", None))
        self.stopButton.setToolTip(_translate("SeriesEntry", "Remove all downloaded content", None))


if __name__ == "__main__":
    # Obtaning the system local settings
    local = unicode(QtCore.QLocale.system().name())
    import sys
    app = QtGui.QApplication(sys.argv)
    #Aplying the translations made with Qt Linguist.
    traductor = QtCore.QTranslator()
    traductor.load(os.path.join(os.path.abspath(os.path.dirname(__file__)),"series_entry_" + local))
    aplicacion.installTranslator(traductor)

    app = QtGui.QApplication(sys.argv)
    SeriesEntry = QtGui.QWidget()
    ui = Ui_SeriesEntry()
    ui.setupUi(SeriesEntry)
    SeriesEntry.show()
    sys.exit(app.exec_())

