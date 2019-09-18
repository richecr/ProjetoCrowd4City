import os
import csv
import json
import spacy
from os import path
from time import sleep


TRAIN_DATA = [
    ('what is the price of polo?', {'entities': [(21, 25, 'PrdName')]}), 
    ('what is the price of ball?', {'entities': [(21, 25, 'PrdName')]}), 
    ('what is the price of jegging?', {'entities': [(21, 28, 'PrdName')]})
]

nlp = spacy.load("pt_core_news_sm")

# Carregando dados.
dados = csv.DictReader(open("./textos_videos.csv", encoding='utf-8'))
textos = []
titulo_textos = []

def retorna_indice(palavra, texto):
    part = texto.split(palavra)
    indice_inicio = len(part[0])
    return indice_inicio

lista_fim = []
for texto in dados:
    doc = nlp(texto['texto'])
    ent_loc = [e for e in doc.ents if e.label_ == "LOC" or e.label_ == "GPE"]
    entidades = {}
    entidades['entities'] = []
    for e in ent_loc:
        print(e.text)
        i = retorna_indice(e.text, texto['texto'])
        i_f = i + len(e.text)
        entidades['entities'].append((i, i_f, 'LOC'))
    
    obj = (texto['texto'].lower(), entidades)
    lista_fim.append(obj)
    break

print(lista_fim)
with open("./textos.json", 'w') as f:
    json.dump(lista_fim, f)
'''

teste = []
with open("./textos.json", 'r') as r:
    teste = json.load(r)

print( tuple(teste[0])[0])

'''