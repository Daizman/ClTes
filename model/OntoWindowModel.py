from model.mixins.JsonEnumExtention import *
from model.Settings import Settings


class OntoWindowModel:
    def __init__(self, settings):
        """
        :param settings: view localSettings
        """
        self.settings = settings

    def saveSettsInFile(self, fName):
        with open(fName, "w") as dump:
            dumpStr = json.dumps(self.settings.__dict__, cls=EnumEncoder)
            dump.write(dumpStr)

    def openSetts(self, fName):
        with open(fName) as f_set:
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
                                     setts['vectMeth'],
                                     setts['clustMeth'],
                                     setts['useTokenFilter'],
                                     setts['distrEpoch'])
