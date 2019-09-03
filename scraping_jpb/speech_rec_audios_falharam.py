import os
import csv
import json
from os import path
import speech_recognition as sr

audios_falharam = []
def escreve():
    with open("./au_f.json", 'w', encoding='utf-8') as af1:
        json.dump(audios_falharam, af1)

audios = []
with open("./audios_falharam.json", 'r', encoding='utf-8') as af:
    audios = json.load(af)

fields = ["titulo", "texto"]
f = csv.writer(open('./textos_videos1.csv', 'w', encoding='utf-8'))
f.writerow(fields)

r = sr.Recognizer()

PATH_AUDIOS = path.dirname(path.realpath(__file__)) + "/audios/"

lista_audios = os.listdir(PATH_AUDIOS)
cont = 1
iniciar_em = 0
libera = False
for audio in audios:
    for a1 in lista_audios:
        if (a1.lower() == audio.lower()):
            print("Começa")
            print(a1)
            audio1 = a1
            caminho = PATH_AUDIOS + a1
            with sr.AudioFile(caminho) as source:
                a1 = r.record(source, duration=198)
            try:
                texto = r.recognize_google(a1, language="pt-br")
                titulo = audio1
                f.writerow([titulo, texto])
                print(cont, "concluído!")
                cont += 1
            except:
                print("FALHOU")
                audios_falharam.append(audio)
                escreve()
                continue

print(audios_falharam)

'''
for audio in lista_audios:
    if (audio.lower() == "Chef JPB - aprenda como fazer receita de 'malassada'-7850766.wav".lower()):
        print("COMEÇA")
        print(audio)
        audio1 = audio
        caminho = PATH_AUDIOS + audio
        with sr.AudioFile(caminho) as source:
            audio = r.record(source, duration=198)
        try:
            texto = r.recognize_google(audio, language="pt-br")
            titulo = audio1
            f.writerow([titulo, texto])
            print(cont, "concluído!")
            cont += 1
        except:
            print("FALHOU")
            print(audio1)
            audios_falharam.append(audio1)
            continue
'''
'''
["Calendário JPB - moradores reclamam e Emlur limpa rua em loteamento de João Pessoa-6877702.wav", "Chef JPB - aprenda como fazer receita de 'malassada'-7850766.wav", "Calendário JPB volta a Comunidade do 'S', em João Pessoa-6880497.wav", "Calendário JPB volta ao Cuiá, em João Pessoa-6908597.wav", "Calendário JPB mostra situação de praça no Ernani Sátiro, em João Pessoa, há dois anos-7344713.wav", "Calendário JPB - Moradores da cidade de Pocinhos cobram atendimento odontológico-5989883.wav", "Calendário JPB mostra situação de quadro de esportes em Santa Rita-6914313.wav", "Equipe do Calendário JPB vai ao conjunto Ernani Sátiro-6505432.wav", "Calendário JPB - moradores de Cruz das Armas pedem calçamento-5613123.wav", "Calendário JPB mostra praça no Esplanada, em João Pessoa-6882999.wav", "Calendário JPB volta ao bairro de Intermares, em Cabedelo-6862237.wav", "Calendário JPB 1 mostra mudanças em uma praça no bairro de Mandacaru, em João Pessoa-7478522.wav", "Calendário JPB volta à praia do Jacaré, em Cabedelo e traz novidados-7416730.wav", "Calendário JPB mostra obra parada em Santa Rita-7783480.wav", "Calendário JPB volta ao bairro do José Pinheiro-5486784.wav"]
'''