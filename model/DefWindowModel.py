from model.enums.Defins import Defins
from model.enums.ClusterizationType import ClusterizationType
from model.enums.VectorizationType import VectorizationType


class DefWindowModel:
    def __init__(self, settings):
        self.settings = settings

    def saveParam(self, wndData):
        if wndData["Defin"] == Defins.VECTORIZATION:
            self.settings.vectMeth = wndData["CBVal"]
            if self.settings.vectMeth == VectorizationType.DISTR:
                self.settings.distrEpoch = int(wndData["LEVal2"])

        if wndData["Defin"] == Defins.CLUST:
            self.settings.clustMeth = wndData["CBVal"]
            self.settings.clustCnt = int(wndData["LEVal"])

            if self.settings.clustMeth == ClusterizationType.KMEANS or self.settings.clustMeth == ClusterizationType.MINIBATCH_KMEANS:
                self.settings.maxIters = int(wndData["LEVal2"])
            elif self.settings.clustMeth == ClusterizationType.BIRCH:
                self.settings.similPers = float(wndData["LEVal2"])
                if self.settings.similPers > 1:
                    raise BaseException("Максимальная кластеров должна быть меньше или равна 1")

            elif self.settings.similPers == ClusterizationType.SPECTRAL:
                self.settings.minClustSize = int(wndData["LEVal2"])

        if wndData["Defin"] == Defins.LEM:
            self.settings.useLem = wndData["CBUse"]
            self.settings.pos = wndData["CBVal"]

        if wndData["Defin"] == Defins.STEM:
            self.settings.useStem = wndData["CBUse"]

        if wndData["Defin"] == Defins.TOKEN:
            self.settings.useTokenFilter = wndData["CBUse"]
            self.settings.maxWordFq = float(wndData["LEVal3"])
            if self.settings.maxWordFq > 1:
                raise BaseException("Максимальная частота слова должна быть меньше или равна 1")
            self.settings.minWordCnt = int(wndData["LEVal2"])
            self.settings.maxDictSize = int(wndData["LEVal"])

        if wndData["Defin"] == Defins.SW:
            self.settings.useSW = wndData["CBUse"]
            for word in wndData["newSW"]:
                self.settings.sw.append(word)
            for word in wndData["removeSW"]:
                if word in self.settings.sw:
                    self.settings.sw.remove(word)

        if wndData["Defin"] == Defins.NGRAMM:
            self.settings.useGramms = wndData["CBUse"]
            self.settings.grammsSize = int(wndData["LEVal"])
