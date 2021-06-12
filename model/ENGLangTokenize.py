import re

import nltk
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer

from model.enums.PartOfSpeech import PartOfSpeech
from model.enums.TokenizerType import TokenizerType


class ENGLangTokenize:
    def __init__(self, settings):
        self.settings = settings

        self.__tokenRe = r'[\w\d]+'
        self.__posStr = 'v' if self.settings.pos == PartOfSpeech.VERB \
            else 'n' if self.settings.pos == PartOfSpeech.NOUN else 'a'
        self.__lemmatizer = None
        self.__stemmer = None

    def tokenize(self, texts, tokenizerType=TokenizerType.SIMPLE):
        if tokenizerType == TokenizerType.SIMPLE:
            return [self.simpleTokenize(text) for text in texts]
        if tokenizerType == TokenizerType.STEM:
            self.__stemmer = SnowballStemmer("english")
            return [self.stemTokenize(text) for text in texts]
        self.__lemmatizer = WordNetLemmatizer()
        return [self.lemTokenize(text) for text in texts]

    def simpleTokenize(self, text):
        sw = self.settings.sw if self.settings.useSW else []
        tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)
                  if len(word) >= self.settings.minWordSize and word not in sw]
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
                temper_token += self.__lemmatizer.lemmatize(token.strip(), pos=self.__posStr)
            else:
                temper_token += token
            if i == self.settings.grammsSize:
                res_tokens.append(' '.join(temper_token))
                temper_token = []
                i = 0
        return res_tokens

    def stemTokenize(self, text):
        self.__stemmer = SnowballStemmer("english")
        return self.simpleTokenize(text)

    def lemTokenize(self, text):
        self.__lemmatizer = WordNetLemmatizer()
        return self.simpleTokenize(text)
