import os
import pandas as pd
import csv

def escrever(text, resp):
    row = [[text, resp]]
    # write to csv
    with open('../twitter_scraping/tweets_testes.csv', 'a', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(row)

# write to csv
fileR = pd.read_csv('../twitter_scraping/dados/lixo/dados.csv', encoding="utf-8")

tweets = []

def acharIndiceTweet(tweet_text):
    cont = 0
    for t in fileR.itertuples(0):
        if (tweet_text in t[1]):
            print(t)
            return cont
        else:
            cont += 1
    return cont

indice = acharIndiceTweet("o menino que eu quero me viu na rua hj um verdadeiro lixo e me mandou um video com a legenda “linda dmsss”")

cont = 0
for t in fileR.itertuples(0):
    if (cont == indice):
        print(t[1])
        resp = input("Sim ou não: ")
        if (resp == "s"):
            escrever(t[1], "sim")
            os.system('cls')
        elif (resp == "n"):
            escrever(t[1], 'não')
            os.system('cls')
        else:
            os.system('cls')
            continue
    else:
        cont += 1