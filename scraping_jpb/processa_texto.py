import csv
import nltk
import spacy
import pandas as pd

textos_limpos = []
arq = csv.DictReader(open("./textos_videos.csv"))

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
'''
textos = pd.read_csv("./textos_videos.csv")
textos = textos.drop_duplicates()

textos_limpos = [txt for txt in textos['texto']]
# print(textos_limpos[0])

print(textos_limpos)

# Carregando modelo em português.
nlp = spacy.load('pt')

doc = nlp(txts[0])

# [print((token.orth_, token.pos_)) for token in doc]
[print((entity, entity.label_)) for entity in doc.ents]
'''