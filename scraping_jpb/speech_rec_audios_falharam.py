import os
import csv
import json
from os import path
from time import sleep
import speech_recognition as sr

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
                print(audio)
                continue