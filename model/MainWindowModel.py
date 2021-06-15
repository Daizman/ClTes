from model.Metrix import Metrix
from model.Settings import Settings
from model.LangVectorize import LangVectorize
from model.Clust import Clust
from model.enums.ViewType import ViewType


class MainWindowModel:
    def __init__(self, settings, metrix, me, meWnd):
        self.settings = settings
        self.metrix = metrix
        self.__me = me
        self.__meWnd = meWnd

    def openSettigns(self):
        pass

    def changeSettings(self):
        pass

    def viewSettings(self):
        pass

    def clust(self):
        pass

    def calcMatrix(self):
        pass

    def saveMetrix(self):
        pass

    def vectorize(self):
        pass

    def createPlots(self):
        pass

    def initDataset(self):
        pass
