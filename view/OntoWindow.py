from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt

from model.mixins.JsonEnumExtention import *
from view import DefWindow
from model.enums.Defins import Defins
from controller.OntoWindowController import OntoWindowController


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, settings=None, openType=ViewType.VIEW):
        super().__init__()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1079, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TWDefHide = QtWidgets.QTableWidget(self.centralwidget)
        self.TWDefHide.setGeometry(QtCore.QRect(250, 10, 501, 201))
        self.TWDefHide.setObjectName("TWDefHide")
        self.TWDefHide.setColumnCount(2)
        self.TWDefHide.setRowCount(0)
        self.TWDefHide.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        item = QtWidgets.QTableWidgetItem()
        self.TWDefHide.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWDefHide.setHorizontalHeaderItem(1, item)
        self.GBActions = QtWidgets.QGroupBox(self.centralwidget)
        self.GBActions.setGeometry(QtCore.QRect(10, 10, 231, 181))
        self.GBActions.setObjectName("GBActions")
        self.BSaveInFile = QtWidgets.QPushButton(self.GBActions)
        self.BSaveInFile.setGeometry(QtCore.QRect(20, 20, 191, 31))
        self.BSaveInFile.setObjectName("BSaveInFile")
        self.BLocalSave = QtWidgets.QPushButton(self.GBActions)
        self.BLocalSave.setGeometry(QtCore.QRect(20, 60, 191, 31))
        self.BLocalSave.setObjectName("BLocalSave")
        self.BExit = QtWidgets.QPushButton(self.GBActions)
        self.BExit.setGeometry(QtCore.QRect(20, 140, 191, 31))
        self.BExit.setObjectName("BExit")
        self.BLoadFromFile = QtWidgets.QPushButton(self.GBActions)
        self.BLoadFromFile.setGeometry(QtCore.QRect(20, 100, 191, 31))
        self.BLoadFromFile.setObjectName("BLoadFromFile")
        self.BClust = QtWidgets.QPushButton(self.centralwidget)
        self.BClust.setGeometry(QtCore.QRect(770, 510, 151, 31))
        self.BClust.setObjectName("BClust")
        self.BPrep = QtWidgets.QPushButton(self.centralwidget)
        self.BPrep.setGeometry(QtCore.QRect(770, 440, 151, 31))
        self.BPrep.setObjectName("BPrep")
        self.BClearData = QtWidgets.QPushButton(self.centralwidget)
        self.BClearData.setGeometry(QtCore.QRect(360, 500, 151, 31))
        self.BClearData.setObjectName("BClearData")
        self.BReduceDim = QtWidgets.QPushButton(self.centralwidget)
        self.BReduceDim.setGeometry(QtCore.QRect(890, 340, 151, 31))
        self.BReduceDim.setObjectName("BReduceDim")
        self.BNormalize = QtWidgets.QPushButton(self.centralwidget)
        self.BNormalize.setGeometry(QtCore.QRect(600, 250, 151, 31))
        self.BNormalize.setObjectName("BNormalize")
        self.BFilter = QtWidgets.QPushButton(self.centralwidget)
        self.BFilter.setGeometry(QtCore.QRect(170, 340, 151, 31))
        self.BFilter.setObjectName("BFilter")
        self.BStopWord = QtWidgets.QPushButton(self.centralwidget)
        self.BStopWord.setGeometry(QtCore.QRect(200, 420, 151, 31))
        self.BStopWord.setObjectName("BStopWord")
        self.BToken = QtWidgets.QPushButton(self.centralwidget)
        self.BToken.setGeometry(QtCore.QRect(30, 420, 151, 31))
        self.BToken.setObjectName("BToken")
        self.BLem = QtWidgets.QPushButton(self.centralwidget)
        self.BLem.setGeometry(QtCore.QRect(330, 340, 151, 31))
        self.BLem.setObjectName("BLem")
        self.BStem = QtWidgets.QPushButton(self.centralwidget)
        self.BStem.setGeometry(QtCore.QRect(490, 340, 151, 31))
        self.BStem.setObjectName("BStem")
        self.BGramm = QtWidgets.QPushButton(self.centralwidget)
        self.BGramm.setGeometry(QtCore.QRect(30, 470, 151, 31))
        self.BGramm.setObjectName("BGramm")
        self.BPrepMeth = QtWidgets.QPushButton(self.centralwidget)
        self.BPrepMeth.setGeometry(QtCore.QRect(680, 340, 171, 41))
        self.BPrepMeth.setObjectName("BPrepMeth")
        self.BVectorize = QtWidgets.QPushButton(self.centralwidget)
        self.BVectorize.setGeometry(QtCore.QRect(810, 250, 151, 31))
        self.BVectorize.setObjectName("BVectorize")
        self.GVBgOnto = QtWidgets.QGraphicsView(self.centralwidget)
        self.GVBgOnto.setGeometry(QtCore.QRect(10, 230, 1061, 321))
        self.GVBgOnto.setObjectName("GVBgOnto")
        self.LbNormalizeIs = QtWidgets.QLabel(self.centralwidget)
        self.LbNormalizeIs.setGeometry(QtCore.QRect(725, 320, 21, 16))
        self.LbNormalizeIs.setObjectName("LbNormalizeIs")
        self.LbVectorizeIs = QtWidgets.QLabel(self.centralwidget)
        self.LbVectorizeIs.setGeometry(QtCore.QRect(845, 320, 21, 16))
        self.LbVectorizeIs.setObjectName("LbVectorizeIs")
        self.LbNormalizeUseFor = QtWidgets.QLabel(self.centralwidget)
        self.LbNormalizeUseFor.setGeometry(QtCore.QRect(970, 320, 41, 16))
        self.LbNormalizeUseFor.setObjectName("LbNormalizeUseFor")
        self.LbPrepMethUseFor = QtWidgets.QLabel(self.centralwidget)
        self.LbPrepMethUseFor.setGeometry(QtCore.QRect(750, 390, 41, 16))
        self.LbPrepMethUseFor.setObjectName("LbPrepMethUseFor")
        self.LbReduceIs = QtWidgets.QLabel(self.centralwidget)
        self.LbReduceIs.setGeometry(QtCore.QRect(950, 390, 21, 16))
        self.LbReduceIs.setObjectName("LbReduceIs")
        self.LbPrepNext = QtWidgets.QLabel(self.centralwidget)
        self.LbPrepNext.setGeometry(QtCore.QRect(850, 480, 31, 16))
        self.LbPrepNext.setObjectName("LbPrepNext")
        self.LbStemUses = QtWidgets.QLabel(self.centralwidget)
        self.LbStemUses.setGeometry(QtCore.QRect(540, 320, 41, 16))
        self.LbStemUses.setObjectName("LbStemUses")
        self.LbLemUses = QtWidgets.QLabel(self.centralwidget)
        self.LbLemUses.setGeometry(QtCore.QRect(410, 320, 41, 16))
        self.LbLemUses.setObjectName("LbLemUses")
        self.LbFilterUses = QtWidgets.QLabel(self.centralwidget)
        self.LbFilterUses.setGeometry(QtCore.QRect(260, 320, 41, 16))
        self.LbFilterUses.setObjectName("LbFilterUses")
        self.LbTokenUses = QtWidgets.QLabel(self.centralwidget)
        self.LbTokenUses.setGeometry(QtCore.QRect(95, 400, 41, 16))
        self.LbTokenUses.setObjectName("LbTokenUses")
        self.LbStopWordsUses = QtWidgets.QLabel(self.centralwidget)
        self.LbStopWordsUses.setGeometry(QtCore.QRect(210, 400, 41, 16))
        self.LbStopWordsUses.setObjectName("LbStopWordsUses")
        self.LbGrammUses = QtWidgets.QLabel(self.centralwidget)
        self.LbGrammUses.setGeometry(QtCore.QRect(105, 450, 41, 16))
        self.LbGrammUses.setObjectName("LbGrammUses")
        self.LbLemIs = QtWidgets.QLabel(self.centralwidget)
        self.LbLemIs.setGeometry(QtCore.QRect(400, 400, 21, 16))
        self.LbLemIs.setObjectName("LbLemIs")
        self.LbStemIs = QtWidgets.QLabel(self.centralwidget)
        self.LbStemIs.setGeometry(QtCore.QRect(500, 400, 21, 16))
        self.LbStemIs.setObjectName("LbStemIs")
        self.LbFilterIs = QtWidgets.QLabel(self.centralwidget)
        self.LbFilterIs.setGeometry(QtCore.QRect(320, 400, 21, 16))
        self.LbFilterIs.setObjectName("LbFilterIs")
        self.LbClearUses = QtWidgets.QLabel(self.centralwidget)
        self.LbClearUses.setGeometry(QtCore.QRect(860, 390, 41, 16))
        self.LbClearUses.setObjectName("LbClearUses")
        self.GVBgOnto.raise_()
        self.TWDefHide.raise_()
        self.GBActions.raise_()
        self.BReduceDim.raise_()
        self.BNormalize.raise_()
        self.BFilter.raise_()
        self.BLem.raise_()
        self.BStem.raise_()
        self.BPrepMeth.raise_()
        self.BVectorize.raise_()
        self.LbNormalizeIs.raise_()
        self.LbVectorizeIs.raise_()
        self.LbNormalizeUseFor.raise_()
        self.LbPrepMethUseFor.raise_()
        self.LbReduceIs.raise_()
        self.LbPrepNext.raise_()
        self.LbStemUses.raise_()
        self.LbLemUses.raise_()
        self.LbFilterUses.raise_()
        self.LbTokenUses.raise_()
        self.LbStopWordsUses.raise_()
        self.LbGrammUses.raise_()
        self.LbLemIs.raise_()
        self.LbStemIs.raise_()
        self.LbFilterIs.raise_()
        self.BStopWord.raise_()
        self.BToken.raise_()
        self.BGramm.raise_()
        self.BClearData.raise_()
        self.BPrep.raise_()
        self.BClust.raise_()
        self.LbClearUses.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1079, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.settings = settings
        self.__meWnd = MainWindow
        self.__localSettings = settings
        self.__openType = openType
        self.__defDict = None
        self.__defs = None
        self.__strDefins = None
        self.__controller = OntoWindowController(self.__localSettings)
        self.__defWindow = None
        self.__defWindowUI = None
        self.__eraseDict = None

        self.__meWnd.paintEvent = self.painEvent

        self.__initWndView()
        self.__initDefWnd()
        self.__initStrDefins()
        self.__initEraseDict()
        self.initButtons()
        self.__meWnd.closeEvent = self.closeEvent

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.__initTable()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.TWDefHide.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Определение"))
        item = self.TWDefHide.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Скрыто"))
        self.GBActions.setTitle(_translate("MainWindow", "Действия"))
        self.BSaveInFile.setText(_translate("MainWindow", "Сохранить в файле"))
        self.BLocalSave.setText(_translate("MainWindow", "Сохранить в сессии"))
        self.BExit.setText(_translate("MainWindow", "Отмена"))
        self.BLoadFromFile.setText(_translate("MainWindow", "Загрузить из файла"))
        self.BClust.setText(_translate("MainWindow", "Кластеризация текстов"))
        self.BPrep.setText(_translate("MainWindow", "Предобработка текстов"))
        self.BClearData.setText(_translate("MainWindow", "Очистка данных"))
        self.BReduceDim.setText(_translate("MainWindow", "Снижение размерности"))
        self.BNormalize.setText(_translate("MainWindow", "Нормализация текстов"))
        self.BFilter.setText(_translate("MainWindow", "Фильтрация токенов"))
        self.BStopWord.setText(_translate("MainWindow", "Стоп-слово"))
        self.BToken.setText(_translate("MainWindow", "Токен"))
        self.BLem.setText(_translate("MainWindow", "Лемматизация"))
        self.BStem.setText(_translate("MainWindow", "Стемминг"))
        self.BGramm.setText(_translate("MainWindow", "n-грамма"))
        self.BPrepMeth.setText(_translate("MainWindow", "Метод предобработки текста \n"
"перед кластеризацией"))
        self.BVectorize.setText(_translate("MainWindow", "Векторизация текстов"))
        self.LbNormalizeIs.setText(_translate("MainWindow", "isA"))
        self.LbVectorizeIs.setText(_translate("MainWindow", "isA"))
        self.LbNormalizeUseFor.setText(_translate("MainWindow", "useFor"))
        self.LbPrepMethUseFor.setText(_translate("MainWindow", "useFor"))
        self.LbReduceIs.setText(_translate("MainWindow", "isA"))
        self.LbPrepNext.setText(_translate("MainWindow", "next"))
        self.LbStemUses.setText(_translate("MainWindow", "uses"))
        self.LbLemUses.setText(_translate("MainWindow", "uses"))
        self.LbFilterUses.setText(_translate("MainWindow", "uses"))
        self.LbTokenUses.setText(_translate("MainWindow", "uses"))
        self.LbStopWordsUses.setText(_translate("MainWindow", "uses"))
        self.LbGrammUses.setText(_translate("MainWindow", "uses"))
        self.LbLemIs.setText(_translate("MainWindow", "isA"))
        self.LbStemIs.setText(_translate("MainWindow", "isA"))
        self.LbFilterIs.setText(_translate("MainWindow", "isA"))
        self.LbClearUses.setText(_translate("MainWindow", "uses"))

    def initButtons(self):
        # кнопки управления
        self.BSaveInFile.clicked.connect(self.__saveSettsInFile)
        self.BLocalSave.clicked.connect(self.__saveSettsLocal)
        self.BLoadFromFile.clicked.connect(self.__openSetts)
        self.BExit.clicked.connect(self.__cancelWnd)

        # определения
        self.BNormalize.clicked.connect(self.openDef)
        self.BVectorize.clicked.connect(self.openDef)
        self.BPrepMeth.clicked.connect(self.openDef)
        self.BReduceDim.clicked.connect(self.openDef)
        self.BPrep.clicked.connect(self.openDef)
        self.BClust.clicked.connect(self.openDef)
        self.BStem.clicked.connect(self.openDef)
        self.BLem.clicked.connect(self.openDef)
        self.BFilter.clicked.connect(self.openDef)
        self.BStopWord.clicked.connect(self.openDef)
        self.BToken.clicked.connect(self.openDef)
        self.BClearData.clicked.connect(self.openDef)
        self.BGramm.clicked.connect(self.openDef)

    def painEvent(self, event):
        painter = QPainter()
        pen = QPen(Qt.black, 5, Qt.SolidLine)

        self.lineNormalizeISPrepMeth = QtCore.QLineF(670, 280, 760, 340)
        self.pathNormalizeISPrepMeth = QtGui.QPainterPath(QtCore.QPoint(760, 340))
        self.pathNormalizeISPrepMeth.lineTo(754, 330)
        self.pathNormalizeISPrepMeth.lineTo(760, 340)
        self.pathNormalizeISPrepMeth.lineTo(750, 338)

        self.lineNormalizeUseForReduceDim = QtCore.QLineF(670, 280, 960, 340)
        self.pathNormalizeUseForReduceDim = QtGui.QPainterPath(QtCore.QPoint(960, 340))
        self.pathNormalizeUseForReduceDim.lineTo(949, 334)
        self.pathNormalizeUseForReduceDim.lineTo(960, 340)
        self.pathNormalizeUseForReduceDim.lineTo(945, 339)

        self.lineNormalizeUsesFilter = QtCore.QLineF(670, 280, 270, 340)
        self.pathNormalizeUsesFilter = QtGui.QPainterPath(QtCore.QPoint(270, 340))
        self.pathNormalizeUsesFilter.lineTo(280, 335)
        self.pathNormalizeUsesFilter.lineTo(270, 340)
        self.pathNormalizeUsesFilter.lineTo(285, 339)

        self.lineNormalizeUsesLem = QtCore.QLineF(670, 280, 410, 340)
        self.pathNormalizeUsesLem = QtGui.QPainterPath(QtCore.QPoint(410, 340))
        self.pathNormalizeUsesLem.lineTo(420, 335)
        self.pathNormalizeUsesLem.lineTo(410, 340)
        self.pathNormalizeUsesLem.lineTo(425, 339)

        self.lineNormalizeUsesStem = QtCore.QLineF(670, 280, 570, 340)
        self.pathNormalizeUsesStem = QtGui.QPainterPath(QtCore.QPoint(570, 340))
        self.pathNormalizeUsesStem.lineTo(574, 330)
        self.pathNormalizeUsesStem.lineTo(570, 340)
        self.pathNormalizeUsesStem.lineTo(580, 338)

        self.lineVectorizeIsPrepMeth = QtCore.QLineF(885, 280, 830, 340)
        self.pathVectorizeIsPrepMeth = QtGui.QPainterPath(QtCore.QPoint(830, 340))
        self.pathVectorizeIsPrepMeth.lineTo(828, 330)
        self.pathVectorizeIsPrepMeth.lineTo(830, 340)
        self.pathVectorizeIsPrepMeth.lineTo(844, 334)

        self.linePrepMethUseForPrep = QtCore.QLineF(755, 380, 850, 440)
        self.pathPrepMethUseForPrep = QtGui.QPainterPath(QtCore.QPoint(850, 440))
        self.pathPrepMethUseForPrep.lineTo(845, 430)
        self.pathPrepMethUseForPrep.lineTo(850, 440)
        self.pathPrepMethUseForPrep.lineTo(840, 438)

        self.lineReduceDimUsesClearData = QtCore.QLineF(965, 370, 440, 500)
        self.pathReduceDimUsesClearData = QtGui.QPainterPath(QtCore.QPoint(440, 500))
        self.pathReduceDimUsesClearData.lineTo(451, 495)
        self.pathReduceDimUsesClearData.lineTo(440, 500)
        self.pathReduceDimUsesClearData.lineTo(454, 499)

        self.lineReduceDimIsPrep = QtCore.QLineF(965, 370, 860, 440)
        self.pathReduceDimIsPrep = QtGui.QPainterPath(QtCore.QPoint(860, 440))
        self.pathReduceDimIsPrep.lineTo(865, 430)
        self.pathReduceDimIsPrep.lineTo(860, 440)
        self.pathReduceDimIsPrep.lineTo(875, 435)

        self.linePrepNextClust = QtCore.QLineF(845, 470, 845, 510)
        self.pathPrepNextClust = QtGui.QPainterPath(QtCore.QPoint(845, 510))
        self.pathPrepNextClust.lineTo(840, 500)
        self.pathPrepNextClust.lineTo(845, 510)
        self.pathPrepNextClust.lineTo(850, 500)

        self.lineStemIsClearData = QtCore.QLineF(565, 370, 440, 500)
        self.pathStemIsClearData = QtGui.QPainterPath(QtCore.QPoint(440, 500))
        self.pathStemIsClearData.lineTo(447, 485)
        self.pathStemIsClearData.lineTo(440, 500)
        self.pathStemIsClearData.lineTo(454, 491)

        self.lineLemIsClearData = QtCore.QLineF(405, 370, 440, 500)
        self.pathLemIsClearData = QtGui.QPainterPath(QtCore.QPoint(440, 500))
        self.pathLemIsClearData.lineTo(429, 485)
        self.pathLemIsClearData.lineTo(440, 500)
        self.pathLemIsClearData.lineTo(442, 485)

        self.lineFilterIsClearData = QtCore.QLineF(245, 370, 440, 500)
        self.pathFilterIsClearData = QtGui.QPainterPath(QtCore.QPoint(440, 500))
        self.pathFilterIsClearData.lineTo(426, 485)
        self.pathFilterIsClearData.lineTo(440, 500)
        self.pathFilterIsClearData.lineTo(426, 497)

        self.lineFilterUsesToken = QtCore.QLineF(245, 370, 100, 420)
        self.pathFilterUsesToken = QtGui.QPainterPath(QtCore.QPoint(100, 420))
        self.pathFilterUsesToken.lineTo(113, 412)
        self.pathFilterUsesToken.lineTo(100, 420)
        self.pathFilterUsesToken.lineTo(115, 419)

        self.lineFilterUsesSW = QtCore.QLineF(245, 370, 265, 420)
        self.pathFilterUsesSW = QtGui.QPainterPath(QtCore.QPoint(265, 420))
        self.pathFilterUsesSW.lineTo(255, 410)
        self.pathFilterUsesSW.lineTo(265, 420)
        self.pathFilterUsesSW.lineTo(268, 410)

        self.lineTokenUsesNGramm = QtCore.QLineF(100, 450, 100, 470)
        self.pathTokenUsesNGramm = QtGui.QPainterPath(QtCore.QPoint(100, 470))
        self.pathTokenUsesNGramm.lineTo(95, 460)
        self.pathTokenUsesNGramm.lineTo(100, 470)
        self.pathTokenUsesNGramm.lineTo(105, 460)

        painter.setPen(pen)

        painter.begin(self.__meWnd)

        if not self.__eraseDict[self.BNormalize] and not self.__eraseDict[self.BPrepMeth]:
            painter.drawLine(self.lineNormalizeISPrepMeth)
            painter.drawPath(self.pathNormalizeISPrepMeth)

        if not self.__eraseDict[self.BNormalize] and not self.__eraseDict[self.BReduceDim]:
            painter.drawLine(self.lineNormalizeUseForReduceDim)
            painter.drawPath(self.pathNormalizeUseForReduceDim)

        if not self.__eraseDict[self.BNormalize] and not self.__eraseDict[self.BFilter]:
            painter.drawLine(self.lineNormalizeUsesFilter)
            painter.drawPath(self.pathNormalizeUsesFilter)

        if not self.__eraseDict[self.BNormalize] and not self.__eraseDict[self.BLem]:
            painter.drawLine(self.lineNormalizeUsesLem)
            painter.drawPath(self.pathNormalizeUsesLem)

        if not self.__eraseDict[self.BNormalize] and not self.__eraseDict[self.BStem]:
            painter.drawLine(self.lineNormalizeUsesStem)
            painter.drawPath(self.pathNormalizeUsesStem)

        if not self.__eraseDict[self.BVectorize] and not self.__eraseDict[self.BPrepMeth]:
            painter.drawLine(self.lineVectorizeIsPrepMeth)
            painter.drawPath(self.pathVectorizeIsPrepMeth)

        if not self.__eraseDict[self.BPrepMeth] and not self.__eraseDict[self.BPrep]:
            painter.drawLine(self.linePrepMethUseForPrep)
            painter.drawPath(self.pathPrepMethUseForPrep)

        if not self.__eraseDict[self.BReduceDim] and not self.__eraseDict[self.BPrep]:
            painter.drawLine(self.lineReduceDimIsPrep)
            painter.drawPath(self.pathReduceDimIsPrep)

        if not self.__eraseDict[self.BReduceDim] and not self.__eraseDict[self.BClearData]:
            painter.drawLine(self.lineReduceDimUsesClearData)
            painter.drawPath(self.pathReduceDimUsesClearData)

        if not self.__eraseDict[self.BPrep] and not self.__eraseDict[self.BClust]:
            painter.drawLine(self.linePrepNextClust)
            painter.drawPath(self.pathPrepNextClust)

        if not self.__eraseDict[self.BStem] and not self.__eraseDict[self.BClearData]:
            painter.drawLine(self.lineStemIsClearData)
            painter.drawPath(self.pathStemIsClearData)

        if not self.__eraseDict[self.BLem] and not self.__eraseDict[self.BClearData]:
            painter.drawLine(self.lineLemIsClearData)
            painter.drawPath(self.pathLemIsClearData)

        if not self.__eraseDict[self.BFilter] and not self.__eraseDict[self.BClearData]:
            painter.drawLine(self.lineFilterIsClearData)
            painter.drawPath(self.pathFilterIsClearData)

        if not self.__eraseDict[self.BFilter] and not self.__eraseDict[self.BToken]:
            painter.drawLine(self.lineFilterUsesToken)
            painter.drawPath(self.pathFilterUsesToken)

        if not self.__eraseDict[self.BFilter] and not self.__eraseDict[self.BStopWord]:
            painter.drawLine(self.lineFilterUsesSW)
            painter.drawPath(self.pathFilterUsesSW)

        if not self.__eraseDict[self.BToken] and not self.__eraseDict[self.BGramm]:
            painter.drawLine(self.lineTokenUsesNGramm)
            painter.drawPath(self.pathTokenUsesNGramm)

        painter.end()

        self.__initDefDict()
        self.GVBgOnto.hide()

    def onCellChanged(self, row, column):
        item = self.TWDefHide.item(row, 0)
        itemState = self.TWDefHide.item(row, 1)
        btn = self.__defs[item.text()]
        for hideItems in self.__defDict[btn]:
            if itemState.checkState() == QtCore.Qt.Checked:
                hideItems.hide()
            else:
                hideItems.show()

        if itemState.checkState() == QtCore.Qt.Checked:
            btn.hide()
        else:
            btn.show()

        self.__eraseDict[btn] = itemState.checkState() == QtCore.Qt.Checked
        self.__meWnd.update()

    def closeEvent(self, event):
        if self.__openType == ViewType.VIEW:
            event.accept()
            return
        reply = QtWidgets.QMessageBox.question(self.__meWnd,
                                               'Сохранение настроек',
                                               'Сохранить настройки в сессии?',
                                               QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel,
                                               QtWidgets.QMessageBox.Cancel)

        if reply == QtWidgets.QMessageBox.Yes:
            self.__saveSettsLocal()
        event.accept()

    def __initEraseDict(self):
        self.__eraseDict = {
            self.BNormalize: False,
            self.BVectorize: False,
            self.BPrepMeth: False,
            self.BReduceDim: False,
            self.BPrep: False,
            self.BClust: False,
            self.BStem: False,
            self.BLem: False,
            self.BClearData: False,
            self.BFilter: False,
            self.BToken: False,
            self.BGramm: False,
            self.BStopWord: False
        }

    def __initDefDict(self):
        self.__defDict = {
            self.BNormalize: [self.LbNormalizeIs,
                              self.LbNormalizeUseFor,
                              self.LbStemUses,
                              self.LbLemUses,
                              self.LbFilterUses],
            self.BVectorize: [self.LbVectorizeIs],
            self.BPrepMeth: [self.LbPrepMethUseFor,
                             self.LbVectorizeIs,
                             self.LbNormalizeIs],
            self.BReduceDim: [self.LbReduceIs,
                              self.LbNormalizeUseFor,
                              self.LbClearUses],
            self.BPrep: [self.LbPrepNext,
                         self.LbPrepMethUseFor,
                         self.LbReduceIs],
            self.BClust: [self.LbPrepNext],
            self.BStem: [self.LbStemUses, self.LbStemIs],
            self.BLem: [self.LbLemUses, self.LbLemIs],
            self.BClearData: [self.LbClearUses, self.LbLemIs, self.LbStemIs, self.LbFilterIs],
            self.BFilter: [self.LbFilterUses,
                           self.LbFilterIs,
                           self.LbTokenUses,
                           self.LbStopWordsUses],
            self.BToken: [self.LbTokenUses,
                          self.LbGrammUses],
            self.BGramm: [self.LbGrammUses],
            self.BStopWord: [self.LbStopWordsUses]
        }

    def __initTable(self):
        self.__defs = {'Нормализация текстов': self.BNormalize,
                       'Векторизация текстов': self.BVectorize,
                       'Метод предобработки текста перед кластеризацией': self.BPrepMeth,
                       'Снижение размерности': self.BReduceDim,
                       'Предобработка текстов': self.BPrep,
                       'Кластеризация текстов': self.BClust,
                       'Фильтрация токенов': self.BFilter,
                       'Лемматизация': self.BLem,
                       'Стемминг': self.BStem,
                       'Токен': self.BToken,
                       'n-грамма': self.BGramm,
                       'Стоп-слово': self.BStopWord,
                       'Очистка данных': self.BClearData}

        self.TWDefHide.setRowCount(len(self.__defs))

        for i, defin in enumerate(self.__defs):
            self.TWDefHide.setItem(i, 0, QtWidgets.QTableWidgetItem(defin))

            item = QtWidgets.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            item.setCheckState(QtCore.Qt.Unchecked)

            self.TWDefHide.setItem(i, 1, item)

        self.TWDefHide.cellChanged.connect(self.onCellChanged)
        self.TWDefHide.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def __initWndView(self):
        self.BSaveInFile.setEnabled(self.__openType == ViewType.EDIT)
        self.BLocalSave.setEnabled(self.__openType == ViewType.EDIT)
        self.BLoadFromFile.setEnabled(self.__openType == ViewType.EDIT)
        self.BExit.setEnabled(self.__openType == ViewType.EDIT)

    def __initStrDefins(self):
        self.__strDefins = {
            'Нормализация текстов': Defins.NORMALIZATION,
            'Векторизация текстов': Defins.VECTORIZATION,
            'Метод предобработки текста \nперед кластеризацией': Defins.PREPMETH,
            'Снижение размерности': Defins.REDUCEDIM,
            'Предобработка текстов': Defins.PREP,
            'Кластеризация текстов': Defins.CLUST,
            'Фильтрация токенов': Defins.FILTER,
            'Лемматизация': Defins.LEM,
            'Стемминг': Defins.STEM,
            'Токен': Defins.TOKEN,
            'n-грамма': Defins.NGRAMM,
            'Стоп-слово': Defins.SW,
            'Очистка данных': Defins.CLEARDATA
        }

    def __saveSettsInFile(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fName, _ = QtWidgets.QFileDialog.getSaveFileName(self.__meWnd,
                                                          "Сохранение",
                                                          "../settingsTemplates",
                                                          "Файлы настроек (*.json)",
                                                          options=options)
        self.__saveSettsLocal()
        self.__controller.saveSettsInFile(fName)

    def __saveSettsLocal(self):
        self.settings = self.__localSettings
        self.__meWnd.prevWindow.setSettings(self.settings)

    def __cancelWnd(self):
        self.__localSettings = self.settings
        self.__meWnd.close()

    def __openSetts(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fName, _ = QtWidgets.QFileDialog.getOpenFileName(self.__meWnd,
                                                          "Выбор файла настроек",
                                                          "../settingsTemplates",
                                                          "Файлы настроек (*.json)",
                                                          options=options)
        self.__localSettings = self.__controller.openSetts(fName)

    def __initDefWnd(self):
        self.__defWindow = QtWidgets.QMainWindow()
        self.__defWindow.prevWindow = self
        self.__defWindowUI = DefWindow.Ui_DefWindow()

    def openDef(self):
        self.__defWindowUI.setupUi(self.__defWindow, self.__localSettings, self.__openType, self.__strDefins[self.__meWnd.sender().text()])
        self.__defWindow.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

