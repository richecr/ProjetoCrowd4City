import pandas as pd
import gensim
import nltk
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import *
from nltk.stem.porter import *
import numpy as np
np.random.seed(2018)
nltk.download('wordnet')

stemmer = PorterStemmer()

# Carregando os dados.
dados = pd.read_csv("../textos_videos.csv")
textos = dados['texto']
# print(textos[:5])

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

processed_docs = dados['texto'].map(preprocess)
print(processed_docs[:10])

dictionary = gensim.corpora.Dictionary(processed_docs)
count = 0
for k, v in dictionary.iteritems():
    print(k, v)
    count += 1
    if count > 10:
        break
