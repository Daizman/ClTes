# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\OntoWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from model.Settings import Settings
from model.mixins.JsonEnumExtention import *
from view import DefWindow
from model.enums.Defins import Defins


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, settings=None, openType=ViewType.VIEW):
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
        self.LClustNext = QtWidgets.QFrame(self.centralwidget)
        self.LClustNext.setGeometry(QtCore.QRect(840, 470, 16, 51))
        self.LClustNext.setMidLineWidth(1)
        self.LClustNext.setFrameShape(QtWidgets.QFrame.VLine)
        self.LClustNext.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LClustNext.setObjectName("LClustNext")
        self.LReduceUsesHor = QtWidgets.QFrame(self.centralwidget)
        self.LReduceUsesHor.setGeometry(QtCore.QRect(428, 420, 520, 3))
        self.LReduceUsesHor.setMidLineWidth(1)
        self.LReduceUsesHor.setFrameShape(QtWidgets.QFrame.HLine)
        self.LReduceUsesHor.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LReduceUsesHor.setObjectName("LReduceUsesHor")
        self.LClearDataIsVert = QtWidgets.QFrame(self.centralwidget)
        self.LClearDataIsVert.setGeometry(QtCore.QRect(420, 400, 16, 110))
        self.LClearDataIsVert.setMidLineWidth(1)
        self.LClearDataIsVert.setFrameShape(QtWidgets.QFrame.VLine)
        self.LClearDataIsVert.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LClearDataIsVert.setObjectName("LClearDataIsVert")
        self.LNormalizeUseFor = QtWidgets.QFrame(self.centralwidget)
        self.LNormalizeUseFor.setGeometry(QtCore.QRect(950, 310, 16, 32))
        self.LNormalizeUseFor.setMidLineWidth(1)
        self.LNormalizeUseFor.setFrameShape(QtWidgets.QFrame.VLine)
        self.LNormalizeUseFor.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LNormalizeUseFor.setObjectName("LNormalizeUseFor")
        self.LNormalizeIs2 = QtWidgets.QFrame(self.centralwidget)
        self.LNormalizeIs2.setGeometry(QtCore.QRect(740, 310, 16, 30))
        self.LNormalizeIs2.setMidLineWidth(1)
        self.LNormalizeIs2.setFrameShape(QtWidgets.QFrame.VLine)
        self.LNormalizeIs2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LNormalizeIs2.setObjectName("LNormalizeIs2")
        self.LLemUses = QtWidgets.QFrame(self.centralwidget)
        self.LLemUses.setGeometry(QtCore.QRect(390, 310, 16, 30))
        self.LLemUses.setMidLineWidth(1)
        self.LLemUses.setFrameShape(QtWidgets.QFrame.VLine)
        self.LLemUses.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LLemUses.setObjectName("LLemUses")
        self.LFilterUses = QtWidgets.QFrame(self.centralwidget)
        self.LFilterUses.setGeometry(QtCore.QRect(250, 310, 16, 30))
        self.LFilterUses.setMidLineWidth(1)
        self.LFilterUses.setFrameShape(QtWidgets.QFrame.VLine)
        self.LFilterUses.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LFilterUses.setObjectName("LFilterUses")
        self.LStemUses = QtWidgets.QFrame(self.centralwidget)
        self.LStemUses.setGeometry(QtCore.QRect(530, 310, 16, 30))
        self.LStemUses.setMidLineWidth(1)
        self.LStemUses.setFrameShape(QtWidgets.QFrame.VLine)
        self.LStemUses.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LStemUses.setObjectName("LStemUses")
        self.LTokenUses = QtWidgets.QFrame(self.centralwidget)
        self.LTokenUses.setGeometry(QtCore.QRect(90, 400, 16, 30))
        self.LTokenUses.setMidLineWidth(1)
        self.LTokenUses.setFrameShape(QtWidgets.QFrame.VLine)
        self.LTokenUses.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LTokenUses.setObjectName("LTokenUses")
        self.LFilterHor = QtWidgets.QFrame(self.centralwidget)
        self.LFilterHor.setGeometry(QtCore.QRect(100, 400, 180, 3))
        self.LFilterHor.setMidLineWidth(1)
        self.LFilterHor.setFrameShape(QtWidgets.QFrame.HLine)
        self.LFilterHor.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LFilterHor.setObjectName("LFilterHor")
        self.LStopWordsUses = QtWidgets.QFrame(self.centralwidget)
        self.LStopWordsUses.setGeometry(QtCore.QRect(270, 400, 16, 30))
        self.LStopWordsUses.setMidLineWidth(1)
        self.LStopWordsUses.setFrameShape(QtWidgets.QFrame.VLine)
        self.LStopWordsUses.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LStopWordsUses.setObjectName("LStopWordsUses")
        self.LFilterVert = QtWidgets.QFrame(self.centralwidget)
        self.LFilterVert.setGeometry(QtCore.QRect(210, 370, 16, 30))
        self.LFilterVert.setMidLineWidth(1)
        self.LFilterVert.setFrameShape(QtWidgets.QFrame.VLine)
        self.LFilterVert.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LFilterVert.setObjectName("LFilterVert")
        self.BGramm = QtWidgets.QPushButton(self.centralwidget)
        self.BGramm.setGeometry(QtCore.QRect(30, 470, 151, 31))
        self.BGramm.setObjectName("BGramm")
        self.LGrammUses = QtWidgets.QFrame(self.centralwidget)
        self.LGrammUses.setGeometry(QtCore.QRect(90, 450, 16, 30))
        self.LGrammUses.setMidLineWidth(1)
        self.LGrammUses.setFrameShape(QtWidgets.QFrame.VLine)
        self.LGrammUses.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LGrammUses.setObjectName("LGrammUses")
        self.LNormalizeAll = QtWidgets.QFrame(self.centralwidget)
        self.LNormalizeAll.setGeometry(QtCore.QRect(260, 310, 700, 3))
        self.LNormalizeAll.setMidLineWidth(1)
        self.LNormalizeAll.setFrameShape(QtWidgets.QFrame.HLine)
        self.LNormalizeAll.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LNormalizeAll.setObjectName("LNormalizeAll")
        self.BPrepMeth = QtWidgets.QPushButton(self.centralwidget)
        self.BPrepMeth.setGeometry(QtCore.QRect(680, 340, 171, 41))
        self.BPrepMeth.setObjectName("BPrepMeth")
        self.LReduceIsVert = QtWidgets.QFrame(self.centralwidget)
        self.LReduceIsVert.setGeometry(QtCore.QRect(940, 370, 16, 50))
        self.LReduceIsVert.setMidLineWidth(1)
        self.LReduceIsVert.setFrameShape(QtWidgets.QFrame.VLine)
        self.LReduceIsVert.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LReduceIsVert.setObjectName("LReduceIsVert")
        self.LPrepMehUseForVert = QtWidgets.QFrame(self.centralwidget)
        self.LPrepMehUseForVert.setGeometry(QtCore.QRect(740, 380, 16, 51))
        self.LPrepMehUseForVert.setMidLineWidth(1)
        self.LPrepMehUseForVert.setFrameShape(QtWidgets.QFrame.VLine)
        self.LPrepMehUseForVert.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LPrepMehUseForVert.setObjectName("LPrepMehUseForVert")
        self.LPrepVert = QtWidgets.QFrame(self.centralwidget)
        self.LPrepVert.setGeometry(QtCore.QRect(840, 420, 16, 30))
        self.LPrepVert.setMidLineWidth(1)
        self.LPrepVert.setFrameShape(QtWidgets.QFrame.VLine)
        self.LPrepVert.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LPrepVert.setObjectName("LPrepVert")
        self.LClearDataIsHor = QtWidgets.QFrame(self.centralwidget)
        self.LClearDataIsHor.setGeometry(QtCore.QRect(300, 400, 210, 3))
        self.LClearDataIsHor.setMidLineWidth(1)
        self.LClearDataIsHor.setFrameShape(QtWidgets.QFrame.HLine)
        self.LClearDataIsHor.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LClearDataIsHor.setObjectName("LClearDataIsHor")
        self.LFilterClear = QtWidgets.QFrame(self.centralwidget)
        self.LFilterClear.setGeometry(QtCore.QRect(290, 370, 16, 30))
        self.LFilterClear.setMidLineWidth(1)
        self.LFilterClear.setFrameShape(QtWidgets.QFrame.VLine)
        self.LFilterClear.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LFilterClear.setObjectName("LFilterClear")
        self.LLemClear = QtWidgets.QFrame(self.centralwidget)
        self.LLemClear.setGeometry(QtCore.QRect(390, 370, 16, 30))
        self.LLemClear.setMidLineWidth(1)
        self.LLemClear.setFrameShape(QtWidgets.QFrame.VLine)
        self.LLemClear.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LLemClear.setObjectName("LLemClear")
        self.LStemClear = QtWidgets.QFrame(self.centralwidget)
        self.LStemClear.setGeometry(QtCore.QRect(500, 370, 16, 30))
        self.LStemClear.setMidLineWidth(1)
        self.LStemClear.setFrameShape(QtWidgets.QFrame.VLine)
        self.LStemClear.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LStemClear.setObjectName("LStemClear")
        self.LNormalizeIs = QtWidgets.QFrame(self.centralwidget)
        self.LNormalizeIs.setGeometry(QtCore.QRect(660, 280, 16, 30))
        self.LNormalizeIs.setMidLineWidth(1)
        self.LNormalizeIs.setFrameShape(QtWidgets.QFrame.VLine)
        self.LNormalizeIs.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LNormalizeIs.setObjectName("LNormalizeIs")
        self.LVectorizeIs = QtWidgets.QFrame(self.centralwidget)
        self.LVectorizeIs.setGeometry(QtCore.QRect(830, 280, 16, 60))
        self.LVectorizeIs.setMidLineWidth(1)
        self.LVectorizeIs.setFrameShape(QtWidgets.QFrame.VLine)
        self.LVectorizeIs.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LVectorizeIs.setObjectName("LVectorizeIs")
        self.BVectorize = QtWidgets.QPushButton(self.centralwidget)
        self.BVectorize.setGeometry(QtCore.QRect(810, 250, 151, 31))
        self.BVectorize.setObjectName("BVectorize")
        self.GVBgOnto = QtWidgets.QGraphicsView(self.centralwidget)
        self.GVBgOnto.setGeometry(QtCore.QRect(10, 230, 1061, 321))
        self.GVBgOnto.setObjectName("GVBgOnto")
        self.LbNormalizeIs = QtWidgets.QLabel(self.centralwidget)
        self.LbNormalizeIs.setGeometry(QtCore.QRect(730, 320, 21, 16))
        self.LbNormalizeIs.setObjectName("LbNormalizeIs")
        self.LbVectorizeIs = QtWidgets.QLabel(self.centralwidget)
        self.LbVectorizeIs.setGeometry(QtCore.QRect(840, 320, 21, 16))
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
        self.LbTokenUses.setGeometry(QtCore.QRect(100, 400, 41, 16))
        self.LbTokenUses.setObjectName("LbTokenUses")
        self.LbStopWordsUses = QtWidgets.QLabel(self.centralwidget)
        self.LbStopWordsUses.setGeometry(QtCore.QRect(250, 400, 41, 16))
        self.LbStopWordsUses.setObjectName("LbStopWordsUses")
        self.LbGrammUses = QtWidgets.QLabel(self.centralwidget)
        self.LbGrammUses.setGeometry(QtCore.QRect(100, 450, 41, 16))
        self.LbGrammUses.setObjectName("LbGrammUses")
        self.LbClearIs = QtWidgets.QLabel(self.centralwidget)
        self.LbClearIs.setGeometry(QtCore.QRect(400, 400, 21, 16))
        self.LbClearIs.setObjectName("LbClearIs")
        self.LbClearUses = QtWidgets.QLabel(self.centralwidget)
        self.LbClearUses.setGeometry(QtCore.QRect(620, 400, 41, 16))
        self.LbClearUses.setObjectName("LbClearUses")
        self.LPrepMethUseForHor = QtWidgets.QFrame(self.centralwidget)
        self.LPrepMethUseForHor.setGeometry(QtCore.QRect(750, 430, 100, 3))
        self.LPrepMethUseForHor.setMidLineWidth(1)
        self.LPrepMethUseForHor.setFrameShape(QtWidgets.QFrame.HLine)
        self.LPrepMethUseForHor.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LPrepMethUseForHor.setObjectName("LPrepMethUseForHor")
        self.GVBgOnto.raise_()
        self.LClearDataIsVert.raise_()
        self.LPrepVert.raise_()
        self.LClustNext.raise_()
        self.TWDefHide.raise_()
        self.GBActions.raise_()
        self.BReduceDim.raise_()
        self.BNormalize.raise_()
        self.BFilter.raise_()
        self.BLem.raise_()
        self.BStem.raise_()
        self.LReduceUsesHor.raise_()
        self.LNormalizeUseFor.raise_()
        self.LNormalizeIs2.raise_()
        self.LLemUses.raise_()
        self.LFilterUses.raise_()
        self.LStemUses.raise_()
        self.LTokenUses.raise_()
        self.LFilterHor.raise_()
        self.LStopWordsUses.raise_()
        self.LFilterVert.raise_()
        self.LGrammUses.raise_()
        self.LNormalizeAll.raise_()
        self.BPrepMeth.raise_()
        self.LReduceIsVert.raise_()
        self.LPrepMehUseForVert.raise_()
        self.LClearDataIsHor.raise_()
        self.LFilterClear.raise_()
        self.LLemClear.raise_()
        self.LStemClear.raise_()
        self.LNormalizeIs.raise_()
        self.LVectorizeIs.raise_()
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
        self.LbClearIs.raise_()
        self.BStopWord.raise_()
        self.BToken.raise_()
        self.BGramm.raise_()
        self.BClearData.raise_()
        self.BPrep.raise_()
        self.BClust.raise_()
        self.LbClearUses.raise_()
        self.LPrepMethUseForHor.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1079, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.mainWindow = MainWindow
        self.settings = settings
        self.localSettings = settings
        self.openType = openType

        self.initDefDict()
        self.initWndView()
        self.initButtons()
        self.mainWindow.closeEvent = self.closeEvent

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.initTable()

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
        self.LbClearIs.setText(_translate("MainWindow", "isA"))
        self.LbClearUses.setText(_translate("MainWindow", "uses"))

    def initButtons(self):
        # кнопки управления
        self.BSaveInFile.clicked.connect(self.saveSettsInFile)
        self.BLocalSave.clicked.connect(self.saveSettsLocal)
        self.BLoadFromFile.clicked.connect(self.openSettings)
        self.BExit.clicked.connect(self.cancelWnd)

        # определения
        self.BNormalize.clicked.connect(self.openNormalizeDef)
        self.BVectorize.clicked.connect(self.openVectorizeDef)
        self.BPrepMeth.clicked.connect(self.openPrepMethDef)
        self.BReduceDim.clicked.connect(self.openReduceDimDef)
        self.BPrep.clicked.connect(self.openPrepDef)
        self.BClust.clicked.connect(self.openClustDef)
        self.BStem.clicked.connect(self.openStemDef)
        self.BLem.clicked.connect(self.openLemDef)
        self.BFilter.clicked.connect(self.openFilterDef)
        self.BStopWord.clicked.connect(self.openSWDef)
        self.BToken.clicked.connect(self.openTokenDef)
        self.BClearData.clicked.connect(self.openClearDataDef)
        self.BGramm.clicked.connect(self.openNGrammDef)

    def initDefDict(self):
        self.defDict = {
            self.BNormalize: [self.LNormalizeIs,
                              self.LNormalizeAll,
                              self.LNormalizeUseFor,
                              self.LNormalizeIs2,
                              self.LStemUses,
                              self.LLemUses,
                              self.LFilterUses,
                              self.LbNormalizeIs,
                              self.LbNormalizeUseFor,
                              self.LbStemUses,
                              self.LbLemUses,
                              self.LbFilterUses],
            self.BVectorize: [self.LVectorizeIs, self.LbVectorizeIs],
            self.BPrepMeth: [self.LPrepMehUseForVert,
                             self.LPrepMethUseForHor,
                             self.LbPrepMethUseFor,
                             self.LVectorizeIs,
                             self.LbVectorizeIs,
                             self.LNormalizeIs2,
                             self.LbNormalizeIs],
            self.BReduceDim: [self.LReduceIsVert,
                              self.LReduceUsesHor,
                              self.LbReduceIs,
                              self.LNormalizeUseFor,
                              self.LbNormalizeUseFor,
                              self.LbClearUses],
            self.BPrep: [self.LClustNext,
                         self.LbPrepNext,
                         self.LPrepVert,
                         self.LPrepMehUseForVert,
                         self.LPrepMethUseForHor,
                         self.LbPrepMethUseFor,
                         self.LbReduceIs],
            self.BClust: [self.LClustNext, self.LbPrepNext],
            self.BStem: [self.LStemUses,
                         self.LbStemUses,
                         self.LStemClear],
            self.BLem: [self.LLemUses,
                        self.LbLemUses,
                        self.LLemClear],
            self.BClearData: [self.LClearDataIsVert,
                              self.LbClearUses,
                              self.LbClearIs,
                              self.LClearDataIsHor,
                              self.LStemClear,
                              self.LLemClear,
                              self.LFilterClear],
            self.BFilter: [self.LFilterUses,
                           self.LbFilterUses,
                           self.LFilterClear,
                           self.LFilterVert,
                           self.LFilterHor,
                           self.LTokenUses,
                           self.LbTokenUses,
                           self.LStopWordsUses,
                           self.LbStopWordsUses],
            self.BToken: [self.LTokenUses,
                          self.LbTokenUses,
                          self.LGrammUses,
                          self.LbGrammUses],
            self.BGramm: [self.LGrammUses,
                          self.LbGrammUses],
            self.BStopWord: [self.LStopWordsUses,
                             self.LbStopWordsUses]
        }

    def initTable(self):
        self.defs = {'Нормализация текстов': self.BNormalize,
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

        self.TWDefHide.setRowCount(len(self.defs))

        for i, defin in enumerate(self.defs):
            self.TWDefHide.setItem(i, 0, QtWidgets.QTableWidgetItem(defin))

            item = QtWidgets.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            item.setCheckState(QtCore.Qt.Unchecked)

            self.TWDefHide.setItem(i, 1, item)

        self.TWDefHide.cellChanged.connect(self.onCellChanged)
        self.TWDefHide.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def onCellChanged(self, row, column):
        item = self.TWDefHide.item(row, 0)
        itemState = self.TWDefHide.item(row, 1)
        for hideItems in self.defDict[self.defs[item.text()]]:
            if itemState.checkState() == QtCore.Qt.Checked:
                hideItems.hide()
            else:
                hideItems.show()

        if itemState.checkState() == QtCore.Qt.Checked:
            self.defs[item.text()].hide()
        else:
            self.defs[item.text()].show()

        self.checkLPrepVert()
        self.checkLFilter()
        self.checkLClearDataIsHor()
        self.checkLClearDataIsVert()

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self.mainWindow, 'Сохранение настроек', 'Сохранить настройки в сессии?',
                                               QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel, QtWidgets.QMessageBox.Cancel)

        if reply == QtWidgets.QMessageBox.Yes:
            self.saveSettsLocal()
        event.accept()

    def initWndView(self):
        self.BSaveInFile.setEnabled(self.openType == ViewType.EDIT)
        self.BLocalSave.setEnabled(self.openType == ViewType.EDIT)
        self.BLoadFromFile.setEnabled(self.openType == ViewType.EDIT)
        self.BExit.setEnabled(self.openType == ViewType.EDIT)

    def checkLPrepVert(self):
        if self.LbPrepMethUseFor.isHidden() and self.LbReduceIs.isHidden():
            self.LPrepVert.hide()
        else:
            self.LPrepVert.show()

    def checkLFilter(self):
        if self.LbStopWordsUses.isHidden() and self.LbTokenUses.isHidden():
            self.LFilterHor.hide()
            self.LFilterVert.hide()
        else:
            self.LFilterHor.show()
            self.LFilterVert.show()

    def checkLClearDataIsHor(self):
        if self.LFilterClear.isHidden() and self.LLemClear.isHidden() and self.LStemClear.isHidden():
            self.LbClearIs.hide()
            self.LClearDataIsHor.hide()
        else:
            self.LbClearIs.show()
            self.LClearDataIsHor.show()

    def checkLClearDataIsVert(self):
        if (self.LClearDataIsHor.isHidden() and self.LReduceUsesHor.isHidden()) or self.BClearData.isHidden():
            self.LClearDataIsVert.hide()
        else:
            self.LClearDataIsVert.show()

    def saveSettsInFile(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        f_name, _ = QtWidgets.QFileDialog.getSaveFileName(self.mainWindow,
                                                          "Сохранение",
                                                          "../settingsTemplates",
                                                          "Файлы настроек (*.json)",
                                                          options=options)
        if not f_name:
            return

        f_name = f_name if f_name.endswith('.json') else f_name + '.json'

        with open(f_name, "w") as dump:
            self.settings = self.localSettings
            sw = self.settings.sw
            self.mainWindow.prevWindow.CBLangVal.setCurrentIndex(self.settings.lang)
            self.settings.sw = sw
            self.mainWindow.prevWindow.controller.settings = self.settings
            dumpStr = json.dumps(self.settings.__dict__, cls=EnumEncoder)
            dump.write(dumpStr)

    def saveSettsLocal(self):
        self.settings = self.localSettings
        sw = self.settings.sw
        self.mainWindow.prevWindow.CBLangVal.setCurrentIndex(self.settings.lang)
        self.settings.sw = sw
        self.mainWindow.prevWindow.controller.settings = self.settings

    def cancelWnd(self):
        self.localSettings = self.settings
        self.mainWindow.close()

    def openSettings(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        f_name, _ = QtWidgets.QFileDialog.getOpenFileName(self.mainWindow,
                                                          "Выбор файла настроек",
                                                          "../settingsTemplates",
                                                          "Файлы настроек (*.json)",
                                                          options=options)
        if not f_name:
            return

        with open(f_name) as f_set:
            f_text = '\n'.join(f_set.readlines()[:2])
            setts = json.loads(f_text, object_hook=as_enum)
            self.settings = Settings(setts['minWordSize'],
                                     setts['maxDictSize'],
                                     setts['minWordCnt'],
                                     setts['maxWordFq'],
                                     setts['minWordFq'],
                                     setts['useStem'],
                                     setts['useLem'],
                                     setts['pos'],
                                     setts['useSW'],
                                     setts['sw'],
                                     setts['useGramms'],
                                     setts['grammsSize'],
                                     setts['clustCnt'],
                                     setts['maxIters'],
                                     setts['similPers'],
                                     setts['minClustSize'],
                                     setts['lang'],
                                     setts['tokenRe'],
                                     setts['vectMeth'],
                                     setts['clustMeth'],
                                     setts['useTokenFilter'])

            self.localSettings = self.settings

    def openNormalizeDef(self):
        self.normalizeDef = QtWidgets.QMainWindow()
        self.normalizeDef.prevWindow = self
        self.normalizeUI = DefWindow.Ui_DefWindow()
        self.normalizeUI.setupUi(self.normalizeDef, self.localSettings, self.openType, Defins.NORMALIZATION)
        self.normalizeDef.show()

    def openVectorizeDef(self):
        self.vectorizeDef = QtWidgets.QMainWindow()
        self.vectorizeDef.prevWindow = self
        self.vectorizeUI = DefWindow.Ui_DefWindow()
        self.vectorizeUI.setupUi(self.vectorizeDef, self.localSettings, self.openType, Defins.VECTORIZATION)
        self.vectorizeDef.show()

    def openPrepMethDef(self):
        self.prepMethDef = QtWidgets.QMainWindow()
        self.prepMethDef.prevWindow = self
        self.prepMethUI = DefWindow.Ui_DefWindow()
        self.prepMethUI.setupUi(self.prepMethDef, self.localSettings, self.openType, Defins.PREPMETH)
        self.prepMethDef.show()

    def openReduceDimDef(self):
        self.reduceDef = QtWidgets.QMainWindow()
        self.reduceDef.prevWindow = self
        self.reduceUI = DefWindow.Ui_DefWindow()
        self.reduceUI.setupUi(self.reduceDef, self.localSettings, self.openType, Defins.REDUCEDIM)
        self.reduceDef.show()

    def openPrepDef(self):
        self.prepDef = QtWidgets.QMainWindow()
        self.prepDef.prevWindow = self
        self.prepUI = DefWindow.Ui_DefWindow()
        self.prepUI.setupUi(self.prepDef, self.localSettings, self.openType, Defins.PREP)
        self.prepDef.show()

    def openClustDef(self):
        self.clustDef = QtWidgets.QMainWindow()
        self.clustDef.prevWindow = self
        self.clustUI = DefWindow.Ui_DefWindow()
        self.clustUI.setupUi(self.clustDef, self.localSettings, self.openType, Defins.CLUST)
        self.clustDef.show()

    def openStemDef(self):
        self.stemDef = QtWidgets.QMainWindow()
        self.stemDef.prevWindow = self
        self.stemUI = DefWindow.Ui_DefWindow()
        self.stemUI.setupUi(self.stemDef, self.localSettings, self.openType, Defins.STEM)
        self.stemDef.show()

    def openLemDef(self):
        self.lemDef = QtWidgets.QMainWindow()
        self.lemDef.prevWindow = self
        self.lemUI = DefWindow.Ui_DefWindow()
        self.lemUI.setupUi(self.lemDef, self.localSettings, self.openType, Defins.LEM)
        self.lemDef.show()

    def openFilterDef(self):
        self.filterDef = QtWidgets.QMainWindow()
        self.filterDef.prevWindow = self
        self.filterUI = DefWindow.Ui_DefWindow()
        self.filterUI.setupUi(self.filterDef, self.localSettings, self.openType, Defins.FILTER)
        self.filterDef.show()

    def openSWDef(self):
        self.swDef = QtWidgets.QMainWindow()
        self.swDef.prevWindow = self
        self.swUI = DefWindow.Ui_DefWindow()
        self.swUI.setupUi(self.swDef, self.localSettings, self.openType, Defins.SW)
        self.swDef.show()

    def openTokenDef(self):
        self.tokenDef = QtWidgets.QMainWindow()
        self.tokenDef.prevWindow = self
        self.tokeneUI = DefWindow.Ui_DefWindow()
        self.tokeneUI.setupUi(self.tokenDef, self.localSettings, self.openType, Defins.TOKEN)
        self.tokenDef.show()

    def openClearDataDef(self):
        self.clearDataDef = QtWidgets.QMainWindow()
        self.clearDataDef.prevWindow = self
        self.clearDataUI = DefWindow.Ui_DefWindow()
        self.clearDataUI.setupUi(self.clearDataDef, self.localSettings, self.openType, Defins.CLEARDATA)
        self.clearDataDef.show()

    def openNGrammDef(self):
        self.nGrammDef = QtWidgets.QMainWindow()
        self.nGrammDef.prevWindow = self
        self.nGrammUI = DefWindow.Ui_DefWindow()
        self.nGrammUI.setupUi(self.nGrammDef, self.localSettings, self.openType, Defins.NGRAMM)
        self.nGrammDef.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

