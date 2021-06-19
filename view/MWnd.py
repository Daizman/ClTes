from PyQt5 import QtCore, QtGui, QtWidgets
from model.enums.Lang import Lang
from model.enums.Corpora import Corpora
from controller.MainWindowController import MainWindowController
import view.OntoWindow

import textract


class Ui_MWnd(object):
    def setupUi(self, MWnd):
        MWnd.setObjectName("MWnd")
        MWnd.resize(677, 260)
        self.WMain = QtWidgets.QWidget(MWnd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WMain.sizePolicy().hasHeightForWidth())
        self.WMain.setSizePolicy(sizePolicy)
        self.WMain.setObjectName("WMain")
        self.gridLayout = QtWidgets.QGridLayout(self.WMain)
        self.gridLayout.setObjectName("gridLayout")
        self.GLMain = QtWidgets.QGridLayout()
        self.GLMain.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.GLMain.setObjectName("GLMain")
        self.GBInputData = QtWidgets.QGroupBox(self.WMain)
        self.GBInputData.setObjectName("GBInputData")
        self.formLayout = QtWidgets.QFormLayout(self.GBInputData)
        self.formLayout.setObjectName("formLayout")
        self.LLang = QtWidgets.QLabel(self.GBInputData)
        self.LLang.setObjectName("LLang")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.LLang)
        self.CBLangVal = QtWidgets.QComboBox(self.GBInputData)
        self.CBLangVal.setObjectName("CBLangVal")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.CBLangVal)
        self.LCorp = QtWidgets.QLabel(self.GBInputData)
        self.LCorp.setObjectName("LCorp")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.LCorp)
        self.CBCorpVal = QtWidgets.QComboBox(self.GBInputData)
        self.CBCorpVal.setObjectName("CBCorpVal")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.CBCorpVal)
        self.GLMain.addWidget(self.GBInputData, 0, 0, 1, 1)
        self.GLOntoSet = QtWidgets.QGridLayout()
        self.GLOntoSet.setObjectName("GLOntoSet")
        self.BOpenSet = QtWidgets.QPushButton(self.WMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BOpenSet.sizePolicy().hasHeightForWidth())
        self.BOpenSet.setSizePolicy(sizePolicy)
        self.BOpenSet.setObjectName("BOpenSet")
        self.GLOntoSet.addWidget(self.BOpenSet, 0, 0, 1, 1)
        self.BEditSet = QtWidgets.QPushButton(self.WMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BEditSet.sizePolicy().hasHeightForWidth())
        self.BEditSet.setSizePolicy(sizePolicy)
        self.BEditSet.setObjectName("BEditSet")
        self.GLOntoSet.addWidget(self.BEditSet, 1, 0, 1, 1)
        self.BViewOnto = QtWidgets.QPushButton(self.WMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BViewOnto.sizePolicy().hasHeightForWidth())
        self.BViewOnto.setSizePolicy(sizePolicy)
        self.BViewOnto.setObjectName("BViewOnto")
        self.GLOntoSet.addWidget(self.BViewOnto, 2, 0, 1, 1)
        self.GLMain.addLayout(self.GLOntoSet, 1, 0, 2, 1)
        self.GLRCol = QtWidgets.QGridLayout()
        self.GLRCol.setObjectName("GLRCol")
        self.GBMetr = QtWidgets.QGroupBox(self.WMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GBMetr.sizePolicy().hasHeightForWidth())
        self.GBMetr.setSizePolicy(sizePolicy)
        self.GBMetr.setObjectName("GBMetr")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.GBMetr)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.GLMetr = QtWidgets.QGridLayout()
        self.GLMetr.setObjectName("GLMetr")
        self.LHomogen = QtWidgets.QLabel(self.GBMetr)
        self.LHomogen.setObjectName("LHomogen")
        self.GLMetr.addWidget(self.LHomogen, 0, 0, 1, 1)
        self.LHomogenVal = QtWidgets.QLabel(self.GBMetr)
        self.LHomogenVal.setObjectName("LHomogenVal")
        self.GLMetr.addWidget(self.LHomogenVal, 0, 1, 1, 1)
        self.LCompleteness = QtWidgets.QLabel(self.GBMetr)
        self.LCompleteness.setObjectName("LCompleteness")
        self.GLMetr.addWidget(self.LCompleteness, 1, 0, 1, 1)
        self.LCompletenessVal = QtWidgets.QLabel(self.GBMetr)
        self.LCompletenessVal.setObjectName("LCompletenessVal")
        self.GLMetr.addWidget(self.LCompletenessVal, 1, 1, 1, 1)

        self.LDaviesBouldin = QtWidgets.QLabel(self.GBMetr)
        self.LDaviesBouldin.setObjectName("LDaviesBouldin")
        self.GLMetr.addWidget(self.LDaviesBouldin, 4, 0, 1, 1)
        self.LDaviesBouldinVal = QtWidgets.QLabel(self.GBMetr)
        self.LDaviesBouldinVal.setObjectName("LDaviesBouldinVal")
        self.GLMetr.addWidget(self.LDaviesBouldinVal, 4, 1, 1, 1)

        self.LSilhouette = QtWidgets.QLabel(self.GBMetr)
        self.LSilhouette.setObjectName("LSilhouette")
        self.GLMetr.addWidget(self.LSilhouette, 5, 0, 1, 1)
        self.LSilhouetteVal = QtWidgets.QLabel(self.GBMetr)
        self.LSilhouetteVal.setObjectName("LSilhouetteVal")
        self.GLMetr.addWidget(self.LSilhouetteVal, 5, 1, 1, 1)

        self.LCalinski = QtWidgets.QLabel(self.GBMetr)
        self.LCalinski.setObjectName("LCalinski")
        self.GLMetr.addWidget(self.LCalinski, 6, 0, 1, 1)
        self.LCalinskiVal = QtWidgets.QLabel(self.GBMetr)
        self.LCalinskiVal.setObjectName("LCalinskiVal")
        self.GLMetr.addWidget(self.LCalinskiVal, 6, 1, 1, 1)

        self.LVMeas = QtWidgets.QLabel(self.GBMetr)
        self.LVMeas.setObjectName("LVMeas")
        self.GLMetr.addWidget(self.LVMeas, 2, 0, 1, 1)
        self.LVMeasVal = QtWidgets.QLabel(self.GBMetr)
        self.LVMeasVal.setObjectName("LVMeasVal")
        self.GLMetr.addWidget(self.LVMeasVal, 2, 1, 1, 1)
        self.LWTime = QtWidgets.QLabel(self.GBMetr)
        self.LWTime.setObjectName("LWTime")
        self.GLMetr.addWidget(self.LWTime, 3, 0, 1, 1)
        self.LWTimeVal = QtWidgets.QLabel(self.GBMetr)
        self.LWTimeVal.setObjectName("LWTimeVal")
        self.GLMetr.addWidget(self.LWTimeVal, 3, 1, 1, 1)
        self.gridLayout_2.addLayout(self.GLMetr, 0, 0, 1, 1)
        self.GLRCol.addWidget(self.GBMetr, 0, 0, 1, 1)
        self.BGetPlots = QtWidgets.QPushButton(self.WMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BGetPlots.sizePolicy().hasHeightForWidth())
        self.BGetPlots.setSizePolicy(sizePolicy)
        self.BGetPlots.setObjectName("BGetPlots")
        self.BGetPlots.setEnabled(False)
        self.GLRCol.addWidget(self.BGetPlots, 1, 0, 1, 1)
        self.BClust = QtWidgets.QPushButton(self.WMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BClust.sizePolicy().hasHeightForWidth())
        self.BClust.setSizePolicy(sizePolicy)
        self.BClust.setObjectName("BClust")
        self.GLRCol.addWidget(self.BClust, 2, 0, 1, 1)
        self.GLMain.addLayout(self.GLRCol, 0, 1, 3, 1)
        self.gridLayout.addLayout(self.GLMain, 0, 0, 1, 1)
        MWnd.setCentralWidget(self.WMain)
        self.menubar = QtWidgets.QMenuBar(MWnd)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 477, 21))
        self.menubar.setObjectName("menubar")
        MWnd.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MWnd)
        self.statusbar.setObjectName("statusbar")
        MWnd.setStatusBar(self.statusbar)

        self.__meWnd = MWnd
        self.__controller = MainWindowController()
        self.__changeSetWnd = None

        self.initCombos()
        self.initButtons()

        self.retranslateUi(MWnd)
        QtCore.QMetaObject.connectSlotsByName(MWnd)

    def retranslateUi(self, MWnd):
        _translate = QtCore.QCoreApplication.translate
        MWnd.setWindowTitle(_translate("MWnd", "Кластеризация"))
        self.GBInputData.setTitle(_translate("MWnd", "Входные данные"))
        self.LLang.setText(_translate("MWnd", "Язык:"))
        self.LCorp.setText(_translate("MWnd", "Корпус:"))
        self.BOpenSet.setText(_translate("MWnd", "Открыть настройки"))
        self.BEditSet.setText(_translate("MWnd", "Изменить настройки"))
        self.BViewOnto.setText(_translate("MWnd", "Просмотр онтологии"))
        self.GBMetr.setTitle(_translate("MWnd", "Метрики"))
        self.LHomogen.setText(_translate("MWnd", "Однородность:"))
        self.LHomogenVal.setText(_translate("MWnd", ""))
        self.LCompleteness.setText(_translate("MWnd", "Полнота:"))
        self.LCompletenessVal.setText(_translate("MWnd", ""))
        self.LDaviesBouldin.setText(_translate("MWnd", "Индекс Болдуина:"))
        self.LDaviesBouldinVal.setText(_translate("MWnd", ""))
        self.LSilhouette.setText(_translate("MWnd", "Силуэт:"))
        self.LSilhouetteVal.setText(_translate("MWnd", ""))
        self.LCalinski.setText(_translate("MWnd", "Индекс Calinski:"))
        self.LCalinskiVal.setText(_translate("MWnd", ""))
        self.LVMeas.setText(_translate("MWnd", "V-мера:"))
        self.LVMeasVal.setText(_translate("MWnd", ""))
        self.LWTime.setText(_translate("MWnd", "Время кластеризации:"))
        self.LWTimeVal.setText(_translate("MWnd", ""))
        self.BGetPlots.setText(_translate("MWnd", "Получить графики"))
        self.BClust.setText(_translate("MWnd", "Кластеризация"))

    def initCombos(self):
        self.CBLangVal.addItem('Русский', userData=Lang.RUS)
        self.CBLangVal.addItem('Английский', userData=Lang.ENG)

        self.CBLangVal.currentTextChanged.connect(self.changeLangCombo)

        self.CBCorpVal.addItem('OpenCorpora', Corpora.OPENCORPORA)
        self.CBCorpVal.addItem('WIKIPEDIA MONOLINGUAL CORPORA', Corpora.RUWIKI)
        self.CBCorpVal.addItem('Выбрать на компьютере', Corpora.USER)

        self.CBCorpVal.currentTextChanged.connect(self.chandeCorpCombo)

    def changeLangCombo(self):
        self.CBCorpVal.clear()

        if self.CBLangVal.currentData() == Lang.RUS:
            self.CBCorpVal.addItem('OpenCorpora', Corpora.OPENCORPORA)
            self.CBCorpVal.addItem('WIKIPEDIA MONOLINGUAL CORPORA', Corpora.RUWIKI)
            self.CBCorpVal.addItem('Выбрать на компьютере', Corpora.USER)
        else:
            self.CBCorpVal.addItem('The 20 Newsgroups data set', Corpora.NEWS)
            self.CBCorpVal.addItem('WIKIPEDIA MONOLINGUAL CORPORA', Corpora.ENGWIKI)
            self.CBCorpVal.addItem('Выбрать на компьютере', Corpora.USER)

    def chandeCorpCombo(self):
        if self.CBCorpVal.currentData() == Corpora.USER:
            options = QtWidgets.QFileDialog.Options()
            options |= QtWidgets.QFileDialog.DontUseNativeDialog
            fNames, _ = QtWidgets.QFileDialog.getOpenFileNames(self.__meWnd,
                                                                "Выбор файлов",
                                                                "../../",
                                                                "Файлы документов (*.txt, *.doc, *.docx);;Все файлы (*)",
                                                                options=options)
            if not fNames:
                return

            try:
                uTexts = []
                for f in fNames:
                    if f.endswith((".doc", ".docx")):
                        uTexts.append(textract.process(f))
                    elif f.endswith(".txt"):
                        uTexts.append(''.join(open(f)))
                self.__controller.setUserTexts(uTexts)
                self.__controller.setUserFNames(fNames)
            except:
                error = QtWidgets.QErrorMessage(self.__meWnd)
                error.setWindowTitle("Предупреждение.")
                error.showMessage("Ошибка в имени одного из файлов")

    def initButtons(self):
        self.BClust.clicked.connect(self.__clust)
        self.BOpenSet.clicked.connect(self.__openSettings)
        self.BEditSet.clicked.connect(self.__changeSettings)
        self.BViewOnto.clicked.connect(self.__viewSettings)
        self.BGetPlots.clicked.connect(self.__controller.createPlots)

    def __openSettings(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fName, _ = QtWidgets.QFileDialog.getOpenFileName(self.__meWnd,
                                                         "Выбор файла настроек",
                                                         "../settingsTemplates",
                                                         "Файлы настроек (*.json)",
                                                         options=options)
        self.__controller.setupLangAndSw(self.CBLangVal.currentData())
        self.__controller.openSettings(fName, self.CBLangVal.currentData())
        self.CBLangVal.setCurrentIndex(self.CBLangVal.findData(self.__controller.getSettings().lang))

    def __initOntoWnd(self):
        self.__changeSetWnd = QtWidgets.QMainWindow()
        self.__changeSetWnd.prevWindow = self
        self.__changeSetUI = view.OntoWindow.Ui_MainWindow()

    def __changeSettings(self):
        if not self.__changeSetWnd:
            self.__initOntoWnd()
        self.__controller.setupLangAndSw(self.CBLangVal.currentData())
        self.__changeSetUI.setupUi(self.__changeSetWnd, self.__controller.getSettings(), view.OntoWindow.ViewType.EDIT)
        self.__changeSetWnd.show()

    def __viewSettings(self):
        if not self.__changeSetWnd:
            self.__initOntoWnd()
        self.__controller.setupLangAndSw(self.CBLangVal.currentData())
        self.__changeSetUI.setupUi(self.__changeSetWnd, self.__controller.getSettings(), view.OntoWindow.ViewType.VIEW)
        self.__changeSetWnd.show()

    def setSettings(self, settings):
        self.__controller.setSettings(settings)
        self.CBLangVal.setCurrentIndex(self.CBLangVal.findData(settings.lang))

    def __clust(self):
        try:
            wndData = {
                "Corpora": self.CBCorpVal.currentData(),
                "Lang": self.CBLangVal.currentData()
            }
            metrix = self.__controller.clust(wndData)
            if metrix:
                if wndData['Corpora'] != Corpora.USER:
                    self.LHomogenVal.setText("Однородность: %0.3f" % metrix.homogen)
                    self.LCompletenessVal.setText("Полнота: %0.3f" % metrix.completeness)
                    self.LVMeasVal.setText("V-мера: %0.3f" % metrix.vMeas)
                    self.BGetPlots.setEnabled(True)
                self.LWTimeVal.setText("Время работы: %0.1f с." % metrix.time)
                self.LDaviesBouldinVal.setText("Индекс Болдуина: %0.3f" % metrix.daviesBouldin)
                self.LSilhouetteVal.setText("Силуэт: %0.3f" % metrix.silhouette)
                self.LCalinskiVal.setText("Индекс Calinski: %0.3f" % metrix.calinski)

        except MemoryError as e:
            error = QtWidgets.QErrorMessage(self.__meWnd)
            error.setWindowTitle("Ошибка.")
            error.showMessage("Недостаточно памяти.")
        except BaseException as e:
            error = QtWidgets.QErrorMessage(self.__meWnd)
            error.setWindowTitle("Ошибка.")
            error.showMessage(str(e))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MWnd = QtWidgets.QMainWindow()
    ui = Ui_MWnd()
    ui.setupUi(MWnd)
    MWnd.show()
    sys.exit(app.exec_())

