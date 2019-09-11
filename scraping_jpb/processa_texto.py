import csv
import nltk
import spacy
import pandas as pd

import requests
import json
import geocoder

import gensim
from nltk.stem.porter import *
from nltk.stem import WordNetLemmatizer

# Ruas de Campina grande
ruas = []
with open("./ruas.json") as f:
    ruas = json.load(f)

fields = ["endereco", "texto"]
f = csv.writer(open('./enderecos.csv', 'w', encoding='utf-8'))
f.writerow(fields)

# Configurando bibliotecas e variaveis globais.
stemmer = PorterStemmer()
nlp = spacy.load("pt_core_news_sm")
gensim.parsing.preprocessing.STOPWORDS.union(["tudo", "coisa", "toda", "tava", "pessoal", "dessa", "resolvido", "aqui", "gente", "tá", "né", "calendário", "jpb", "agora", "voltar", "lá", "hoje", "aí", "ainda", "então", "vai", "porque", "moradores", "fazer", "rua", "bairro", "prefeitura", "todo", "vamos", "problema", "fica", "ver", "tô"])

def lematizacao(palavra):
    """
	Realiza a lematização de uma palavra.

	Parâmetro:
	----------
	``palavra`` : String
		- Palavra que irá sofrer a lematização.

	Retorno:
	----------
	``palavra`` : String
		- Palavra lematizada.
	"""
    return stemmer.stem(WordNetLemmatizer().lemmatize(palavra, pos="v"))

def lista_para_texto(lista):
    """
	Transforma uma lista de palavras em texto.

	Parâmetros:
	----------
	``lista`` : List
		- Lista de palavras.

	Retorno:
	----------
	``texto`` : String
		- O texto contento todas as palavras da lista.
	"""
    texto = ""
    for palavra in lista:
        texto += palavra + " "

    return texto.strip()

allowed_postags = ['NOUN', 'ADJ', 'PRON']
def pre_processamento(texto):
    """
	Realiza o pré-processamento de um texto:
		- Remove Stop Words.
		- Remove palavras que são entidades de localizações.
		- Colocar as palavras para caixa baixa.
		- Realiza a lematização das palavras.
		- Apenas palavras que são: substantivos, adjetivos e pronomes.

	Parâmetro:
	----------
	``texto`` : String
		- Texto que irá sofrer o pré-processamento.
	``titulo``: String
		- Titulo do texto.

	Retorno:
	----------
	``doc_out`` : List
		- Lista de palavras que passaram pelo pré-processamento.
	"""
    doc_out = []
    doc = nlp(texto)
    for token in doc:
        if (token.text not in gensim.parsing.preprocessing.STOPWORDS):
            doc_out.append(token.text)

    texto = lista_para_texto(doc_out)
    return texto

def concantena_end(lista_end):
    saida = []
    for i in range(len(lista_end) - 1):
        for j in range(i+1, len(lista_end)):
            temp = str(lista_end[i]) + " " + str(lista_end[j])
            saida.append(temp)
    return saida

def verifica_endereco(end):
	if (end['address'].lower() in ruas):
		return True
	if (end['confidence'] >= 5):
		# ", campina grande" in end['address'].lower() and
		if (", paraíba" in end['address'].lower()):
			return True
		else:
			return False
	else:
		return False

# print(textos_limpos)

def verfica(ents_loc):
    ends = []
    for loc in ents_loc:
        l = str(loc)
        g = geocoder.arcgis(l)
        end = g.json
        if (end != None):
            ends.append(end)
    # print("1: ", json.dumps(ends, indent=4))

    ends_corretos = []
    for e in ends:
        if (verifica_endereco(e)):
            ends_corretos.append(e)
    print("2: ", json.dumps(ends_corretos, indent=4))

    if (len(ends_corretos)):
        end_final = ends_corretos[0]
        end_final_confidence = ends_corretos[0]
        for ed in ends_corretos:
            if (ed['confidence'] > end_final_confidence['confidence']):
                end_final = ed
        print("3: ", end_final)
        return (True, end_final)
    else:
        return (False, [])

def main(textos, titulos):
	cont = 0
	nlp = spacy.load('pt_core_news_sm')
	for texto, titulo in zip(textos, titulos):
		doc = nlp(texto)
		ents_loc = [entity for entity in doc.ents if entity.label_ == "LOC"]
		end_encontrados = concantena_end(ents_loc)
		print(ents_loc)
		result = verfica(end_encontrados)
		if result[0]:
			f.writerow([result[1]['address'], texto])
			cont += 1
		else:
			doc = nlp(titulo)
			ents_loc = [entity for entity in doc.ents if entity.label_ == "LOC"]
			end_encontrados = concantena_end(ents_loc)
			print(ents_loc)
			result = verfica(end_encontrados)
			if result[0]:
				f.writerow([result[1]['address'], texto])
				cont += 1
		print("\n------------------------------------------------\n")
	print(cont)


textos_limpos = []
titulos = []
arq = csv.DictReader(open("./textos_videos.csv", encoding='utf-8'))

for p in arq:
	textos_limpos.append(p['texto'])
	titulos.append(p['titulo'])

txl = []
for l in textos_limpos:
	txt = pre_processamento(l)
	txl.append(txt)

main(txl, titulos)