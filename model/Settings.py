from model.enums.PartOfSpeech import PartOfSpeech
from model.enums.Lang import Lang
from model.enums.ClusterizationType import ClusterizationType
from model.enums.VectorizationType import VectorizationType
from nltk.corpus import stopwords as nltk_sw


class Settings:
    def __init__(self,
                 minWordSize=0,
                 maxDictSize=2**16,
                 minWordCnt=1,
                 maxWordFq=1,
                 minWordFq=0,
                 useStem=False,
                 useLem=False,
                 pos=PartOfSpeech.NOUN,
                 useSW=False,
                 sw=None,
                 useGramms=False,
                 grammsSize=1,
                 clustCnt=10,
                 maxIters=10000,
                 similPers=1,
                 minClustSize=1,
                 lang=Lang.RUS,
                 vectMeth=VectorizationType.TFIDF,
                 clustMeth=ClusterizationType.KMEANS,
                 useTokenFilter=False,
                 distrEpoch=10):
        self.minWordSize = minWordSize
        self.maxDictSize = maxDictSize
        self.minWordCnt = minWordCnt
        self.maxWordFq = maxWordFq
        self.minWordFq = minWordFq
        self.useStem = useStem
        self.useLem = useLem
        self.pos = pos
        self.useSW = useSW
        self.sw = sw if sw is not None else nltk_sw.words('russian') if lang == Lang.RUS else nltk_sw.words('english')
        self.useGramms = useGramms
        self.grammsSize = grammsSize
        self.clustCnt = clustCnt
        self.maxIters = maxIters
        self.similPers = similPers
        self.minClustSize = minClustSize
        self.lang = lang
        self.vectMeth = vectMeth
        self.clustMeth = clustMeth
        self.useTokenFilter = useTokenFilter
        self.distrEpoch = distrEpoch

    def __str__(self):
        return 'Минимальный размер слова: {}\n' \
               'Максимальный размер словаря: {}\n' \
               'Минимальное количество встречь слова: {}\n' \
               'Максимальная частота встречь слова: {}\n' \
               'Минимальная частота встречь слова: {}\n' \
               'Использование стемминга: {}\n' \
               'Использование лемматизации: {}\n' \
               'Использование стоп-слов: {}\n' \
               'Использование группировки: {}\n' \
               'Количество токенов в группе: {}\n' \
               'Количество кластеров: {}\n' \
               'Количество эпох обучения: {}\n'.format(self.minWordSize,
                                                       self.maxDictSize,
                                                       self.minWordCnt,
                                                       self.maxWordFq,
                                                       self.minWordFq,
                                                       'Да' if self.useStem else 'Нет',
                                                       'Да' if self.useLem else 'Нет',
                                                       'Да' if self.useSW else 'Нет',
                                                       'Да' if self.useGramms else 'Нет',
                                                       self.grammsSize,
                                                       self.clustCnt,
                                                       self.maxIters)
