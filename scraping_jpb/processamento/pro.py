import os
import re
import csv
import nltk
import spacy
import scipy.sparse
import pandas as pd

from string import punctuation
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

from gensim.utils import simple_preprocess, lemmatize
from gensim.models import LdaModel, LdaMulticore
from smart_open import smart_open
from gensim import matutils, models
from gensim import corpora
from pprint import pprint

nltk.download('stopwords')
stop_words = stopwords.words('portuguese')

stop_words = stop_words + ["aqui", "gente", "tá", "né", "calendário", "jpb", "agora", "lá", "hoje", "aí", "ainda", "então", "vai", "porque", "moradores", "fazer", "rua", "bairro", "prefeitura", "todo", "vamos"]

### Carregando dados.
data = pd.read_csv('../textos_videos.csv', encoding='utf-8')
t = data['texto']

textos = []
for texto in t:
    textos.append(texto.lower())
# print(textos)

nlp = spacy.load('pt_core_news_sm')
data_processada = []

def buscar_entidade(palavra, entidades):
    for ent in entidades:
        if (ent.text == palavra):
            return ent
    return -1

for texto in textos:
    t = nlp(texto)
    doc_out = []
    entidades = [entity for entity in doc.ents]
    for palavra in texto.split():
        if (palavra not in stop_words):
            verifica_entidade = buscar_entidade(palavra, entidades)
            if (verifica_entidade != -1):
                if (verifica_entidade.label_ == "NN" or verifica_entidade.label_ == "NN")
            doc_out.append(palavra)

        else:
            continue
    data_processada.append(doc_out)

print(data_processada[0][:5])

dct = corpora.Dictionary(data_processada)
corpus = [dct.doc2bow(line) for line in data_processada]

lda_model = LdaMulticore(corpus=corpus,
                         id2word=dct,
                         num_topics=4,
                         passes=10)

lda_model.save('lda_model.model')

print(lda_model.print_topics(-1))

'''
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