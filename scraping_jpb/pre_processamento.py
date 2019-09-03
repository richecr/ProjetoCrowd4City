import csv
import json
import pandas as pd

import nltk
import spacy
import gensim
from nltk.stem.porter import *
from nltk.stem import WordNetLemmatizer

# Objetivo é colocar todos os textos(dados) em um arquivo CSV, pré-processados.
# Resultado é ter um arquivo com todos os textos(dados) pré-processados.

# Carregando dados.
dados = csv.DictReader(open("./textos_videos.csv", encoding='utf-8'))
textos = []
titulo_textos = []

for arq in dados:
    textos.append(arq['texto'])
    titulo_textos.append(arq['titulo'])

# ---------

# Configurando bibliotecas e variaveis globais.
stemmer = PorterStemmer()
nlp = spacy.load("pt_core_news_sm")
gensim.parsing.preprocessing.STOPWORDS.union(["tudo", "coisa", "toda", "tava", "pessoal", "dessa", "resolvido", "aqui", "gente", "tá", "né", "calendário", "jpb", "agora", "voltar", "lá", "hoje", "aí", "ainda", "então", "vai", "porque", "moradores", "fazer", "rua", "bairro", "prefeitura", "todo", "vamos", "problema", "fica", "ver", "tô"])


def lematização(palavra):
    return stemmer.stem(WordNetLemmatizer().lemmatize(palavra, pos="v"))

allowed_postags = ['NOUN', 'ADJ', 'PRON']
def pre_processamento(texto):
    doc = nlp(texto)
    entidades_loc = [entidade for entidade in doc.ents if entidade.label_ == "LOC"]
    for token in doc:
        if (token.text not in gensim.parsing.preprocessing.STOPWORDS):
            if(token.pos_ in allowed_postags):
                if (token)

