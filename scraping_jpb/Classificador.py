import re
import numpy as np
import pandas as pd
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

#Funções de Pre-Processamento.
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