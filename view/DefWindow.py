# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\DefWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(317, 624)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.GBDefInfo = QtWidgets.QGroupBox(self.centralwidget)
        self.GBDefInfo.setGeometry(QtCore.QRect(20, 10, 282, 566))
        self.GBDefInfo.setObjectName("GBDefInfo")
        self.formLayout = QtWidgets.QFormLayout(self.GBDefInfo)
        self.formLayout.setObjectName("formLayout")
        self.LDef = QtWidgets.QLabel(self.GBDefInfo)
        self.LDef.setObjectName("LDef")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.LDef)
        self.TEDef = QtWidgets.QTextEdit(self.GBDefInfo)
        self.TEDef.setObjectName("TEDef")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.TEDef)
        self.LRefs = QtWidgets.QLabel(self.GBDefInfo)
        self.LRefs.setObjectName("LRefs")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.LRefs)
        self.TWRefs = QtWidgets.QTableWidget(self.GBDefInfo)
        self.TWRefs.setObjectName("TWRefs")
        self.TWRefs.setColumnCount(2)
        self.TWRefs.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TWRefs.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWRefs.setHorizontalHeaderItem(1, item)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.TWRefs)
        self.CBUse = QtWidgets.QCheckBox(self.GBDefInfo)
        self.CBUse.setObjectName("CBUse")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.CBUse)
        self.LVal = QtWidgets.QLabel(self.GBDefInfo)
        self.LVal.setObjectName("LVal")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.LVal)
        self.LEVal = QtWidgets.QLineEdit(self.GBDefInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LEVal.sizePolicy().hasHeightForWidth())
        self.LEVal.setSizePolicy(sizePolicy)
        self.LEVal.setObjectName("LEVal")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.LEVal)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.BAccept = QtWidgets.QPushButton(self.GBDefInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BAccept.sizePolicy().hasHeightForWidth())
        self.BAccept.setSizePolicy(sizePolicy)
        self.BAccept.setObjectName("BAccept")
        self.gridLayout.addWidget(self.BAccept, 0, 0, 1, 1)
        self.BClose = QtWidgets.QPushButton(self.GBDefInfo)
        self.BClose.setObjectName("BClose")
        self.gridLayout.addWidget(self.BClose, 0, 1, 1, 1)
        self.formLayout.setLayout(8, QtWidgets.QFormLayout.SpanningRole, self.gridLayout)
        self.CBVal = QtWidgets.QComboBox(self.GBDefInfo)
        self.CBVal.setObjectName("CBVal")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.CBVal)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 317, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.GBDefInfo.setTitle(_translate("MainWindow", "Информация о понятии"))
        self.LDef.setText(_translate("MainWindow", "Определение:"))
        self.LRefs.setText(_translate("MainWindow", "Связи:"))
        item = self.TWRefs.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Определение"))
        item = self.TWRefs.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Тип связи"))
        self.CBUse.setText(_translate("MainWindow", "Использовать"))
        self.LVal.setText(_translate("MainWindow", "Значение:"))
        self.BAccept.setText(_translate("MainWindow", "Принять изменения"))
        self.BClose.setText(_translate("MainWindow", "Закрыть"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

