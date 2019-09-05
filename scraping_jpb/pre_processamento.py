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

def verificar_palavra_entidade_loc(palavra, entidades_loc):
	"""
	Verifica se a palavra é uma entidade de localização.

	Parâmetros:
	----------
	palavra : 'String'\n
	entidades_loc : 'List' de entidades de localizações.

	Retorno:
	----------
	True : Caso a palavra seja uma entidade de localização.\n
	False : Caso a palavra não seja uma entidade de localização.
	"""
    
	for e in entidades_loc:
		if (e.text.lower() == palavra.lower()):
			return True

	return False

def para_texto(lista):
	saida = ""
	for palavra in lista:
		saida += palavra + " "

	return saida.strip()

fields = ["titulo", "texto"]
f = csv.writer(open('./processamento/textos_limpos.csv', 'w', encoding='utf-8'))
f.writerow(fields)

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
def pre_processamento(texto, titulo):
    doc_out = []
    doc = nlp(texto)
    entidades_loc = [entidade for entidade in doc.ents if entidade.label_ == "LOC"]
    for token in doc:
        if (token.text not in gensim.parsing.preprocessing.STOPWORDS and token.pos_ in allowed_postags and not verificar_palavra_entidade_loc(token.text, entidades_loc)):
            doc_out.append(lematização(token.text))

    texto = para_texto(doc_out)
    f.writerow([titulo, texto])

for texto, titulo in zip(textos, titulo_textos):
	pre_processamento(texto, titulo)