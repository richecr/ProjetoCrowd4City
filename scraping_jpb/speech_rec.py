import os
import csv
import json
from os import path
from time import sleep
import speech_recognition as sr

audios_falharam = []
def escreve():
    print("Falhou")
    with open("./audios_falharam.json", 'w', encoding='utf-8') as af:
        json.dump(audios_falharam, af)

fields = ["titulo", "texto"]
f = csv.writer(open('./textos_videos.csv', 'w', encoding='utf-8'))
f.writerow(fields)

r = sr.Recognizer()

PATH_AUDIOS = path.dirname(path.realpath(__file__)) + "/audios/"

lista_audios = os.listdir(PATH_AUDIOS)
cont = 1
iniciar_em = 0

for audio in lista_audios:
    if (iniciar_em > 0):
        iniciar_em -= 1
    else:
        print("Começa")
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
            audios_falharam.append(audio1)
            escreve()
            continue