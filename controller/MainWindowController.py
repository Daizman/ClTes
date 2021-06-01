from model.Settings import Settings
from PyQt5 import QtWidgets
from view.OntoWindow import Ui_MainWindow
from model.mixins.JsonEnumExtention import *
from sklearn.datasets import fetch_20newsgroups
import numpy as np
from time import time
from model.LangVectorize import LangVectorize
from model.Clust import Clust
from sklearn import metrics
import matplotlib.pyplot as plt
import matplotlib.colors as plt_colors


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
            sw = self.settings.sw
            self.me.CBLangVal.setCurrentIndex(self.me.CBLangVal.findData(self.settings.lang))
            self.settings.sw = sw

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
        if self.me.CBCorpVal.currentText() == 'The 20 Newsgroups data set':
            self.clustNewsgroup()

    def clustNewsgroup(self):
        t0 = time()
        self.initNewsgroup()
        self.vectorize()
        if self.settings.clustMeth == ClusterizationType.KMEANS:
            km = Clust.kMeans(self.settings.clustCnt, self.settings.maxIters, self.x)
        elif self.settings.clustMeth == ClusterizationType.MINIBATCH_KMEANS:
            km = Clust.miniBatch(self.settings.clustCnt, self.settings.maxIters, self.x)
        elif self.settings.clustMeth == ClusterizationType.BIRCH:
            km = Clust.birch(self.settings.clustCnt, self.settings.similPers, self.x)
        elif self.settings.clustMeth == ClusterizationType.AGGLOMERATIVE:
            km = Clust.agglomerative(self.settings.clustCnt, self.x)
        else:
            km = Clust.spectral(self.settings.clustCnt, self.settings.minClustSize, self.x)
        km.fit(self.x)
        self.km = km
        self.work_time = time() - t0
        self.calcMetrix(km)
        self.me.LHomogenVal.setText("Однородность: %0.3f" % self.homogen)
        self.me.LCompletenessVal.setText("Полнота: %0.3f" % self.completeness)
        self.me.LVMeasVal.setText("V-мера: %0.3f" % self.v_measure)
        self.me.LWTimeVal.setText("Время работы: %0.1f с." % self.work_time)
        self.me.BGetPlots.setEnabled(True)

    def vectorize(self):
        vectorizer = LangVectorize(self.settings.lang, self.settings)
        if self.settings.vectMeth == VectorizationType.TF:
            self.x = vectorizer.tf(self.dataset.data)
        if self.settings.vectMeth == VectorizationType.TFIDF:
            self.x = vectorizer.tfidf(self.dataset.data)
        if self.settings.vectMeth == VectorizationType.HASH:
            self.x = vectorizer.hash(self.dataset.data)
        if self.settings.vectMeth == VectorizationType.ONEHOT:
            self.x = vectorizer.oh(self.dataset.data)
        if self.settings.vectMeth == VectorizationType.DISTR:
            self.x = vectorizer.distribution(self.dataset.data)

    def createPlots(self):
        plt.rcParams["figure.figsize"] = (10, 8)
        fig, (ax1, ax2) = plt.subplots(2, sharex=True)
        fig.suptitle('Сравнение распределения документов по кластерам')
        clusters = [i for i in range(self.settings.clustCnt)]
        orig_distr = []
        pred_distr = []
        for i in range(self.settings.clustCnt):
            pred_i = np.where(self.km.labels_ == i)[0].size
            orig_i = np.where(self.labels == i)[0].size
            orig_distr.append(pred_i)
            pred_distr.append(orig_i)
        ax1.plot(clusters, orig_distr, 'o')
        ax2.plot(clusters, pred_distr, '*')
        ax1.grid()
        ax2.grid()
        plt.xticks(np.arange(0, self.settings.clustCnt))
        ax1.set_title('Оригинальное распределение документов по кластерам')
        ax2.set_title('Предсказанное распределение документов по кластерам')
        fig.show()

    def calcMetrix(self, km):
        self.homogen = metrics.homogeneity_score(self.labels, km.labels_)
        self.completeness = metrics.completeness_score(self.labels, km.labels_)
        self.v_measure = metrics.v_measure_score(self.labels, km.labels_)

    def initNewsgroup(self):
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
        self.dataset = fetch_20newsgroups(subset='all', categories=categories[:barier], shuffle=True, random_state=42)
        # print("%d documents" % len(self.dataset.data))
        # print("%d categories" % len(self.dataset.target_names))
        self.labels = self.dataset.target
        self.true_k = np.unique(self.labels).shape[0]

    def initOntoWnd(self):
        self.changeSetWnd = QtWidgets.QMainWindow()
        self.changeSetUI = Ui_MainWindow()
        self.changeSetWnd.prevWindow = self.me
