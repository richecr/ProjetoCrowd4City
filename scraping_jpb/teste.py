import os
import csv
import json
import spacy
from os import path
from time import sleep

nlp = spacy.load("pt_core_news_sm")

f = open('./processamento/textos.txt', 'w', encoding='utf-8')

# Carregando dados.
dados = csv.DictReader(open("./textos_videos.csv", encoding='utf-8'))
textos = []
titulo_textos = []

for texto in dados:
    f.write(texto['texto'])
    f.write("\n")