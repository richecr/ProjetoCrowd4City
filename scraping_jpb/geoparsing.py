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

from googletrans import Translator

import truecase


translator = Translator() 

#fields = ["endereco", "texto"]
#f = csv.writer(open('./enderecos1.csv', 'w', encoding='utf-8'))
#f.writerow(fields)

# Configurando bibliotecas e variaveis globais.
stemmer = PorterStemmer()
nlp = spacy.load("pt_core_news_sm")
nlp.Defaults.stop_words |= {"ficar", "quando", "aqui", "vamos", "olha", "pois", "tudo", "coisa", "toda", "tava", "pessoal", "dessa", "resolvido", "aqui", "gente", "tá", "né", "calendário", "jpb", "agora", "voltar", "lá", "hoje", "aí", "ainda", "então", "vai", "porque", "moradores", "fazer", "prefeitura", "todo", "vamos", "problema", "fica", "ver", "tô"}
stop_words_spacy = nlp.Defaults.stop_words

gazetter_ln = csv.DictReader(open("./processamento/gazetteer/gazetteer_ln.csv", "r", encoding='utf-8'))
gazetter_pt = csv.DictReader(open("./processamento/gazetteer/gazetteer_pt.csv", "r", encoding='utf-8'))

def processar_gazetteer(gazetter):
	saida = {}
	for row in gazetter:
		saida[row['name'].lower()] = row['coordenates']

	return saida

gazetter_ln = processar_gazetteer(gazetter_ln)
gazetter_pt = processar_gazetteer(gazetter_pt)

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

def remove_repeat(lista):
	saida = []
	for item in lista:
		item = str(item)
		if not saida.__contains__(item.lower()):
			if len(item.split()) >= 2:
				saida.append(item.lower())
	return saida

def lista2text(lista):
	texto = ""
	for palavra in lista:
		texto += palavra + " "
	
	return texto.strip()

def pre_processing(text):
        """
            Realiza o pré-processamento de um texto:
                - Remove Stop Words.
                - Remove palavras que são entidades de localizações.
                - Colocar as palavras para caixa baixa.
                - Realiza a lematização das palavras.
                - Apenas palavras que são: substantivos, adjetivos e pronomes.
            Parâmetro:
            ----------
            texto : String
                - Texto que irá sofrer o pré-processamento.
            titulo: String
                - Titulo do texto.

            Retorno:
            ----------
            doc_out : List
                - Lista de palavras que passaram pelo pré-processamento.
        """
        doc_out = []
        doc = nlp(text)
        entidades_loc = [entidade for entidade in doc.ents if entidade.label_ == "LOC"]
        for token in doc:
            if (token.text.lower() not in stop_words_spacy and len(token.text) > 3):
                doc_out.append(token.text)

        return lista2text(doc_out)

continuar = "5670399"
def main(textos, titulos):
	cont = 0
	cont_erros = 0
	total = 0
	for texto, titulo in zip(textos, titulos):
		texto = pre_processing(texto)
		regex = r"[A-ZÀ-Ú]+[a-zà-ú]+[ \-]?(?:d[a-u].)?(?:[A-ZÀ-Ú]+[a-zà-ú]+)*"
		candidates = re.findall(regex, texto)
		c = []
		flag = True
		for candidate in candidates:
			achou = False
			for key in gazetter_ln.keys():
				if candidate.lower() == key:
					c.append(key)
					achou = True
					break
			if achou:
				print(candidate)
				print(c)
				flag = False
				cont += 1
				break
		if flag:
			cont_erros += 1
		total += 1
		if (total == 50):
			break
		'''
		ents_loc = [entity for entity in doc.ents if entity.label_ == "LOC" or entity.label_ == "GPE"]
		ents_loc = remove_repeat(ents_loc)
		print(ents_loc)
		for loc in ents_loc:
			flag = False
			for key in gazetter_ln.keys():
				if str(loc).lower() in key:
					print(str(loc))
					print("achou")
					flag = True
			if not flag:
				print(str(loc))
				print("n achou")
				flag = True
		print("--------------------")
		'''
		'''
		address_found = concantena_end(ents_loc)
		result = verfica(address_found, limit)
		
		if (result[0]):
			return result[1]
		else:
			raise Exception("Não foi possivel realizar o geoparsing do texto")
		'''

	print(cont)
	print(cont_erros)
textos_limpos = []
titulos = []
arq = csv.DictReader(open("./textos_videos.csv", "r", encoding='utf-8'))

for p in arq:
	textos_limpos.append(p['texto'])
	titulos.append(p['titulo'])

main(textos_limpos, titulos)


'''
if (flag):
			# print(texto)
			texto_en = translator.translate(texto, src="pt", dest="en")
			texto_en = texto_en.text
			t = truecase.caser.get_true_case(texto_en)

			texto_pt = translator.translate(t, src="en", dest="pt")
			texto = texto_pt.text
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
				# f.writerow([result[1]['address'], texto])
				cont += 1
			else:
				cont_erros += 1
			print("\n------------------------------------------------\n")
			print(cont, " - ", cont_erros)
		else:
			if (continuar.lower() in titulo.lower()):
				flag = True
			continue

from model.model.ner_model import NERModel
from model.model.config import Config
from nltk import word_tokenize
from nltk import tokenize

import nltk
from nltk.tokenize import sent_tokenize
from nltk import tokenize
import re
from sacremoses import MosesTruecaser, MosesTokenizer
'''