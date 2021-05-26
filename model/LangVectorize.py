from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import HashingVectorizer

from nltk.corpus import stopwords as nltk_sw

from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from gensim.utils import simple_preprocess

from model.RULangTokenize import RULangTokenize
from model.ENGLangTokenize import ENGLangTokenize

from model.Enums.Lang import Lang
from model.Enums.TokenizerType import TokenizerType


class LangVectorize:
    def __init__(self, lang, settings):
        self.lang = lang
        self.settings = settings
        self.__tokenizer = RULangTokenize(self.settings) if self.lang == Lang.RUS else ENGLangTokenize(self.settings)

    def vect(self, model, corpus, stem, lem, use_sw, use_nltk,  min_cnt=0, max_features=None, max_df=1.0, binary=False):
        min_df = min_cnt
        tokenizer = Tokenizer()
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

    def tf(self, corpus, stem, lem, use_sw, use_nltk,  min_cnt=0, max_features=None, max_df=1.0):
        return self.vect(CountVectorizer, corpus, stem, lem, use_sw, use_nltk, min_cnt, max_features, max_df)

    def oh(self, corpus, stem, lem, use_sw, use_nltk,  min_cnt=0, max_features=None, max_df=1.0):
        return self.vect(CountVectorizer, corpus, stem, lem, use_sw, use_nltk,  min_cnt, max_features, max_df, True)

    def tfidf(self, corpus, stem, lem, use_sw, use_nltk,  min_cnt=0, max_features=None, max_df=1.0):
        return self.vect(TfidfVectorizer, corpus, stem, lem, use_sw, use_nltk, min_cnt, max_features, max_df)

    def hash(self, corpus, stem, lem, use_sw, use_nltk, max_features):
        if max_features is None:
            max_features = 2**20
        if stem:
            if use_sw:
                vectorizer = HashingVectorizer(tokenizer=tokenizer.stem_nltk_tokenizer,
                                               stop_words=nltk_sw.words('english'),
                                               n_features=max_features)
            else:
                vectorizer = HashingVectorizer(tokenizer=tokenizer.stem_nltk_tokenizer,
                                               n_features=max_features)
        elif lem:
            if use_sw:
                vectorizer = HashingVectorizer(tokenizer=tokenizer.lem_nltk_tokenizer,
                                               stop_words=nltk_sw.words('english'),
                                               n_features=max_features)
            else:
                vectorizer = HashingVectorizer(tokenizer=tokenizer.lem_nltk_tokenizer,
                                               n_features=max_features)
        elif use_nltk:
            if use_sw:
                vectorizer = HashingVectorizer(tokenizer=tokenizer.nltk_tokenizer,
                                               stop_words=nltk_sw.words('english'),
                                               n_features=max_features)
            else:
                vectorizer = HashingVectorizer(tokenizer=tokenizer.nltk_tokenizer,
                                               n_features=max_features)
        else:
            if use_sw:
                vectorizer = HashingVectorizer(stop_words="english",
                                               n_features=max_features)
            else:
                vectorizer = HashingVectorizer(n_features=max_features)
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

        if self.settings.maxDictSize is not None:
            if self.settings.maxIters is not None:
                model = Doc2Vec(tagged_docs,
                                vector_size=self.settings.maxDictSize,
                                min_count=self.settings.minWordCnt,
                                epochs=self.settings.maxIters,
                                workers=4)
            else:
                model = Doc2Vec(tagged_docs,
                                vector_size=self.settings.maxDictSize,
                                min_count=self.settings.minWordCnt,
                                workers=4)
        else:
            if self.settings.maxIters is not None:
                model = Doc2Vec(tagged_docs, min_count=self.settings.minWordCnt, epochs=self.settings.maxIters, workers=4)
            else:
                model = Doc2Vec(tagged_docs, min_count=self.settings.minWordCnt, workers=4)

        return [it for it in model.docvecs]
