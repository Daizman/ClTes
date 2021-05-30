from enum import Enum


class ClusterizationType(Enum):
    KMEANS = 1
    MINIBATCH_KMEANS = 2
    BIRCH = 3
    SPECTRAL = 4
    AGGLOMERATIVE = 5
