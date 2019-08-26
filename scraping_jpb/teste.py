import os
import csv
import json
from os import path
from time import sleep

PATH_AUDIOS = path.dirname(path.realpath(__file__)) + "/audios/"

lista_audios = os.listdir(PATH_AUDIOS)

for audio in lista_audios:
    print(audio)