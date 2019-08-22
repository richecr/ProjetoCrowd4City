import re
import csv
import nltk
import spacy
import pandas as pd

from string import punctuation
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

from gensim.utils import simple_preprocess
from smart_open import smart_open
from gensim import corpora
from pprint import pprint
import os

### Carregando dados.
data = pd.read_csv('../textos_videos.csv', encoding='utf-8')
t = data['texto']

textos = []
for texto in t:
    textos.append(texto)
# print(textos)

# Tokenização dos textos.
tokenized_list = [simple_preprocess(doc) for doc in textos]

# Criação do Corpus
mydict = corpora.Dictionary()
mycorpus = [mydict.doc2bow(doc, allow_update=True) for doc in tokenized_list]
# pprint(mycorpus)

# Convertendo os id's em palavras novamente. Melhorar visualização.
word_counts = [[(mydict[id], count) for id, count in line] for line in mycorpus]
pprint(word_counts)

'''
def sort_coo(coo_matrix):
    tuples = zip(coo_matrix.col, coo_matrix.data)
    return sorted(tuples, key=lambda x: (x[1], x[0]), reverse=True)

def extract_topn_from_vector(feature_names, sorted_items, topn=10):
    """get the feature names and tf-idf score of top n items"""
    
    #use only topn items from vector
    sorted_items = sorted_items[:topn]

    score_vals = []
    feature_vals = []

    for idx, score in sorted_items:
        fname = feature_names[idx]
        
        #keep track of feature name and its corresponding score
        score_vals.append(round(score, 3))
        feature_vals.append(feature_names[idx])

    #create a tuples of feature,score
    #results = zip(feature_vals,score_vals)
    results= {}
    for idx in range(len(feature_vals)):
        results[feature_vals[idx]]=score_vals[idx]
    
    return results

def pre_processamento(texto):
    texto = texto.lower()
    texto = re.sub("(\\d|\\W)+", " ", texto)
    stopwords1 = set(stopwords.words('portuguese') + list(punctuation))
    res = ""
    for p in texto.split():
        if (p not in stopwords1):
            res += p + " "

    return res

data['texto'] = data['texto'].apply(lambda x:pre_processamento(x))

nltk.download('stopwords')

docs = data['texto'].tolist()

# Criando um vocabulário de palavras.
# Eliminando as palavras que aparecem em 85% dos textos.
# Eliminando as stopwords.
cv = CountVectorizer(max_df=0.85, stop_words=stopwords.words('portuguese'))
word_count_vector = cv.fit_transform(docs)

print(list(cv.vocabulary_.keys())[:10])

tfidf_transformer = TfidfTransformer(smooth_idf=True, use_idf=True)
tfidf_transformer.fit(word_count_vector)

feature_names = cv.get_feature_names()

doc = docs[0]

tf_idf_vector = tfidf_transformer.transform(cv.transform([doc]))

sorted_items = sort_coo(tf_idf_vector.tocoo())

keywords = extract_topn_from_vector(feature_names, sorted_items, 15)

print("========TEXTO========")
print(doc)
print("========KEYWORDS========")
print(keywords)
'''