from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import HashingVectorizer

from nltk.corpus import stopwords as nltk_sw

from gensim.models.doc2vec import Doc2Vec, TaggedDocument

from model.RULangTokenize import RULangTokenize
from model.ENGLangTokenize import ENGLangTokenize

from model.enums.Lang import Lang
from model.enums.TokenizerType import TokenizerType


class LangVectorize:
    def __init__(self, lang, settings):
        self.lang = lang
        self.settings = settings
        self.__tokenizer = RULangTokenize(self.settings) if self.lang == Lang.RUS else ENGLangTokenize(self.settings)

    def vect(self, model, corpus, binary=False):
        if self.settings.useStem:
            if self.settings.useSW:
                if self.settings.useGramms:
                    vectorizer = model(max_features=self.settings.maxDictSize,
                                       tokenizer=self.__tokenizer.stemTokenize,
                                       stop_words=self.settings.sw,
                                       ngram_range=(1, self.settings.grammsSize),
                                       min_df=self.settings.minWordFq,
                                       max_df=self.settings.maxWordFq,
                                       binary=binary)
                else:
                    vectorizer = model(max_features=self.settings.maxDictSize,
                                       tokenizer=self.__tokenizer.stemTokenize,
                                       stop_words=self.settings.sw,
                                       min_df=self.settings.minWordFq,
                                       max_df=self.settings.maxWordFq,
                                       binary=binary)
            else:
                if self.settings.useGramms:
                    vectorizer = model(max_features=self.settings.maxDictSize,
                                       tokenizer=self.__tokenizer.stemTokenize,
                                       ngram_range=(1, self.settings.grammsSize),
                                       min_df=self.settings.minWordFq,
                                       max_df=self.settings.maxWordFq,
                                       binary=binary)
                else:
                    vectorizer = model(max_features=self.settings.maxDictSize,
                                       tokenizer=self.__tokenizer.stemTokenize,
                                       min_df=self.settings.minWordFq,
                                       max_df=self.settings.maxWordFq,
                                       binary=binary)
        elif self.settings.useLem:
            if self.settings.useSW:
                if self.settings.useGramms:
                    vectorizer = model(max_features=self.settings.maxDictSize,
                                       tokenizer=self.__tokenizer.lemTokenize,
                                       stop_words=self.settings.sw,
                                       ngram_range=(1, self.settings.grammsSize),
                                       min_df=self.settings.minWordFq,
                                       max_df=self.settings.maxWordFq,
                                       binary=binary)
                else:
                    vectorizer = model(max_features=self.settings.maxDictSize,
                                       tokenizer=self.__tokenizer.lemTokenize,
                                       stop_words=self.settings.sw,
                                       min_df=self.settings.minWordFq,
                                       max_df=self.settings.maxWordFq,
                                       binary=binary)
            else:
                if self.settings.useGramms:
                    vectorizer = model(max_features=self.settings.maxDictSize,
                                       tokenizer=self.__tokenizer.lemTokenize,
                                       ngram_range=(1, self.settings.grammsSize),
                                       min_df=self.settings.minWordFq,
                                       max_df=self.settings.maxWordFq,
                                       binary=binary)
                else:
                    vectorizer = model(max_features=self.settings.maxDictSize,
                                       tokenizer=self.__tokenizer.lemTokenize,
                                       min_df=self.settings.minWordFq,
                                       max_df=self.settings.maxWordFq,
                                       binary=binary)
        else:
            if self.settings.useSW:
                if self.settings.useGramms:
                    vectorizer = model(max_features=self.settings.maxDictSize,
                                       tokenizer=self.__tokenizer.lemTokenize,
                                       stop_words=self.settings.sw,
                                       ngram_range=(1, self.settings.grammsSize),
                                       min_df=self.settings.minWordFq,
                                       max_df=self.settings.maxWordFq,
                                       binary=binary)
                else:
                    vectorizer = model(max_features=self.settings.maxDictSize,
                                       tokenizer=self.__tokenizer.lemTokenize,
                                       stop_words=self.settings.sw,
                                       min_df=self.settings.minWordFq,
                                       max_df=self.settings.maxWordFq,
                                       binary=binary)
            else:
                if self.settings.useGramms:
                    vectorizer = model(max_features=self.settings.maxDictSize,
                                       tokenizer=self.__tokenizer.lemTokenize,
                                       ngram_range=(1, self.settings.grammsSize),
                                       min_df=self.settings.minWordFq,
                                       max_df=self.settings.maxWordFq,
                                       binary=binary)
                else:
                    vectorizer = model(max_features=self.settings.maxDictSize,
                                       tokenizer=self.__tokenizer.lemTokenize,
                                       min_df=self.settings.minWordFq,
                                       max_df=self.settings.maxWordFq,
                                       binary=binary)

        return vectorizer.fit_transform(corpus)

    def tf(self, corpus):
        return self.vect(CountVectorizer, corpus)

    def oh(self, corpus):
        return self.vect(CountVectorizer, corpus, True)

    def tfidf(self, corpus):
        return self.vect(TfidfVectorizer, corpus)

    def hash(self, corpus):
        if self.settings.useStem:
            if self.settings.useSW:
                if self.settings.useGramms:
                    vectorizer = HashingVectorizer(n_features=self.settings.maxDictSize,
                                                   tokenizer=self.__tokenizer.stemTokenize,
                                                   stop_words=self.settings.sw,
                                                   ngram_range=(1, self.settings.grammsSize))
                else:
                    vectorizer = HashingVectorizer(n_features=self.settings.maxDictSize,
                                                   tokenizer=self.__tokenizer.stemTokenize,
                                                   stop_words=self.settings.sw)
            else:
                if self.settings.useGramms:
                    vectorizer = HashingVectorizer(n_features=self.settings.maxDictSize,
                                                   tokenizer=self.__tokenizer.stemTokenize,
                                                   ngram_range=(1, self.settings.grammsSize))
                else:
                    vectorizer = HashingVectorizer(n_features=self.settings.maxDictSize,
                                                   tokenizer=self.__tokenizer.stemTokenize)
        elif self.settings.useLem:
            if self.settings.useSW:
                if self.settings.useGramms:
                    vectorizer = HashingVectorizer(n_features=self.settings.maxDictSize,
                                                   tokenizer=self.__tokenizer.lemTokenize,
                                                   stop_words=self.settings.sw,
                                                   ngram_range=(1, self.settings.grammsSize))
                else:
                    vectorizer = HashingVectorizer(n_features=self.settings.maxDictSize,
                                                   tokenizer=self.__tokenizer.lemTokenize,
                                                   stop_words=self.settings.sw)
            else:
                if self.settings.useGramms:
                    vectorizer = HashingVectorizer(n_features=self.settings.maxDictSize,
                                                   tokenizer=self.__tokenizer.lemTokenize,
                                                   ngram_range=(1, self.settings.grammsSize))
                else:
                    vectorizer = HashingVectorizer(n_features=self.settings.maxDictSize,
                                                   tokenizer=self.__tokenizer.lemTokenize)
        else:
            if self.settings.useSW:
                if self.settings.useGramms:
                    vectorizer = HashingVectorizer(n_features=self.settings.maxDictSize,
                                                   tokenizer=self.__tokenizer.lemTokenize,
                                                   stop_words=self.settings.sw,
                                                   ngram_range=(1, self.settings.grammsSize))
                else:
                    vectorizer = HashingVectorizer(n_features=self.settings.maxDictSize,
                                                   tokenizer=self.__tokenizer.lemTokenize,
                                                   stop_words=self.settings.sw)
            else:
                if self.settings.useGramms:
                    vectorizer = HashingVectorizer(n_features=self.settings.maxDictSize,
                                                   tokenizer=self.__tokenizer.lemTokenize,
                                                   ngram_range=(1, self.settings.grammsSize))
                else:
                    vectorizer = HashingVectorizer(n_features=self.settings.maxDictSize,
                                                   tokenizer=self.__tokenizer.lemTokenize)

        return vectorizer.fit_transform(corpus)

    def distribution(self, corpus):
        if self.settings.useStem:
            docs = self.__tokenizer.tokenize(corpus, TokenizerType.STEM)
        elif self.settings.useLem:
            docs = self.__tokenizer.tokenize(corpus, TokenizerType.LEM)
        else:
            docs = self.__tokenizer.tokenize(corpus)

        tagged_docs = [
            TaggedDocument(words, ['d{}'.format(idx)])
            for idx, words in enumerate(docs)
        ]

        model = Doc2Vec(tagged_docs,
                        vector_size=self.settings.maxDictSize,
                        min_count=self.settings.minWordCnt,
                        epochs=10,
                        workers=4)

        vectors = []
        for i in range(model.docvecs.count):
            vectors.append(model.docvecs[i])

        return vectors
