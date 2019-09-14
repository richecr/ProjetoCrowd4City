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
		if (palavra.lower() not in stop_words_spacy):
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

continuar = "4106572"
def main(textos, titulos):
	cont = 0
	cont_erros = 0
	flag = False
	for texto, titulo in zip(textos, titulos):
		if (flag):
			print(titulo)
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
		else:
			if (continuar.lower() in titulo.lower()):
				flag = True
			if ("4488541" in titulo.lower()):
				flag = False
			continue

textos_limpos = []
titulos = []
arq = csv.DictReader(open("./textos_videos.csv", "r", encoding='utf-8'))

for p in arq:
	textos_limpos.append(p['texto'])
	titulos.append(p['titulo'])

main(textos_limpos, titulos)