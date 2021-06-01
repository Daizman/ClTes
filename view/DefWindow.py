# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\DefWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from model.enums.ViewType import ViewType
from model.enums.Defins import Defins
from model.enums.VectorizationType import VectorizationType
from model.enums.ClusterizationType import ClusterizationType


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
                'слова, называемой леммой, в словарь.\nНельзя использовать вместе со стеммингом.',
    Defins.STEM: '«Стемминг» - использование набора правил (или моделей) для разбиения строки на меньшие подстроки,'
                ' с целью удаления приставок и суффиксов слов, которые изменяют значение.'
                 '\nНельзя использовать вместе с лемматизацией.',
    Defins.TOKEN: '«Токен» - самостоятельная единица текста, в используемых моделях это обозначение используется для'
                  ' слов, которые остались после нормализации.',
    Defins.SW: '«Стоп-слово» - часто используемые слова предлоги, артикли и т.п., которые модель запрограммирована'
               ' игнорировать.',
    Defins.NGRAMM: '«N-грамма» - группа токенов.',
    Defins.CLEARDATA: '«Очистка данных» - подготовка данных для векторизации при снижении размерности.'
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
    Defins.NGRAMM: {},
    Defins.CLEARDATA: {}
}

vectVals = {
    VectorizationType.TF: 'Частотное',
    VectorizationType.TFIDF: 'TF-IDF',
    VectorizationType.ONEHOT: 'Не зависимо от количества встречь',
    VectorizationType.DISTR: 'Распределенная модель',
    VectorizationType.HASH: 'TF-IDF с использованием хэширования'
}

clustVals = {
    ClusterizationType.KMEANS: 'K-Means',
    ClusterizationType.MINIBATCH_KMEANS: 'K-Means с использованием подгрупп',
    ClusterizationType.BIRCH: 'Birch',
    ClusterizationType.AGGLOMERATIVE: 'Agglomerative',
    ClusterizationType.SPECTRAL: 'Spectral',
}

notEditableDefs = [Defins.NORMALIZATION, Defins.FILTER, Defins.PREP, Defins.REDUCEDIM, Defins.PREPMETH, Defins.CLEARDATA]
usableDefs = [Defins.LEM, Defins.STEM, Defins.SW, Defins.TOKEN, Defins.NGRAMM]
selectableDefs = [Defins.CLUST, Defins.VECTORIZATION]
inputDefs = [Defins.TOKEN, Defins.SW, Defins.NGRAMM]
onlyUse = [Defins.LEM, Defins.STEM]


class Ui_DefWindow(object):
    def setupUi(self, MainWindow, settings=None, viewType=ViewType.VIEW, defin=Defins.NORMALIZATION):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(317, 695)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.GBDefInfo = QtWidgets.QGroupBox(self.centralwidget)
        self.GBDefInfo.setGeometry(QtCore.QRect(20, 10, 282, 660))
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
        if defin != Defins.SW:
            self.TWRefs = QtWidgets.QTableWidget(self.GBDefInfo)
            self.TWRefs.setObjectName("TWRefs")
            self.TWRefs.setColumnCount(2)
            self.TWRefs.setRowCount(0)
            item = QtWidgets.QTableWidgetItem()
            self.TWRefs.setHorizontalHeaderItem(0, item)
            item = QtWidgets.QTableWidgetItem()
            self.TWRefs.setHorizontalHeaderItem(1, item)
            self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.TWRefs)
        else:
            self.TWWords = QtWidgets.QTableWidget(self.GBDefInfo)
            self.TWWords.setObjectName("TWWords")
            self.TWWords.setColumnCount(1)
            self.TWWords.setRowCount(0)
            item = QtWidgets.QTableWidgetItem()
            self.TWWords.setHorizontalHeaderItem(0, item)
            self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.TWWords)
        self.CBUse = QtWidgets.QCheckBox(self.GBDefInfo)
        self.CBUse.setObjectName("CBUse")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.CBUse)
        self.LVal = QtWidgets.QLabel(self.GBDefInfo)
        self.LVal.setObjectName("LVal")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.LVal)
        self.LEVal = QtWidgets.QLineEdit(self.GBDefInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LEVal.sizePolicy().hasHeightForWidth())
        self.LEVal.setSizePolicy(sizePolicy)
        self.LEVal.setObjectName("LEVal")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.LEVal)
        self.LVal2 = QtWidgets.QLabel(self.GBDefInfo)
        self.LVal2.setObjectName("LVal2")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.LVal2)
        self.LEVal2 = QtWidgets.QLineEdit(self.GBDefInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LEVal2.sizePolicy().hasHeightForWidth())
        self.LEVal2.setSizePolicy(sizePolicy)
        self.LEVal2.setObjectName("LEVal2")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.LEVal2)
        self.LEVal2.hide()
        self.LVal2.hide()
        self.LVal3 = QtWidgets.QLabel(self.GBDefInfo)
        self.LVal3.setObjectName("LVal3")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.LVal3)
        self.LEVal3 = QtWidgets.QLineEdit(self.GBDefInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LEVal3.sizePolicy().hasHeightForWidth())
        self.LEVal3.setSizePolicy(sizePolicy)
        self.LEVal3.setObjectName("LEVal3")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.LEVal3)
        self.LEVal3.hide()
        self.LEVal3.hide()
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        if defin == Defins.SW:
            self.BAddSw = QtWidgets.QPushButton(self.GBDefInfo)
            self.BAddSw.setObjectName("BAddSw")
            self.BAddSw.setGeometry(QtCore.QRect(160, 500, 40, 20))
            self.BRemoveSw = QtWidgets.QPushButton(self.GBDefInfo)
            self.BRemoveSw.setObjectName("BRemoveSw")
            self.BRemoveSw.setGeometry(QtCore.QRect(210, 500, 40, 20))
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
        self.formLayout.setLayout(12, QtWidgets.QFormLayout.SpanningRole, self.gridLayout)
        self.CBVal = QtWidgets.QComboBox(self.GBDefInfo)
        self.CBVal.setObjectName("CBVal")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.SpanningRole, self.CBVal)
        self.CBVal.hide()
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

        self.retranslateUi(MainWindow)
        self.setupAll()

        if self.defin in onlyUse:
            self.LVal.hide()
            self.LEVal.hide()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.GBDefInfo.setTitle(_translate("MainWindow", "Информация о понятии"))
        _translate = QtCore.QCoreApplication.translate
        if self.defin != Defins.SW:
            item = self.TWRefs.horizontalHeaderItem(0)
            item.setText(_translate("MainWindow", "Определение"))
            item = self.TWRefs.horizontalHeaderItem(1)
            item.setText(_translate("MainWindow", "Тип связи"))
        else:
            item = self.TWWords.horizontalHeaderItem(0)
            item.setText(_translate("MainWindow", "Стоп-слово"))
            self.BAddSw.setText(_translate("MainWindow", "+"))
            self.BRemoveSw.setText(_translate("MainWindow", "-"))
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
        if self.defin in selectableDefs:
            self.setupCBVal()
        if self.defin in inputDefs:
            self.setupTEVal()
        if self.defin not in usableDefs:
            self.CBUse.hide()
        else:
            self.checkDef()

        if self.viewType == ViewType.VIEW:
            self.setupView()

    def setupRefs(self):
        if self.defin == Defins.SW:
            return
        self.TWRefs.clear()
        item = QtWidgets.QTableWidgetItem()
        self.TWRefs.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWRefs.setHorizontalHeaderItem(1, item)
        self.TWRefs.setRowCount(len(definRefs[self.defin]))
        if self.TWRefs.rowCount() == 0:
            self.TWRefs.hide()
            self.LRefs.hide()
            return
        for i, ref in enumerate(definRefs[self.defin]):
            item = QtWidgets.QTableWidgetItem(ref)
            item.setToolTip(ref)
            self.TWRefs.setItem(i, 0, item)
            self.TWRefs.setItem(i, 1, QtWidgets.QTableWidgetItem(definRefs[self.defin][ref]))

        self.TWRefs.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def setupButtons(self):
        self.BClose.clicked.connect(self.mainWindow.close)
        self.BAccept.clicked.connect(self.saveParam)
        if self.defin == Defins.SW:
            self.newSW = []
            self.removeSW = []
            self.BAddSw.clicked.connect(self.addSw)
            self.BRemoveSw.clicked.connect(self.removeSw)

    def addSw(self):
        self.LEVal.setText(self.LEVal.text().strip())
        self.newSW.append(self.LEVal.text().strip())
        olderCnt = self.TWWords.rowCount()
        self.TWWords.setRowCount(olderCnt + 1)
        self.TWWords.setItem(olderCnt, 0, QtWidgets.QTableWidgetItem(self.LEVal.text().strip()))
        self.LEVal.setText('')

    def removeSw(self):
        if self.TWWords.selectedItems()[0]:
            self.removeSW.append(self.TWWords.selectedItems()[0].text().strip())
            self.TWWords.removeRow(self.TWWords.selectedIndexes()[0].row())

    def setupNotEditableFields(self):
        self.CBUse.hide()
        self.LVal.hide()
        self.LEVal.hide()
        self.CBVal.hide()
        self.BAccept.hide()

    def checkDef(self):
        self.CBUse.stateChanged.connect(self.checkConflict)
        if self.defin == Defins.STEM:
            self.CBUse.setChecked(self.settings.useStem)
        if self.defin == Defins.LEM:
            self.CBUse.setChecked(self.settings.useLem)
        if self.defin == Defins.NGRAMM:
            self.CBUse.setChecked(self.settings.useGramms)
        if self.defin == Defins.SW:
            self.CBUse.setChecked(self.settings.useSW)
        if self.defin == Defins.TOKEN:
            self.CBUse.setChecked(self.settings.useTokenFilter)

    def checkConflict(self):
        error = QtWidgets.QErrorMessage(self.mainWindow)
        if self.CBUse.isChecked() and ((self.defin == Defins.LEM and self.settings.useStem)
                                       or (self.defin == Defins.STEM and self.settings.useLem)):
            error.setWindowTitle("Предупреждение.")
            error.showMessage("Можно выбрать либо лемматизацию, либо стемминг.")
            self.CBUse.setChecked(False)

    def setupCBVal(self):
        self.CBVal.show()
        if self.defin == Defins.VECTORIZATION:
            self.LEVal.hide()
            for el in vectVals:
                self.CBVal.addItem(vectVals[el], el)
            if self.settings.vectMeth is not None:
                self.CBVal.setCurrentIndex(self.CBVal.findData(self.settings.vectMeth))
        if self.defin == Defins.CLUST:
            self.LVal.setText('Количество кластеров:')
            self.LEVal.setInputMask("999")
            self.LEVal.setText(str(self.settings.clustCnt))
            self.LVal2.setText('Количество эпох обучения:')
            self.LEVal2.setInputMask("99999")
            self.LEVal2.setText(str(self.settings.maxIters))
            self.LVal2.show()
            self.LEVal2.show()
            for el in clustVals:
                self.CBVal.addItem(clustVals[el], el)
            if self.settings.clustMeth is not None:
                self.CBVal.setCurrentIndex(self.CBVal.findData(self.settings.clustMeth))

    def setupTEVal(self):
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LEVal.sizePolicy().hasHeightForWidth())
        self.LEVal.setSizePolicy(sizePolicy)
        if self.defin == Defins.NGRAMM:
            self.LVal.setText('Размер n-граммы:')
            self.LEVal.setInputMask("9999")
            self.LEVal.setText(str(self.settings.grammsSize))
        if self.defin == Defins.SW:
            self.TWWords.show()
            self.TWWords.setRowCount(len(self.settings.sw))
            for i, word in enumerate(self.settings.sw):
                self.TWWords.setItem(i, 0, QtWidgets.QTableWidgetItem(word))

            self.TWWords.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        if self.defin == Defins.TOKEN:
            self.CBUse.setText('Использовать фильтры на токены')
            self.LVal.setText('Максимальное количество токенов:')
            self.LEVal.setInputMask("9999999")
            self.LEVal.setText(str(self.settings.maxDictSize))
            self.LVal2.setText('Нижняя граница количества вхождений токена:')
            self.LEVal2.setInputMask("99999")
            self.LEVal2.setText(str(self.settings.minWordCnt))
            self.LVal2.show()
            self.LEVal2.show()
            self.LVal3.setText('Максимальная частота вхождений токена (1.00):')
            self.LEVal3.setInputMask("9.99")
            self.LEVal3.setText(str(float(self.settings.maxWordFq)))
            self.LVal3.show()
            self.LEVal3.show()


    def setupView(self):
        self.CBUse.setEnabled(False)
        self.CBVal.setEnabled(False)
        self.LEVal.setReadOnly(True)
        self.BAccept.hide()
        if self.defin == Defins.SW:
            self.BAddSw.hide()
            self.BRemoveSw.hide()
            self.LEVal.hide()
            self.LVal.hide()

    def saveParam(self):
        if self.defin == Defins.VECTORIZATION:
            self.settings.vectMeth = self.CBVal.currentData()
            self.mainWindow.prevWindow.settings.vectMeth = self.settings.vectMeth
        if self.defin == Defins.CLUST:
            self.settings.clustMeth = self.CBVal.currentData()
            self.mainWindow.prevWindow.settings.clustMeth = self.settings.clustMeth
            self.settings.clustCnt = int(self.LEVal.text().strip())
            self.settings.maxIters = int(self.LEVal2.text().strip())
            self.mainWindow.prevWindow.settings.clustCnt = self.settings.clustCnt
            self.mainWindow.prevWindow.settings.maxIters = self.settings.maxIters
        if self.defin == Defins.LEM:
            self.settings.useLem = self.CBUse.isChecked()
            self.mainWindow.prevWindow.settings.useLem = self.settings.useLem
        if self.defin == Defins.STEM:
            self.settings.useStem = self.CBUse.isChecked()
            self.mainWindow.prevWindow.settings.useStem = self.settings.useStem
        if self.defin == Defins.TOKEN:
            self.settings.useTokenFilter = self.CBUse.isChecked()
            self.mainWindow.prevWindow.settings.useTokenFilter = self.settings.useTokenFilter
            self.settings.maxWordFq = float(self.LEVal3.text().strip())
            self.settings.minWordCnt = int(self.LEVal2.text().strip())
            self.settings.maxDictSize = int(self.LEVal.text().strip())
            self.mainWindow.prevWindow.settings.maxWordFq = self.settings.maxWordFq
            self.mainWindow.prevWindow.settings.minWordCnt = self.settings.minWordCnt
            self.mainWindow.prevWindow.settings.maxDictSize = self.settings.maxDictSize
        if self.defin == Defins.SW:
            self.settings.useSW = self.CBUse.isChecked()
            self.mainWindow.prevWindow.settings.useSW = self.settings.useSW
            for word in self.newSW:
                self.settings.sw.append(word)
            for word in self.removeSW:
                if word in self.settings.sw:
                    self.settings.sw.remove(word)
            self.mainWindow.prevWindow.settings.sw = self.settings.sw
        if self.defin == Defins.NGRAMM:
            self.settings.useGramms = self.CBUse.isChecked()
            self.mainWindow.prevWindow.settings.useGramms = self.settings.useGramms
            self.settings.grammsSize = int(self.LEVal.text().strip())
            self.mainWindow.prevWindow.settings.grammsSize = self.settings.grammsSize
        self.mainWindow.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_DefWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

