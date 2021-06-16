from model.MainWindowModel import MainWindowModel

from model.enums.Corpora import Corpora


class MainWindowController:
    def __init__(self):
        self.__model = MainWindowModel()

    def openSettings(self, fName, lang):
        if not fName:
            return
        self.__model.openSettigns(fName, lang)

    def setupLangAndSw(self, lang):
        self.__model.setupLangAndSw(lang)

    def getSettings(self):
        return self.__model.settings

    def clust(self, wndData):
        self.__model.clust(wndData)

        if wndData['Corpora'] != Corpora.USER:
            self.__model.calcMetrix()
            self.__model.saveMetrix(wndData['Corpora'])
        else:
            self.__model.sortUserFiles()

        return self.__model.metrix

    def createPlots(self):
        self.__model.createPlots()

    def setUserTexts(self, uTexts):
        self.__model.setUserTexts(uTexts)

    def setUserFNames(self, fNames):
        self.__model.setUserFNames(fNames)
