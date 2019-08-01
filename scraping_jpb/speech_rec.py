from os import path
import speech_recognition as sr
import os
import csv

fields = ["texto"]
f = csv.writer(open('./textos_videos.csv', 'w'))
f.writerow(fields)

r = sr.Recognizer()

PATH_AUDIOS = path.dirname(path.realpath(__file__)) + "/audios/"

lista_audios = os.listdir(PATH_AUDIOS)
for audio in lista_audios:
    caminho = PATH_AUDIOS + audio
    with sr.AudioFile(caminho) as source:
        audio = r.record(source)
    texto = r.recognize_google(audio, language="pt-br")

    f.writerow([texto])