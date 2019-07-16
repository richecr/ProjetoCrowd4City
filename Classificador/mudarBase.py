import os
import pandas as pd
import csv

def escrever(text, resp):
    row = [[text, resp]]
    # write to csv
    with open('../twitter_scraping/novos_tweets.csv', 'a', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(row)

# write to csv
fileR = pd.read_csv('../twitter_scraping/tweets_testes.csv', encoding="utf-8")

for t in fileR.itertuples(0):
    if (t[1] == "sim"):
        escrever(t[0], "pos")
    else:
        escrever(t[0], "neg")