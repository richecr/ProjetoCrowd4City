import re
import nltk
import numpy as np
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.probability import FreqDist
from collections import defaultdict
from nltk.corpus import stopwords
from heapq import nlargest
from string import punctuation
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import cross_val_score, cross_val_predict, train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

### Carregando dados.
data = pd.read_csv('./problemas_textos_testes.csv', encoding='utf-8')

### Pre-Processamento dos dados.
# Remove duplicadas, caso exista.
data.drop_duplicates(['texto'], inplace=True)

# Separando os dados de sua classificação
titulo = data['titulo']
textos = data['texto']
problemas = data['problema']
enderecos = data['endereco']
resolvidos = data['resolvido']

# Instala bibliotecas e baixa a base de dados
nltk.download('stopwords')
nltk.download('rslp')

docs = data['texto'].tolist()

# Criando um vocabulário de palavras.
# Eliminando as palavras que aparecem em 85% dos textos.
# Eliminando as stopwords.
cv = CountVectorizer(max_df=0.85, stop_words=stopwords.words('portuguese'))
word_count_vector = cv.fit_transform(docs)
# print(word_count_vector)

print(list(cv.vocabulary_.keys())[:15])

tfidf_transformer = TfidfTransformer(smooth_idf=True, use_idf=True)
tfidf_transformer.fit(word_count_vector)

# Função para resumir um texto.
def sumarizacao(texto):
    sentencas = sent_tokenize(texto)
    palavras = word_tokenize(texto.lower())
    stopwords1 = set(stopwords.words('portuguese') + list(punctuation))
    palavras_sem_stopwords = [palavra for palavra in palavras if palavra not in stopwords1]
    frequencia = FreqDist(palavras_sem_stopwords)
    sentencas_importantes = defaultdict(int)
    for i, sentenca in enumerate(sentencas):
        for palavra in word_tokenize(sentenca.lower()):
            if palavra in frequencia:
                sentencas_importantes[i] += frequencia[palavra]
    idx_sentencas_importantes = nlargest(4, sentencas_importantes, sentencas_importantes.get)

    txt = ""
    for i in sorted(idx_sentencas_importantes):
        txt += sentencas[i]

    return txt

# Funções de Pre-Processamento.
# Função que remove as palavras consideradas irrelevantes para o conjunto de resultados.
def RemoveStopWords(instancia):
    stopwords = set(nltk.corpus.stopwords.words('portuguese'))
    palavras = [i for i in instancia.split() if not i in stopwords]
    return (" ".join(palavras))

# Função que faz a limpeza dos tweets: Removendo links, marcações e etc.
def limpa_dados(instancia):
    # TODO
    pass

# Aplicando funções de pre-processamento.
def preprocessamento(instancia):
    stemmer = nltk.stem.RSLPStemmer()
    instancia = re.sub(r"http\S+", "", instancia).lower().replace('.','').replace(';','').replace('-','').replace(':','').replace(')','')
    stopwords = set(nltk.corpus.stopwords.words('portuguese'))
    palavras = [stemmer.stem(i) for i in instancia.split() if not i in stopwords]
    return (" ".join(palavras))