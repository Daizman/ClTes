from enum import Enum


class VectorizationType(Enum):
    ONEHOT = 1
    TF = 2
    TFIDF = 3
    HASH = 4
    DISTR = 5
