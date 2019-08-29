import pandas as pd
import gensim
import nltk
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import *
from nltk.stem.porter import *
from nltk.corpus import stopwords
import numpy as np
np.random.seed(2018)
nltk.download('wordnet')

stemmer = PorterStemmer()

# Carregando os dados.
dados = pd.read_csv("../textos_videos.csv")
textos = dados['texto']
# print(textos[:5])

nltk.download('stopwords')
stop_words = stopwords.words('portuguese')
stop_words = stop_words + ["tudo", "aqui", "gente", "tá", "né", "calendário", "jpb", "agora", "voltar", "lá", "hoje", "aí", "ainda", "então", "vai", "porque", "moradores", "fazer", "rua", "bairro", "prefeitura", "todo", "vamos", "problema", "fica", "ver", "tô"]

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
        if token not in stop_words and len(token) > 3:
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

# Gensim Filter Extremes
# dictionary.filter_extremes(no_below=15, no_above=0.5, keep_n=100000)

# Bag-of-words.
bow_corpus = [dictionary.doc2bow(doc) for doc in processed_docs]

bow_doc_4310 = bow_corpus[50]
for i in range(len(bow_doc_4310)):
    print("A palavra {} (\"{}\") apareceu {} vez(es).".format(bow_doc_4310[i][0], 
                                               dictionary[bow_doc_4310[i][0]], 
bow_doc_4310[i][1]))