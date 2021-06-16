from model.OntoWindowModel import OntoWindowModel


class OntoWindowController:
    def __init__(self, settings):
        self.__model = OntoWindowModel(settings)

    def saveSettsInFile(self, fName):
        if not fName:
            return
        fName = fName if fName.endswith('.json') else fName + '.json'
        self.__model.saveSettsInFile(fName)

    def openSetts(self, fName):
        if not fName:
            return
        self.__model.openSetts(fName)
        return self.__model.settings

    def getSettings(self):
        return self.__model.settings

    def setSettings(self, settings):
        self.__model.settings = settings
