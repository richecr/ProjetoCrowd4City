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

# Configurando bibliotecas e variaveis globais.
stemmer = PorterStemmer()
nlp = spacy.load("pt_core_news_sm")
gensim.parsing.preprocessing.STOPWORDS.union(["tudo", "coisa", "toda", "tava", "pessoal", "dessa", "resolvido", "aqui", "gente", "tá", "né", "calendário", "jpb", "agora", "voltar", "lá", "hoje", "aí", "ainda", "então", "vai", "porque", "moradores", "fazer", "rua", "bairro", "prefeitura", "todo", "vamos", "problema", "fica", "ver", "tô"])


def lematizacao(palavra):
    """
	Realiza a lematização de uma palavra.

	Parâmetro:
	----------
	palavra : String
		- Palavra que irá sofrer a lematização.

	Retorno:
	----------
	palavra : String
		- Palavra lematizada.
	"""
    return stemmer.stem(WordNetLemmatizer().lemmatize(palavra, pos="v"))

def lista_para_texto(lista):
    """
	Transforma uma lista de palavras em texto.

	Parâmetros:
	----------
	lista : List
		- Lista de palavras.

	Retorno:
	----------
	texto : String
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
    doc = nlp(texto)
    for token in doc:
        if (token.text not in gensim.parsing.preprocessing.STOPWORDS and token.pos_ in allowed_postags):
            doc_out.append(lematizacao(token.text))

    texto = lista_para_texto(doc_out)
    return texto

def tf(palavra, texto):
    resultado = 0
    for p in texto:
        if (palavra.lower() == p.lower()):
            resultado += 1

    return resultado

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
        if (", campina grande" in end['address'].lower() and ", paraíba" in end['address'].lower()):
            return True
        else:
            return False
    else:
        return False

def buscar_endereco(texto):
    bbox = [-35.959043, -7.312016, -35.842933, -7.175498]
    response = geocoder.mapbox(texto, bbox=bbox, key="pk.eyJ1IjoicmljaGVsdG9uIiwiYSI6ImNqejFrNnRkdDA1NDkzaW1samUyY2pkc2YifQ.Nl_sJiP2M1hm-gXdm7zR1w")

    return response.json

def verifica_endereco_mapbox(end):
    if (end['text'].lower() in ruas):
        return True
    if (end['relevance'] >= 0.5):
        if ("campina grande" in end['place_name'].lower() and "paraíba" in end['place_name'].lower()):
            return True
        else:
            return False
    else:
        return False

# print(textos_limpos)

# Fazer as verificações corretas.

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

def verifica_teste_mapbox(ents_loc):
    ends = []
    for loc in ents_loc:
        l = str(loc)
        # Retorna uma lista de endereços.
        # Deve se achar o com maior chance dessa lista
        # E por fim comparar com os melhores das outras lista
        # Assim restando o melhor entre todos os endereços encontrados.
        end = buscar_endereco(l)
        if (end != None):
            ends.append(end['features'])
    # print("1: ", json.dumps(ends, indent=4))

    ends_corretos = []
    for e in ends:
        for address in e:
            if (verifica_endereco_mapbox(address)):
                ends_corretos.append(address)
    # print("2: ", json.dumps(ends_corretos, indent=4))

    if (len(ends_corretos)):
        end_final = ends_corretos[0]
        end_final_confidence = ends_corretos[0]
        for ed in ends_corretos:
            if (ed['relevance'] > end_final_confidence['relevance']):
                end_final = ed
        print("3: ", end_final)
        return (True, end_final)
    else:
        return (False, [])

def main(textos_limpos):
    cont = 0
    nlp = spacy.load('pt_core_news_sm')
    for texto in textos_limpos:
        doc = nlp(texto)
        ents_loc = [entity for entity in doc.ents if entity.label_ == "LOC"]
        end_encontrados = concantena_end(ents_loc)
        print(ents_loc)
        result = verfica(end_encontrados)
        if result[0]:
            cont += 1
        print("\n------------------------------------------------\n")
    print(cont)

textos_limpos = []
arq = csv.DictReader(open("./textos_videos.csv", encoding='utf-8'))

for p in arq:
    textos_limpos.append(p['texto'])

txl = []
for l in textos_limpos:
    txt = pre_processamento(l)
    txl.append(txt)

main(txl)

# Básico: Indo atras do endereço, da primeira entidade, usando a API do mapbox - geocoding
'''
# Testar com a API do mapbox. Pode ser que seja melhor.
response = requests.get("https://api.mapbox.com/geocoding/v5/mapbox.places/rua joao sergio de almeida%20campina grande%20.json?country=BR&fuzzyMatch=true&language=pt&proximity=-7.22592,-35.8755&access_token=pk.eyJ1IjoicmljaGVsdG9uIiwiYSI6ImNqejFrNnRkdDA1NDkzaW1samUyY2pkc2YifQ.Nl_sJiP2M1hm-gXdm7zR1w")
loc = response.json()
print(loc)
print(loc['features'][3]['context'][1]['text']) # Santa Catarina

response = requests.get('https://api.mapbox.com/geocoding/v5/mapbox.places/' + ents_loc[0].__str__() + ', campina grande.json?access_token=pk.eyJ1IjoicmljaGVsdG9uIiwiYSI6ImNqejFrNnRkdDA1NDkzaW1samUyY2pkc2YifQ.Nl_sJiP2M1hm-gXdm7zR1w')
enderecos = response.json()

ends = enderecos['features'][0]
print(ends)

if (ends['relevance'] >= 0.5):
    if (ends['context'][2]['text'] == "Campina Grande"):
        print("CORRETO")
    else:
        print("ERRADO, Tenta outra combinação")
else:
    print("ERRADO, Tenta outra combinação")
'''


'''
textos = pd.read_csv("./textos_videos.csv")
textos = textos.drop_duplicates()

textos_limpos = [txt for txt in textos['texto']]
# print(textos_limpos[0])

print(textos_limpos)
'''