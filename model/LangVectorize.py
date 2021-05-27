from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import HashingVectorizer

from nltk.corpus import stopwords as nltk_sw

from gensim.models.doc2vec import Doc2Vec, TaggedDocument

from model.RULangTokenize import RULangTokenize
from model.ENGLangTokenize import ENGLangTokenize

from model.Enums.Lang import Lang
from model.Enums.TokenizerType import TokenizerType


class LangVectorize:
    def __init__(self, lang, settings):
        self.lang = lang
        self.settings = settings
        self.__tokenizer = RULangTokenize(self.settings) if self.lang == Lang.RUS else ENGLangTokenize(self.settings)

    def vect(self, model, corpus, binary=False):
        if stem:
            if use_sw:
                vectorizer = model(tokenizer=tokenizer.stem_nltk_tokenizer,
                                   stop_words=nltk_sw.words('english'),
                                   min_df=min_df,
                                   max_df=max_df,
                                   max_features=max_features,
                                   binary=binary)
            else:
                vectorizer = model(tokenizer=tokenizer.stem_nltk_tokenizer,
                                   min_df=min_df,
                                   max_df=max_df,
                                   max_features=max_features,
                                   binary=binary)
        elif lem:
            if use_sw:
                vectorizer = model(tokenizer=tokenizer.lem_nltk_tokenizer,
                                   stop_words=nltk_sw.words('english'),
                                   min_df=min_df,
                                   max_df=max_df,
                                   max_features=max_features,
                                   binary=binary)
            else:
                vectorizer = model(tokenizer=tokenizer.lem_nltk_tokenizer,
                                   min_df=min_df,
                                   max_df=max_df,
                                   max_features=max_features,
                                   binary=binary)
        elif use_nltk:
            if use_sw:
                vectorizer = model(tokenizer=tokenizer.nltk_tokenizer,
                                   stop_words=nltk_sw.words('english'),
                                   min_df=min_df,
                                   max_df=max_df,
                                   max_features=max_features,
                                   binary=binary)
            else:
                vectorizer = model(tokenizer=tokenizer.nltk_tokenizer,
                                   min_df=min_df,
                                   max_df=max_df,
                                   max_features=max_features,
                                   binary=binary)
        else:
            if use_sw:
                vectorizer = model(stop_words="english",
                                   min_df=min_df,
                                   max_df=max_df,
                                   max_features=max_features,
                                   binary=binary)
            else:
                vectorizer = model(min_df=min_df,
                                   max_df=max_df,
                                   max_features=max_features,
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
                        epochs=self.settings.maxIters,
                        workers=4)

        return [it for it in model.docvecs]
