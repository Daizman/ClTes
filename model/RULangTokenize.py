import re

import pymorphy2

from nltk import SnowballStemmer

from model.enums.PartOfSpeech import PartOfSpeech
from model.enums.TokenizerType import TokenizerType


class RULangTokenize:
    def __init__(self, settings):
        self.settings = settings

        self.__tokenRe = r'[\w\d]+'
        self.__posStr = 'VERB' if self.settings.pos == PartOfSpeech.VERB \
            else 'NOUN' if self.settings.pos == PartOfSpeech.NOUN else 'ADJ'
        self.__morph = None
        self.__stemmer = None

    def tokenize(self, texts, tokenizerType=TokenizerType.SIMPLE):
        if tokenizerType == TokenizerType.SIMPLE:
            return [self.simpleTokenize(text) for text in texts]
        if tokenizerType == TokenizerType.STEM:
            self.__stemmer = SnowballStemmer("russian")
            return [self.stemTokenize(text) for text in texts]
        self.__morph = pymorphy2.MorphAnalyzer()
        return [self.lemTokenize(text) for text in texts]

    def simpleTokenize(self, txt):
        sw = self.settings.sw if self.settings.useSW else []
        tokens = [token for token in txt.lower().split()
                  if len(token) >= self.settings.minWordSize and token not in sw]
        if not self.settings.useGramms:
            return [token for token in tokens if re.search(self.__tokenRe, token)]

        return self.__grammsTokenize(tokens, self.settings.useLem, self.settings.useStem)

    def __grammsTokenize(self, tokens, useLem=False, useStem=False):
        if len(tokens) % self.settings.grammsSize != 0:
            tokens += ['' for _ in range(len(tokens) % self.settings.grammsSize)]

        res_tokens = []
        temper_token = []
        i = 0
        for token in tokens:
            i += 1
            if useStem:
                temper_token += self.__stemmer.stem(token.strip())
            elif useLem:
                terms = self.__morph.parse(token.strip())
                termToAdd = ''
                for term in terms:
                    if term.tag.POS == self.__posStr:
                        termToAdd = term.normal_form
                        break
                if termToAdd == '':
                    termToAdd = terms[0].normal_form
                temper_token += termToAdd
            else:
                temper_token += token
            if i == self.settings.grammsSize:
                res_tokens.append(' '.join(temper_token))
                temper_token = []
                i = 0
        return res_tokens

    def stemTokenize(self, text):
        self.__stemmer = SnowballStemmer("russian")
        return self.simpleTokenize(text)

    def lemTokenize(self, text):
        self.__morph = pymorphy2.MorphAnalyzer()
        return self.simpleTokenize(text)
