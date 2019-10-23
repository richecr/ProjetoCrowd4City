import csv
import nltk
import spacy
import pandas as pd

import requests
import json
import geocoder
import re

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

gazetteer_ln = csv.DictReader(open("./processamento/gazetteer/gazetteer_ln.csv", "r", encoding='utf-8'))
gazetteer_pt = csv.DictReader(open("./processamento/gazetteer/gazetteer_pt.csv", "r", encoding='utf-8'))

suburb = [k['name'].lower() for k in gazetteer_pt if k['fclass'] == "suburb" and len(k['name'].split()) <= 1]

residencial = {}

def processar_gazetteer(gazetter):
	saida = {}
	for row in gazetter:
		if row['fclass'] == "residential":
			residencial[row['name'].lower()] = row['coordenates']
		else:
			saida[row['name'].lower()] = row['coordenates']

	return saida

gazetteer_ln = processar_gazetteer(gazetteer_ln)
gazetteer_pt = processar_gazetteer(gazetteer_pt)
gazetteer_ln.update(gazetteer_pt)

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

def main(textos, titulos):
	correct = 0
	fail = 0
	total = 0
	for texto, titulo in zip(textos, titulos):
		#texto = pre_processing(texto)
		texto = texto.lower()
		residential = []
		geral = []
		flag = False
		texto_lista = texto.split()
		for key in residencial.keys():
			key_aux = key.split()
			if key_aux[0] == "rua":
				key_aux = key_aux[1:]
			if (len(key_aux) > 1):
				if re.search("\\b" + key + "\\b", texto):
					flag = True
					residential.append(key)

		for key in gazetteer_ln.keys():
			key_aux = key.split()
			if key_aux[0] == "rua":
				key_aux = key_aux[1:]
			if (len(key_aux) > 1):
				if re.search("\\b" + key + "\\b", texto):
					flag = True
					geral.append(key)

		print("residencial: ", residential)
		print("residencial: ", geral)
		if flag:
			correct += 1
		else:
			fail += 1
		total += 1

	print(total)
	print(correct)
	print(fail)

textos_limpos = []
titulos = []
arq = csv.DictReader(open("./textos_videos.csv", "r", encoding='utf-8'))

for p in arq:
	textos_limpos.append(p['texto'])
	titulos.append(p['titulo'])

#textos_limpos = ["o calendário JPB foi até a zona leste de Campina Grande os moradores do bairro José Pinheiro estão muito preocupados com trânsito no cruzamento da rua Marinheira Agra seguintes segundo eles e a gente viu de perto também no local não tem sinalização os carros não respeitam os pedestres Vários acidentes acontecem por lá quem foi conseguir essa loucura de perto foi Marcos Vasconcelos Lembra daquela música infantil que fala assim se essa rua fosse minha eu mandava ladrilhar com pedrinhas de brilhante para o meu amor passar pois é o pessoal aqui da rua Marinheira Agra não queria tanto não queria apenas um asfalto e o pessoal conseguiu A rua está um tapete só só que ao chegar no cruzamento com a Campos Sales Esqueceram de um detalhe bastante importante para mim a sinalização por aqui o cruzamento é uma bagunça só E olha que essa comerciante falou que o trânsito está até tranquilo só chegou a Comparar as cruzamento com alguns outro trânsito de assim a solução para que a Índia tem hora que eu tô naquele nojenta Não estou no Brasil não é possível que eu esteja no Brasil por que uma loucura tão grande quem vai passar primeiro que não vai passar primeiro é horrível horrível né o barulho o tempo todo eu tava horrível aqui mas foi ficar apenas poucos minutos e o problema apareceu aqui ninguém sabe de quem é a prioridade para entrar em uma das ruas e se você for um pedestre então é complicado e o pessoal não tem educação não tem ainda Educação de trânsito muita gente não tem educação de trânsito quando vai passar muitas vezes se pede parada ninguém para ficar como não poderia deixar de ser se ninguém se entende neste cruzamento no bairro de José Pinheiro acidente acontece direto é só que vem cruzando a gente é a principal que ele conhece o bairro Passa direto e indireto Faz 15 dias que a senhora e o rapaz aí ela vir aí o carro bateu jogo hoje não tá fazendo ali quebrou a perna foi problema aqui já tem oito meses eu acho que vai acontecer um acidente aqui para tentar resolver esse problema ou trouxemos o calendário JPB até o bairro do José Pinheiro aqui do meu lado Já está o Alex masculino e gerente de operações da sttp o que pode ser feito aqui iremos em diante do problema que está acontecendo com relação a algumas partes das sinalizações que estão em déficit colocarmos a sinalização horizontal vertical colocaremos as placas faremos as pinturas colocaremos Estações intercalados para que possa minimizar a velocidade como também faremos um trabalho de pintura das vias para que possa os veículos não estacionar menos 5 metros aqui como também colocaremos agentes de trânsito para que possa ajudar no tráfico desses veículos Fábio acha que isso resolve nada não chegou ainda aí já que ele tá aqui pessoalmente a gente vai fazer aí não vai fazer como"]
main(textos_limpos, titulos)

# main(textos_limpos, titulos)


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