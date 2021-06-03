import re
import nltk
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer

from model.enums.PartOfSpeech import PartOfSpeech
from model.enums.TokenizerType import TokenizerType


class ENGLangTokenize:
    def __init__(self, settings):
        self.tokenRe = settings.tokenRe
        self.minWordSize = settings.minWordSize
        self.pos = settings.pos
        self.__posStr = 'v' if self.pos == PartOfSpeech.VERB else 'n' if self.pos == PartOfSpeech.NOUN else 'a'
        self.stopwords = settings.sw if settings.useSW else []
        self.useGramms = settings.useGramms
        self.grammsSize = settings.grammsSize
        self.__lemmatizer = None
        self.__stemmer = None

    def tokenize(self, texts, tokenizer_type=TokenizerType.SIMPLE):
        if tokenizer_type == TokenizerType.SIMPLE:
            return [self.simpleTokenize(text) for text in texts]
        if tokenizer_type == TokenizerType.STEM:
            self.__stemmer = SnowballStemmer("english")
            return [self.stemTokenize(text) for text in texts]
        self.__lemmatizer = WordNetLemmatizer()
        return [self.lemTokenize(text) for text in texts]

    def simpleTokenize(self, txt):
        tokens = [word for sent in nltk.sent_tokenize(txt) for word in nltk.word_tokenize(sent)
                  if len(word) >= self.minWordSize and word not in self.stopwords]
        if not self.useGramms:
            return [token for token in tokens if re.search(self.tokenRe, token)]

        if len(tokens) % self.grammsSize != 0:
            tokens += ['' for _ in range(len(tokens) % self.grammsSize)]

        res_tokens = []
        temper_token = []
        i = 0
        for token in tokens:
            i += 1
            temper_token += token
            if i == self.grammsSize:
                res_tokens.append(' '.join(temper_token))
                temper_token = []
                i = 0
        return res_tokens

    def stemTokenize(self, text):
        filtered_tokens = self.simpleTokenize(text)
        self.__stemmer = SnowballStemmer("english")
        return [self.__stemmer.stem(t.strip()) for t in filtered_tokens]

    def lemTokenize(self, text):
        filtered_tokens = self.simpleTokenize(text)
        self.__lemmatizer = WordNetLemmatizer()
        return [self.__lemmatizer.lemmatize(t.strip(), pos=self.__posStr) for t in filtered_tokens]
