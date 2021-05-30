# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\DefWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from model.enums.ViewType import ViewType
from model.enums.Defins import Defins


definDict = {
    Defins.NORMALIZATION: '«Нормализация текста» - уменьшение размерности текста '
                          'при помощи уменьшения его разреженности.',
    Defins.VECTORIZATION: '«Векторизация текста» - представление текста в виде вектора критериев'
                          ' для использования в алгоритмах кластеризации.',
    Defins.PREPMETH: '«Метод предобработки текста перед кластеризацией» – набор действий над текстом, его обработки,'
                     ' чтобы его можно было применить в одном из алгоритмов кластеризации.'
                     'К этим методам относится нормализация и векторизация текстов.',
    Defins.REDUCEDIM: '«Снижение размерности» - уменьшение количества различных токенов.\n'
                      '«Размерность текста» - количество токенов в тексте.\n'
                      '«Разреженность текста» - разреженность матрицы токенов данного текста. '
                      'Возникает в некоторых моделях из-за того, что матрица строится по всем токенам корпуса.',
    Defins.PREP: '«Предобработка текстов» - векторизация текстов и снижение размерности этих векторов с помощью '
                 'методов предобработки',
    Defins.CLUST: '«Задача кластеризации корпуса текстов» - это разбиение корпуса текстов на кластеры.\n'
                  '«Кластеры текстов» - подмножества тематически близких документов из исходного корпуса текстов.',
    Defins.FILTER: '«Фильтрация токенов» - использование следующих методов: удаление токенов по частоте,'
                   ' удаление стоп-слов, выбор наиболее частых слов, исключение пунктуации',
    Defins.LEM: '«Лемматизация» - использование словаря для просмотра каждого токена, и возвращения начальной формы '
                'слова, называемой леммой, в словарь.',
    Defins.STEM: '«Стемминг» - использование набора правил (или моделей) для разбиения строки на меньшие подстроки,'
                ' с целью удаления приставок и суффиксов слов, которые изменяют значение.',
    Defins.TOKEN: '«Токен» - самостоятельная единица текста, в используемых моделях это обозначение используется для'
                  ' слов, которые остались после нормализации.',
    Defins.SW: '«Стоп-слово» - часто используемые слова предлоги, артикли и т.п., которые модель запрограммирована'
               ' игнорировать.',
    Defins.NGRAMM: '«N-грамма» - группа токенов.'
}

definRefs = {
    Defins.NORMALIZATION: {
        'Снижение размерности': 'useFor',
        'Метод предобработки текста перед кластеризацией': 'isA',
        'Фильтрация токенов': 'uses',
        'Лемматизация': 'uses',
        'Стемминг': 'uses'
    },
    Defins.VECTORIZATION: {'Метод предобработки текста перед кластеризацией': 'isA'},
    Defins.PREPMETH: {'Предобработка текстов': 'useFor'},
    Defins.REDUCEDIM: {
        'Предобработка текстов': 'isA',
        'Очистка данных': 'uses'
    },
    Defins.PREP: {'Кластеризация текстов': 'next'},
    Defins.CLUST: {},
    Defins.FILTER: {
        'Очистка данных': 'isA',
        'Токен': 'uses',
        'Стоп-слово': 'uses'
    },
    Defins.LEM: {'Очистка данных': 'isA'},
    Defins.STEM: {'Очистка данных': 'isA'},
    Defins.TOKEN: {'N-грамма': 'uses'},
    Defins.SW: {},
    Defins.NGRAMM: {}
}

notEditableDefs = [Defins.NORMALIZATION, Defins.FILTER, Defins.PREP, Defins.REDUCEDIM, Defins.PREPMETH]


class Ui_DefWindow(object):
    def setupUi(self, MainWindow, settings=None, viewType=ViewType.VIEW, defin=Defins.NORMALIZATION):
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
        self.TEDef.setText(definDict[defin])
        self.TEDef.setReadOnly(True)
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

        self.mainWindow = MainWindow
        self.settings = settings
        self.viewType = viewType
        self.defin = defin

        self.setupAll()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.GBDefInfo.setTitle(_translate("MainWindow", "Информация о понятии"))
        _translate = QtCore.QCoreApplication.translate
        item = self.TWRefs.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Определение"))
        item = self.TWRefs.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Тип связи"))
        self.LDef.setText(_translate("MainWindow", "Определение:"))
        self.LRefs.setText(_translate("MainWindow", "Связи:"))
        self.CBUse.setText(_translate("MainWindow", "Использовать"))
        self.LVal.setText(_translate("MainWindow", "Значение:"))
        self.BAccept.setText(_translate("MainWindow", "Принять изменения"))
        self.BClose.setText(_translate("MainWindow", "Закрыть"))

    def setupAll(self):
        self.setupRefs()
        if self.defin in notEditableDefs:
            self.setupNotEditableFields()
        self.setupButtons()

    def setupRefs(self):
        self.TWRefs.clear()
        item = QtWidgets.QTableWidgetItem()
        self.TWRefs.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWRefs.setHorizontalHeaderItem(1, item)
        self.TWRefs.setRowCount(len(definRefs[self.defin]))
        if self.TWRefs.rowCount() == 0:
            self.TWRefs.hide()
            return
        for i, ref in enumerate(definRefs[self.defin]):
            item = QtWidgets.QTableWidgetItem(ref)
            item.setToolTip(ref)
            self.TWRefs.setItem(i, 0, item)
            self.TWRefs.setItem(i, 1, QtWidgets.QTableWidgetItem(definRefs[self.defin][ref]))

        self.TWRefs.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def setupButtons(self):
        self.BClose.clicked.connect(self.mainWindow.close)

    def setupNotEditableFields(self):
        self.CBUse.hide()
        self.LVal.hide()
        self.LEVal.hide()
        self.CBVal.hide()
        self.BAccept.hide()

    def saveParam(self):
        if self.defin == Defins.NORMALIZATION:
            return
        if self.defin == Defins.VECTORIZATION:
            return
        if self.defin == Defins.PREPMETH:
            return
        if self.defin == Defins.REDUCEDIM:
            return
        if self.defin == Defins.PREP:
            return
        if self.defin == Defins.CLUST:
            return
        if self.defin == Defins.FILTER:
            return
        if self.defin == Defins.LEM:
            return
        if self.defin == Defins.STEM:
            return
        if self.defin == Defins.TOKEN:
            return
        if self.defin == Defins.SW:
            return
        if self.defin == Defins.NGRAMM:
            return


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_DefWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

