import csv
import nltk
import spacy
import pandas as pd

import requests
import json

textos_limpos = []
arq = csv.DictReader(open("./textos_videos.csv", encoding='utf-8'))

for p in arq:
    textos_limpos.append(p["texto"])

print(textos_limpos)

# Removendo stop words
txts = []
nltk.download('stopwords')
stop_words = nltk.corpus.stopwords.words('portuguese')
for t in textos_limpos:
    te = ""
    for palavra in t.split(" "):
        if (palavra not in stop_words):
            te += palavra
            te += " "
    txts.append(te)

print("-----------------------\n")
print(txts)

# Carregando modelo em português.
nlp = spacy.load('pt')
doc = nlp(txts[0])

# Salvar as entidades que foram classificadas como LOC.
ents_loc = [entity for entity in doc.ents if entity.label_ == "LOC"]
print(ents_loc)

# Básico: Indo atras do endereço, da primeira entidade, usando a API do mapbox - geocoding
response = requests.get('https://api.mapbox.com/geocoding/v5/mapbox.places/' + ents_loc[0].__str__() + ', joão pessoa.json?access_token=pk.eyJ1IjoicmljaGVsdG9uIiwiYSI6ImNqejFrNnRkdDA1NDkzaW1samUyY2pkc2YifQ.Nl_sJiP2M1hm-gXdm7zR1w')
enderecos = response.json()

ends = enderecos['features'][0]
print(ends)

if (ends['relevance'] >= 0.5):
    if (ends['context'][2]['text'] == "João Pessoa"):
        print("CORRETO")
    else:
        print("ERRADO, Tenta outra combinação")
else:
    print("ERRADO, Tenta outra combinação")

'''
textos = pd.read_csv("./textos_videos.csv")
textos = textos.drop_duplicates()

textos_limpos = [txt for txt in textos['texto']]
# print(textos_limpos[0])

print(textos_limpos)
'''