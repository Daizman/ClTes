from model.enums.PartOfSpeech import PartOfSpeech
from model.enums.Lang import Lang
from nltk.corpus import stopwords as nltk_sw


class Settings:
    def __init__(self,
                 minWordSize=0,
                 maxDictSize=2**20,
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
                 tokenRe=r'[\w\d]+',
                 vectMeth=None,
                 clustMeth=None,
                 useTokenFilter=False):
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
        self.tokenRe = tokenRe
        self.vectMeth = vectMeth
        self.clustMeth = clustMeth
        self.useTokenFilter = useTokenFilter
