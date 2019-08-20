import csv
import nltk
import spacy
import pandas as pd

import requests
import json
import geocoder

# Ruas de Campina grande
ruas = []
with open("./ruas.json") as f:
    ruas = json.load(f)

def pre_processamento(texto):
    novo_texto = ""
    for palavra in texto:
        novo_texto += palavra.lower()

    return novo_texto

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
        if (", joão pessoa" in end['address'].lower() or ", paraíba" in end['address'].lower()):
            return True
        else:
            return False
    else:
        return False

def achar_inicio_nome_rua(texto):
    saida = []
    inicio = 0
    cont = 0
    for i in range(len(texto.split())):
        if texto.split()[i].lower() == "rua":
            inicio = i + 1
            break

    for i in range(inicio, len(texto.split())):
        if cont < 3:
            if (texto.split()[i].lower() not in ["de", "da", "do"]):
                cont += 1
            saida.append(texto.split()[i])

    return saida

textos_limpos = []
arq = csv.DictReader(open("./textos_videos.csv", encoding='utf-8'))

for p in arq:
    textos_limpos.append(p['texto'])

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
    print("2: ", json.dumps(ends_corretos, indent=4))

    if (len(ends_corretos)):
        end_final = ends_corretos[0]
        end_final_confidence = ends_corretos[0]
        for ed in ends_corretos:
            if (ed['confidence'] > end_final_confidence['confidence']):
                end_final = ed
        print("3: ", end_final)
        return True
    else:
        return False

'''
# Testar com a API do mapbox. Pode ser que seja melhor.
response = requests.get("https://api.mapbox.com/geocoding/v5/mapbox.places/rua joao sergio de almeida.json?access_token=pk.eyJ1IjoicmljaGVsdG9uIiwiYSI6ImNqejFrNnRkdDA1NDkzaW1samUyY2pkc2YifQ.Nl_sJiP2M1hm-gXdm7zR1w")
loc = response.json()
print(loc)
print(loc['features'][3]['context'][1]['text']) # Santa Catarina
'''

def main():
    cont = 0
    nlp = spacy.load('pt_core_news_sm')
    for texto in textos_limpos:
        doc = nlp(texto)
        ents_loc = [entity for entity in doc.ents if entity.label_ == "LOC"]
        end_encontrados = concantena_end(ents_loc)
        print(ents_loc)
        if verfica(end_encontrados):
            cont += 1
        print("\n------------------------------------------------\n")
    print(cont)

main()

'''
# Carregando modelo em português.
nlp = spacy.load('pt_core_news_sm')
doc = nlp(textos_limpos[0])

# Salvar as entidades que foram classificadas como LOC.
ents_loc = [entity for entity in doc.ents if entity.label_ == "LOC"]
print(ents_loc)

end_encontrados = concantena_end(ents_loc)

print(achar_inicio_nome_rua(textos_limpos[0]))
# Básico: Indo atras do endereço, da primeira entidade, usando a API do geocoder com arcgis.
# Para testes # ents_loc[0] = "Rua João Sergio de almeida"
flag = False
ends = []
for loc in ents_loc:
    l = str(loc)
    g = geocoder.arcgis(l)
    end = g.json
    ends.append(end)
print("1: ", ends)
print("\n----------------\n")

ends_corretos = []
for e in ends:
    if (verifica_endereco(e)):
        ends_corretos.append(e)
print("2: ", ends_corretos)
print("\n----------------\n")

end_final = ends_corretos[0]
end_final_confidence = ends_corretos[0]

for ed in ends_corretos:
    if (ed['confidence'] > end_final_confidence['confidence']):
        end_final = end
print("3: ", end_final)
print("\n----------------\n")
'''

'''
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

# Básico: Indo atras do endereço, da primeira entidade, usando a API do mapbox - geocoding
'''
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