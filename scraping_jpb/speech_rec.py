from os import path
import speech_recognition as sr
import os
import csv
from time import sleep

fields = ["titulo", "texto"]
f = csv.writer(open('./textos_videos1.csv', 'w', encoding='utf-8'))
f.writerow(fields)

r = sr.Recognizer()

PATH_AUDIOS = path.dirname(path.realpath(__file__)) + "/audios/"

lista_audios = os.listdir(PATH_AUDIOS)
cont = 1
for audio in lista_audios:
    audio1 = audio
    caminho = PATH_AUDIOS + audio
    with sr.AudioFile(caminho) as source:
        audio = r.record(source, duration=198)
    texto = r.recognize_google(audio, language="pt-br")
    titulo = audio1

    f.writerow([titulo, texto])
    print(cont, "concluído!")
    cont += 1
    sleep(5)