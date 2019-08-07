from os import path
import speech_recognition as sr
import os
import csv

fields = ["titulo", "texto"]
f = csv.writer(open('./textos_videos1.csv', 'w', encoding='utf-8'))
f.writerow(fields)
f.writerow(['abraço', 'é á pão calendário'])