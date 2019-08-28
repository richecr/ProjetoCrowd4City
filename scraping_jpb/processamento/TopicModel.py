import pandas as pd
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import numpy as np
import nltk

np.random.seed(2018)
nltk.download('wordnet')

# Carregando os dados.
dados = pd.read_csv("../textos_videos.csv")
textos = dados['texto']
print(textos[:5])

# Pré-processamento dos dados.

# Lematização
def lemmatize_stemming(text):
    return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))

# Colocando todas as palavras para caixa baixa.
# Removendo acentos e pontuações.
# Remover palavras com menos de 3 letras.
def preprocess(text):
    result = []
    for token in gensim.utils.simple_preprocess(text):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(lemmatize_stemming(token))
    return result

