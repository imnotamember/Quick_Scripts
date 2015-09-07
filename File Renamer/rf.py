# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rf.ui'
#
# Created: Sun Sep 06 13:12:25 2015
#      by: PyQt4 UI code generator 4.10.4
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
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(868, 531)
        Dialog.setAcceptDrops(True)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(False)
        self.FileTable = QtGui.QTableWidget(Dialog)
        self.FileTable.setGeometry(QtCore.QRect(10, 10, 681, 331))
        self.FileTable.setAcceptDrops(True)
        self.FileTable.setMidLineWidth(1)
        self.FileTable.setDragEnabled(True)
        self.FileTable.setDragDropMode(QtGui.QAbstractItemView.DropOnly)
        self.FileTable.setAlternatingRowColors(True)
        self.FileTable.setCornerButtonEnabled(False)
        self.FileTable.setColumnCount(4)
        self.FileTable.setObjectName(_fromUtf8("FileTable"))
        self.FileTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.FileTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.FileTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.FileTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.FileTable.setHorizontalHeaderItem(3, item)
        self.FileTable.horizontalHeader().setCascadingSectionResizes(True)
        self.FileTable.horizontalHeader().setDefaultSectionSize(169)
        self.FileTable.horizontalHeader().setSortIndicatorShown(False)
        self.FileTable.horizontalHeader().setStretchLastSection(True)
        self.FileTable.verticalHeader().setCascadingSectionResizes(True)
        self.FileTable.verticalHeader().setSortIndicatorShown(True)
        self.FileTable.verticalHeader().setStretchLastSection(False)
        self.OrderNum = QtGui.QPushButton(Dialog)
        self.OrderNum.setGeometry(QtCore.QRect(710, 190, 141, 23))
        self.OrderNum.setObjectName(_fromUtf8("OrderNum"))
        self.Deploy = QtGui.QPushButton(Dialog)
        self.Deploy.setGeometry(QtCore.QRect(710, 320, 141, 23))
        self.Deploy.setObjectName(_fromUtf8("Deploy"))
        self.SaveText = QtGui.QLineEdit(Dialog)
        self.SaveText.setGeometry(QtCore.QRect(710, 260, 141, 20))
        self.SaveText.setObjectName(_fromUtf8("SaveText"))
        self.SaveBrowse = QtGui.QPushButton(Dialog)
        self.SaveBrowse.setGeometry(QtCore.QRect(710, 290, 141, 23))
        self.SaveBrowse.setObjectName(_fromUtf8("SaveBrowse"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(710, 240, 141, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(710, 10, 141, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.OpenText = QtGui.QLineEdit(Dialog)
        self.OpenText.setGeometry(QtCore.QRect(710, 30, 141, 20))
        self.OpenText.setMouseTracking(False)
        self.OpenText.setStyleSheet(_fromUtf8("color: rgb(0, 170, 0);\n"
"alternate-background-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(0, 0, 0);\n"
"selection-color: rgb(0, 170, 0);\n"
"background-color: rgb(0, 0, 0);"))
        self.OpenText.setDragEnabled(True)
        self.OpenText.setObjectName(_fromUtf8("OpenText"))
        self.OpenBrowse = QtGui.QPushButton(Dialog)
        self.OpenBrowse.setGeometry(QtCore.QRect(710, 60, 141, 23))
        self.OpenBrowse.setFlat(False)
        self.OpenBrowse.setObjectName(_fromUtf8("OpenBrowse"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(710, 110, 141, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(710, 90, 141, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(710, 220, 141, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.Console = QtGui.QTextEdit(Dialog)
        self.Console.setGeometry(QtCore.QRect(10, 350, 851, 171))
        self.Console.setAcceptDrops(False)
        self.Console.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 170, 0);"))
        self.Console.setFrameShape(QtGui.QFrame.StyledPanel)
        self.Console.setLineWidth(2)
        self.Console.setMidLineWidth(-2)
        self.Console.setUndoRedoEnabled(False)
        self.Console.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.Console.setReadOnly(True)
        self.Console.setAcceptRichText(False)
        self.Console.setObjectName(_fromUtf8("Console"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(710, 130, 31, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(710, 160, 31, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.Prefix = QtGui.QLineEdit(Dialog)
        self.Prefix.setGeometry(QtCore.QRect(750, 130, 101, 20))
        self.Prefix.setObjectName(_fromUtf8("Prefix"))
        self.Suffix = QtGui.QLineEdit(Dialog)
        self.Suffix.setGeometry(QtCore.QRect(750, 160, 101, 20))
        self.Suffix.setObjectName(_fromUtf8("Suffix"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.FileTable, self.OpenText)
        Dialog.setTabOrder(self.OpenText, self.OpenBrowse)
        Dialog.setTabOrder(self.OpenBrowse, self.OrderNum)
        Dialog.setTabOrder(self.OrderNum, self.SaveText)
        Dialog.setTabOrder(self.SaveText, self.SaveBrowse)
        Dialog.setTabOrder(self.SaveBrowse, self.Deploy)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("File Renamer", "File Renamer", None))
        self.FileTable.setSortingEnabled(False)
        item = self.FileTable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Original Folder", None))
        item = self.FileTable.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Original Filename", None))
        item = self.FileTable.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "New Folder", None))
        item = self.FileTable.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "New Filename", None))
        self.OrderNum.setText(_translate("Dialog", "Apply New Labels", None))
        self.Deploy.setText(_translate("Dialog", "Deploy", None))
        self.SaveText.setText(_translate("Dialog", "C:\\", None))
        self.SaveBrowse.setText(_translate("Dialog", "Browse", None))
        self.label.setText(_translate("Dialog", "Location for new files:", None))
        self.label_2.setText(_translate("Dialog", "Location of files to rename:", None))
        self.OpenText.setText(_translate("Dialog", "C:\\", None))
        self.OpenBrowse.setText(_translate("Dialog", "Browse", None))
        self.label_3.setText(_translate("Dialog", "New Labels:", None))
        self.label_4.setText(_translate("Dialog", "Prefix:", None))
        self.label_5.setText(_translate("Dialog", "Suffix:", None))

