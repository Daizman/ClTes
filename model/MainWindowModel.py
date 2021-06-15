from model.Metrix import Metrix
from model.Settings import Settings
from model.LangVectorize import LangVectorize
from model.Clust import Clust

from PyQt5 import QtWidgets
from view.OntoWindow import Ui_MainWindow

from model.mixins.JsonEnumExtention import *

import matplotlib.pyplot as plt

import numpy as np
import os
import datetime
from time import time
from nltk.corpus import stopwords as nltk_sw
from sklearn import metrics
from sklearn.datasets import fetch_20newsgroups


class MainWindowModel:
    def __init__(self, me, meWnd):
        self.settings = Settings()
        self.metrix = Metrix()
        self.__me = me
        self.__meWnd = meWnd
        self.__userTexts = []
        self.__dirToAnswer = ""
        self.__x = []
        self.__km = None
        self.__labels = []
        self.__userF = None
        self.__corporaType = None
        self.__changeSetWnd = None
        self.__changeSetUI = None

    def openSettigns(self, fName):
        if not fName:
            return

        with open(fName) as f_set:
            fText = '\n'.join(f_set.readlines()[:2])
            setts = json.loads(fText, object_hook=as_enum)
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

    def changeSettings(self):
        if not self.__changeSetWnd:
            self.__initOntoWnd()

        if self.settings.lang != self.__me.CBLangVal.currentData():
            self.settings.lang = self.__me.CBLangVal.currentData()
            self.settings.sw = nltk_sw.words('russian') if self.settings.lang == Lang.RUS else nltk_sw.words('english')

        self.settings.lang = self.__me.CBLangVal.currentData()
        self.__changeSetUI.setupUi(self.__changeSetWnd, self.settings, ViewType.EDIT)
        self.__changeSetWnd.show()

    def viewSettings(self):
        if not self.__changeSetWnd:
            self.__initOntoWnd()

        if self.settings.lang != self.__me.CBLangVal.currentData():
            self.settings.lang = self.__me.CBLangVal.currentData()
            self.settings.sw = nltk_sw.words('russian') if self.settings.lang == Lang.RUS else nltk_sw.words('english')

        self.__changeSetUI.setupUi(self.__changeSetWnd, self.settings, ViewType.VIEW)
        self.__changeSetWnd.show()

    def __initOntoWnd(self):
        self.__changeSetWnd = QtWidgets.QMainWindow()
        self.__changeSetUI = Ui_MainWindow()
        self.__changeSetWnd.prevWindow = self.__me

    def clust(self):
        self.initDataset()

        self.settings.lang = self.__me.CBLangVal.currentData()

        t0 = time()
        self.vectorize()
        if self.settings.clustMeth == ClusterizationType.KMEANS:
            km = Clust.kMeans(self.settings.clustCnt, self.settings.maxIters, self.__x)
        elif self.settings.clustMeth == ClusterizationType.MINIBATCH_KMEANS:
            km = Clust.miniBatch(self.settings.clustCnt, self.settings.maxIters, self.__x)
        elif self.settings.clustMeth == ClusterizationType.BIRCH:
            km = Clust.birch(self.settings.clustCnt, self.settings.similPers, self.__x)
        elif self.settings.clustMeth == ClusterizationType.AGGLOMERATIVE:
            km = Clust.agglomerative(self.settings.clustCnt, self.__x)
        else:
            km = Clust.spectral(self.settings.clustCnt, self.settings.minClustSize, self.__x)
        km.fit(self.__x)
        self.__km = km
        self.metrix.time = time() - t0

    def calcMetrix(self):
        self.metrix.homogen = metrics.homogeneity_score(self.__labels, self.__km.labels_)
        self.metrix.completeness = metrics.completeness_score(self.__labels, self.__km.labels_)
        self.metrix.vMeas = metrics.v_measure_score(self.__labels, self.__km.labels_)

    def saveMetrix(self):
        if not os.path.exists(os.pardir + '/metricRes'):
            os.mkdir(os.pardir + '/metricRes')
        fName = os.pardir + '/metricRes/setup_' \
                + str(self.settings.lang) + '_' \
                + str(self.__me.CBCorpVal.currentData()) + '_' \
                + str(self.settings.vectMeth) + '_' \
                + str(self.settings.clustMeth) + '_' \
                + str(datetime.datetime.now()).replace(' ', '_').replace(':', '_').replace('-', '_') + '.txt'

        with open(fName, 'w') as metrSave:
            metrSave.write("Однородность: %0.3f\n" % self.metrix.homogen)
            metrSave.write("Полнота: %0.3f\n" % self.metrix.completeness)
            metrSave.write("V-мера: %0.3f\n" % self.metrix.vMeas)
            metrSave.write("Время работы: %0.1f с.\n\n\nНастройки:\n" % self.metrix.time)

            metrSave.write(str(self.settings))

    def sortUserFiles(self):
        for i, f in enumerate(self.__userF):
            fLocal = f[f.rfind('/'):]
            os.rename(f, self.__dirToAnswer + '/%i' % self.__km.labels_[i] + fLocal)

    def vectorize(self):
        vectorizer = LangVectorize(self.settings)
        if self.settings.vectMeth == VectorizationType.TF:
            self.__x = vectorizer.tf(self.__userTexts)
        elif self.settings.vectMeth == VectorizationType.TFIDF:
            self.__x = vectorizer.tfidf(self.__userTexts)
        elif self.settings.vectMeth == VectorizationType.HASH:
            self.__x = vectorizer.hash(self.__userTexts)
        elif self.settings.vectMeth == VectorizationType.ONEHOT:
            self.__x = vectorizer.oh(self.__userTexts)
        else:
            self.__x = vectorizer.distribution(self.__userTexts)

    def createPlots(self):
        plt.rcParams["figure.figsize"] = (10, 8)
        fig, (ax1, ax2) = plt.subplots(2, sharex=True)
        fig.suptitle('Сравнение распределения документов по кластерам')
        clusters = [i for i in range(self.settings.clustCnt)]
        orig_distr = []
        pred_distr = []
        for i in range(self.settings.clustCnt):
            pred_i = np.where(self.__km.labels_ == i)[0].size
            orig_i = np.where(self.__labels == i)[0].size
            orig_distr.append(orig_i)
            pred_distr.append(pred_i)
        ax1.plot(clusters, orig_distr, 'o')
        ax2.plot(clusters, pred_distr, '*')
        ax1.grid()
        ax2.grid()
        plt.xticks(np.arange(0, self.settings.clustCnt))
        ax1.set_title('Оригинальное распределение документов по кластерам')
        ax2.set_title('Предсказанное распределение документов по кластерам')
        fig.show()

    def initDataset(self):
        corp = self.__me.CBCorpVal.currentData()
        if corp == Corpora.NEWS:
            categories = ['alt.atheism',
                          'comp.graphics',
                          'comp.os.ms-windows.misc',
                          'comp.sys.ibm.pc.hardware',
                          'comp.sys.mac.hardware',
                          'comp.windows.x',
                          'misc.forsale',
                          'rec.autos',
                          'rec.motorcycles',
                          'rec.sport.baseball',
                          'rec.sport.hockey',
                          'sci.crypt',
                          'sci.electronics',
                          'sci.med',
                          'sci.space',
                          'soc.religion.christian',
                          'talk.politics.guns',
                          'talk.politics.mideast',
                          'talk.politics.misc',
                          'talk.religion.misc']
            barier = self.settings.clustCnt if self.settings.clustCnt <= 20 else 20
            dataset = fetch_20newsgroups(subset='all', categories=categories[:barier], shuffle=True, random_state=42)
            self.__labels = dataset.target
            # self.true_k = np.unique(self.__labels).shape[0]
            self.__userTexts = dataset.data
        elif corp == Corpora.USER:
            self.__dirToAnswer = self.__userF[0][:self.__userF[0].rfind('/')] + '/answerClusts'
            if not os.path.exists(self.__dirToAnswer):
                os.mkdir(self.__dirToAnswer)
            for i in range(self.settings.clustCnt):
                if not os.path.exists(self.__dirToAnswer + '/%i' % i):
                    os.mkdir(self.__dirToAnswer + '/%i' % i)
        elif corp == Corpora.RUWIKI:
            pass
        elif corp == Corpora.ENGWIKI:
            pass
        else:
            pass

    def setUserTexts(self, uTexts):
        self.__userTexts = uTexts

    def setUserFNames(self, fNames):
        self.__userF = fNames
