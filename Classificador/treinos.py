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

indice = acharIndiceTweet("I liked a @YouTube video https://t.co/uWTA1QLoaa jogando lixo na rua")

cont = 0
for t in fileR.itertuples(270):
    if (cont == indice):
        print(t[2])
        resp = input("Sim ou não: ")
        if (resp == "s"):
            escrever(t[2], "sim")
        elif (resp == "p"):
            continue
        else:
            escrever(t[2], 'não')
    else:
        cont += 1