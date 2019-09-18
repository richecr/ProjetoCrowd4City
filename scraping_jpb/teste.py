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
    ent_loc1 = []
    for i in ent_loc:
        flag = True
        for j in ent_loc1:
            if (i.text == j.text):
                flag = False
                break
        if (flag):
            ent_loc1.append(i)

    entidades = {}
    entidades['entities'] = []
    for e in ent_loc1:
        i = retorna_indice(e.text, texto['texto'])
        i_f = i + len(e.text)
        entidades['entities'].append((i, i_f, 'LOC'))
    
    obj = (texto['texto'].lower(), entidades)
    lista_fim.append(obj)

with open("./textos.json", 'w', encoding='utf-8') as f:
    json.dump(lista_fim, f)
f.close()

teste = []
with open("./textos.json", 'r', encoding='utf-8') as r:
    teste = json.load(r)
r.close()

ts = open("./treinar_spacy.txt", mode="w", encoding="utf-8")

for partial in teste:
    t1 = tuple(partial)
    ts.write(str(t1))
    ts.write('\n')

#print( tuple(teste[0])[1])
