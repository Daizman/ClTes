import pymorphy2
from nltk import SnowballStemmer
from model.Enums.PartOfSpeech import PartOfSpeech
from model.Enums.TokenizerType import TokenizerType


class RULangTokenize:
    def __init__(self, settings):
        self.tokenRe = settings.tokenRe
        self.minWordSize = settings.minWordSize
        self.pos = settings.pos
        self.__posStr = 'VERB' if self.pos == PartOfSpeech.VERB else 'NOUN' if self.pos == PartOfSpeech.NOUN else 'ADJ'
        self.stopwords = settings.stopwords
        self.useGramms = settings.useGramms
        self.grammsSize = settings.grammsSizese
        self.__stemmer = None
        self.__morph = None

    def tokenize(self, texts, tokenizer_type=TokenizerType.SIMPLE):
        if tokenizer_type == TokenizerType.SIMPLE:
            return [self.simpleTokenize(text) for text in texts]
        if tokenizer_type == TokenizerType.STEM:
            self.__stemmer = SnowballStemmer("russian")
            return [self.stemTokenize(text) for text in texts]
        self.__morph = pymorphy2.MorphAnalyzer()
        return [self.lemTokenize(text) for text in texts]

    def simpleTokenize(self, txt):
        if not self.useGramms:
            return [token for token in self.tokenRe.findall(txt.lower())
                    if len(token) >= self.minWordSize and token not in self.stopwords]

        start_tokens = [token for token in self.tokenRe.findall(txt.lower())
                        if len(token) >= self.minWordSize and token not in self.stopwords]
        if len(start_tokens) % self.grammsSize != 0:
            start_tokens += ['' for _ in range(len(start_tokens) % self.grammsSize)]

        tokens = []
        temper_token = []
        i = 0
        for token in start_tokens:
            i += 1
            temper_token += token
            if i == self.grammsSize:
                tokens.append(' '.join(temper_token))
                temper_token = []
                i = 0
        return tokens

    def stemTokenize(self, text):
        return [self.__stemmer.stem(t.strip()) for t in self.simpleTokenize(text)]

    def lemTokenize(self, text):
        return [(term.normal_form for term in self.__morph.parse(t.strip()) if term.tag.POS == self.__posStr)
                for t in self.simpleTokenize(text)]
