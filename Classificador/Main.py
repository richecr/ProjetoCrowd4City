from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score, cross_val_predict

import numpy as np

import pandas as pd

tweets = pd.read_csv("tweets_testes.csv", encoding='utf-8')

# print(tweets["reclamacao"].value_counts())

pip_simples = Pipeline([
    ('counts', CountVectorizer()),
    ('classifier', MultinomialNB())
])

def avaliaModelo(clf, X, y):
    resultados = cross_val_predict(clf, X, y, cv=5)
    print(pd.crosstab(y, resultados, rownames=['Real'], colnames=['Predito'], margins=True))
    return np.mean(cross_val_score(clf, X, y, cv=5))

print(avaliaModelo(pip_simples, tweets['full_text'], tweets['reclamacao']))

'''
with open("../twitter_scraping/tweets_testes.csv", "r", encoding="utf-8") as file:
    texto = file.read()
    
    print(texto)
'''