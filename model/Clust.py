from sklearn import cluster
import numpy as np


class Clust:
    @staticmethod
    def kMeans(clustCnt, learnIters, vectorizedTexts):
        km = cluster.KMeans(n_clusters=clustCnt, init='k-means++', max_iter=learnIters, n_init=1)
        km.fit(vectorizedTexts)
        return km

    @staticmethod
    def miniBatch(clustCnt, learnIters, vectorizedTexts):
        km = cluster.MiniBatchKMeans(n_clusters=clustCnt, init='k-means++', max_iter=learnIters, n_init=1, batch_size=1000)
        km.fit(vectorizedTexts)
        return km

    @staticmethod
    def birch(clustCnt, similPer, vectorizedTexts):
        km = cluster.Birch(n_clusters=clustCnt, threshold=similPer)
        km.fit(vectorizedTexts)
        return km

    @staticmethod
    def spectral(clustCnt, minClustSize, vectorizedTexts):
        km = cluster.SpectralClustering(n_clusters=clustCnt, random_state=42, affinity='nearest_neighbors', n_neighbors=minClustSize)
        km.fit(vectorizedTexts)
        return km

    @staticmethod
    def agglomerative(clustCnt, vectorizedTexts):
        km = cluster.AgglomerativeClustering(n_clusters=clustCnt)
        vectorizedTexts = np.asarray(vectorizedTexts) if type(vectorizedTexts) == list else vectorizedTexts.toarray()
        km.fit(vectorizedTexts)
        return km
