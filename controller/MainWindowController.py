from model.MainWindowModel import MainWindowModel

from PyQt5 import QtWidgets

from model.enums.Corpora import Corpora


class MainWindowController:
    def __init__(self, me, meWnd):
        self.__me = me
        self.__meWnd = meWnd
        self.__model = MainWindowModel(me, meWnd)

    def openSettings(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fName, _ = QtWidgets.QFileDialog.getOpenFileName(self.__meWnd,
                                                         "Выбор файла настроек",
                                                         "../settingsTemplates",
                                                         "Файлы настроек (*.json)",
                                                         options=options)
        self.__model.openSettigns(fName)
        self.__me.CBLangVal.setCurrentIndex(self.__me.CBLangVal.findData(self.__model.settings.lang))

    def changeSettings(self):
        self.__model.changeSettings()

    def viewSettings(self):
        self.__model.viewSettings()

    def clust(self):
        try:
            self.__model.clust()
        except MemoryError as e:
            error = QtWidgets.QErrorMessage(self.__meWnd)
            error.setWindowTitle("Ошибка.")
            error.showMessage("Недостаточно памяти.")
        except BaseException as e:
            error = QtWidgets.QErrorMessage(self.__meWnd)
            error.setWindowTitle("Ошибка.")
            error.showMessage(str(e))

        self.__me.LWTimeVal.setText("Время работы: %0.1f с." % self.__model.metrix.time)
        if self.__me.CBCorpVal.currentData() != Corpora.USER:
            self.__model.calcMetrix()
            self.__me.LHomogenVal.setText("Однородность: %0.3f" % self.__model.metrix.homogen)
            self.__me.LCompletenessVal.setText("Полнота: %0.3f" % self.__model.metrix.completeness)
            self.__me.LVMeasVal.setText("V-мера: %0.3f" % self.__model.metrix.vMeas)
            self.__me.BGetPlots.setEnabled(True)
            self.__model.saveMetrix()
        else:
            self.__model.sortUserFiles()

    def createPlots(self):
        self.__model.createPlots()

    def setUserTexts(self, uTexts):
        self.__model.setUserTexts(uTexts)

    def setUserFNames(self, fNames):
        self.__model.setUserFNames(fNames)
