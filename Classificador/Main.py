import pandas as pd
tweets = pd.read_csv("../twitter_scraping/tweets_testes.csv", sep='\t', )
print(tweets.head())


'''
with open("../twitter_scraping/tweets_testes.csv", "r", encoding="utf-8") as file:
    texto = file.read()
    
    print(texto)
'''