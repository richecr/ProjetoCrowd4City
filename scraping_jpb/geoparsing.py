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

from model.model.ner_model import NERModel
from model.model.config import Config
from nltk import word_tokenize
from nltk import tokenize

import nltk
from nltk.tokenize import sent_tokenize
from nltk import tokenize
import re
from sacremoses import MosesTruecaser, MosesTokenizer

# from treinar_spacy.train_ner import Truecasing
class Truecasing():
    def __init__(self):
        self.nlp = spacy.load("pt_core_news_sm")
        self.nlp.Defaults.stop_words |= {"vamos", "olha", "pois", "tudo", "coisa", "toda", "tava", "pessoal", "dessa", "resolvido", "aqui", "gente", "tá", "né", "calendário", "jpb", "agora", "voltar", "lá", "hoje", "aí", "ainda", "então", "vai", "porque", "moradores", "fazer", "prefeitura", "todo", "vamos", "problema", "fica", "ver", "tô"}
        self.stop_words_spacy = self.nlp.Defaults.stop_words
        self.mtr = MosesTruecaser()
        self.mtok = MosesTokenizer(lang="en")
        tokenized_docs = [self.mtok.tokenize(line) for line in open('./textos.txt')]
        self.mtr.train(tokenized_docs, save_to='textos.truecasemodel')

    def truecasing(self, texto):
        texto = self.remove_stop_words(texto)
        # texto = self.pre_processamento(texto)
        texto = self.mtr.truecase(texto, return_str=True)
        return self.nlp(texto)

    def pre_processamento(self, texto):
       # texto = self.remove_stop_words(texto)
        novo_texto = ""
        lista = ["rua", "r.", "bairro", "avenida", "av", "travessa", "trav."]
        prox = False
        for palavra in texto.split():
            if (prox):
                novo_texto += palavra[0].upper() + palavra[1:] + " "
                prox = False
            elif (palavra.lower() in lista):
                novo_texto += palavra[0].upper() + palavra[1:] + " "
                prox = True
            else:
                novo_texto += palavra + " "

        return novo_texto.strip()
    
    def remove_stop_words(self, texto):
        saida = ""
        for palavra in texto.split():
            if (palavra.lower() not in self.stop_words_spacy):
                saida += palavra + " "
        s = saida.strip()
        return s


fields = ["endereco", "texto"]
f = csv.writer(open('./enderecos1.csv', 'w', encoding='utf-8'))
f.writerow(fields)

# Configurando bibliotecas e variaveis globais.
stemmer = PorterStemmer()
nlp = spacy.load("pt_core_news_sm")
nlp.Defaults.stop_words |= {"vamos", "olha", "pois", "tudo", "coisa", "toda", "tava", "pessoal", "dessa", "resolvido", "aqui", "gente", "tá", "né", "calendário", "jpb", "agora", "voltar", "lá", "hoje", "aí", "ainda", "então", "vai", "porque", "moradores", "fazer", "prefeitura", "todo", "vamos", "problema", "fica", "ver", "tô"}
stop_words_spacy = nlp.Defaults.stop_words

def remove_stop_words(texto):
	saida = ""
	for palavra in texto.split():
		if (palavra.lower() not in stop_words_spacy and len(palavra) > 3):
			saida += palavra + " "
	s = saida.strip()
	return s

def concantena_end(lista_end):
    saida = []
    for i in range(len(lista_end) - 1):
        for j in range(i+1, len(lista_end)):
            temp = str(lista_end[i]) + " " + str(lista_end[j])
            saida.append(temp)
    return saida

def verifica_endereco(end):
	# if (end['address'].lower() in ruas):
	#	return True
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
    # print("2: ", json.dumps(ends_corretos, indent=4))

    if (len(ends_corretos)):
        end_final = ends_corretos[0]
        end_final_confidence = ends_corretos[0]
        for ed in ends_corretos:
            if (ed['confidence'] > end_final_confidence['confidence']):
                end_final = ed
        print("3: ", end_final['address'])
        return (True, end_final)
    else:
        return (False, [])

config = Config()

# build model
model = NERModel(config)
model.build()
model.restore_session(config.dir_model)

continuar = "5670399"
def main(textos, titulos):
	cont = 0
	cont_erros = 0
	flag = True
	for texto, titulo in zip(textos, titulos):
		if (flag):			
			# Testar '.upper()' e '.title()'
			# E ver qual é melhor.
			# texto = remove_stop_words(texto.upper())
			# print(texto)
			words = tokenize.word_tokenize(texto, language="portuguese")
			predsTexto = model.predict(words)
			# print(predsTexto)
			ents_loc = []
			texto_ = texto.split()
			for pos in range(len(predsTexto)):
				if (predsTexto[pos] == "B-LOCAL" or predsTexto[pos] == "I-LOCAL"):
					ents_loc.append(texto_[pos])

			print(ents_loc)
			# Testar título com Spacy.
			titulo = titulo.split("-")[0]
			print(titulo)
			doc_titulo = nlp(titulo)
			ents_loc1 = [entity for entity in doc_titulo.ents if entity.label_ == "LOC" or entity.label_ == "GPE"]
			
			'''
			print(texto)
			doc = nlp(texto)
			titulo = titulo.split("-")
			doc1 = nlp(titulo[0])
			ents_loc = [entity for entity in doc.ents if entity.label_ == "LOC" or entity.label_ == "GPE"]
			ents_loc1 = [entity for entity in doc1.ents if entity.label_ == "LOC" or entity.label_ == "GPE"]
			end_encontrados = concantena_end(ents_loc + ents_loc1)
			
			print(ents_loc)
			print("------")
			print(ents_loc1)
			print("------")
			print(end_encontrados)

			result = verfica(end_encontrados)
			if result[0]:
				f.writerow([result[1]['address'], texto])
				cont += 1
			else:
				cont_erros += 1
			print("\n------------------------------------------------\n")
			print(cont, " - ", cont_erros)
			'''
		else:
			if (continuar.lower() in titulo.lower()):
				flag = True
			continue

textos_limpos = []
titulos = []
arq = csv.DictReader(open("./textos_videos.csv", "r", encoding='utf-8'))

for p in arq:
	textos_limpos.append(p['texto'])
	titulos.append(p['titulo'])

main(textos_limpos, titulos)