import json
from model.Settings import Settings
from PyQt5 import QtWidgets
from view.OntoWindow import Ui_MainWindow
from model.mixins.JsonEnumExtention import *


class MainWindowController:
    def __init__(self, me, mainWindow, settings):
        self.me = me
        self.mainWindow = mainWindow
        self.settings = settings
        self.changeSetWnd = None

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

    def changeSettings(self):
        if not self.changeSetWnd:
            self.initOntoWnd()
        self.changeSetUI.setupUi(self.changeSetWnd, self.settings, ViewType.EDIT)
        self.changeSetWnd.show()

    def viewSettings(self):
        if not self.changeSetWnd:
            self.initOntoWnd()
        self.changeSetUI.setupUi(self.changeSetWnd, self.settings, ViewType.VIEW)
        self.changeSetWnd.show()

    def clust(self):
        pass

    def createPlots(self):
        pass

    def calcMetrix(self):
        pass

    def initOntoWnd(self):
        self.changeSetWnd = QtWidgets.QMainWindow()
        self.changeSetUI = Ui_MainWindow()
        self.changeSetWnd.prevWindow = self.me
