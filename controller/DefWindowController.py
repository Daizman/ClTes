from model.DefWindowModel import DefWindowModel


class DefWindowController:
    def __init__(self, settings):
        self.__model = DefWindowModel(settings)

    def getSettings(self):
        return self.__model.settings

    def setSettings(self, settings):
        self.__model.settings = settings

    def saveParam(self, wndData):
        pass
