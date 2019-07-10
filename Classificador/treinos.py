import pandas as pd
import csv

def escrever(text, resp):
    row = [[text, resp]]
    # write to csv
    with open('../twitter_scraping/tweets_testes.csv', 'a', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(row)

# write to csv
fileR = pd.read_csv('../twitter_scraping//dados/lixo/dados.csv', encoding="utf-8")

tweets = []

# lyka chegou em casa agr ja foi botando os lixo na rua organizando a cozinha, eh disso q eu to falando
# Parei nesse tweet.
# Achar o ID desse tweets.

for t in fileR.itertuples(0):
    print(t[1])
    if (resp == "s"):
        escrever(t[1], "sim")
    elif (resp == "p"):
        continue
    else:
        escrever(t[1], 'não')

