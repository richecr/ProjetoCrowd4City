from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.model_selection import cross_val_score, cross_val_predict, train_test_split
from sklearn.metrics import accuracy_score

import numpy as np

import pandas as pd

# Carregando os arquivos.
tweets = pd.read_csv("tweets.csv", encoding='utf-8')
tests = pd.read_csv("testes.csv", encoding='utf-8')

# Criando o classificador.
pip_simples = Pipeline([
    ('counts', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', SGDClassifier(loss='hinge', penalty='l2',
                          alpha=1e-3, random_state=42,
                          max_iter=5, tol=None))
])

# treinando.
pip_simples.fit(tweets['full_text'], tweets['reclamacao'])

# Função para avaliar a eficácia do modelo. 
def avaliaModelo(clf, X, y):
    resultados = cross_val_predict(clf, X, y, cv=5)
    print(pd.crosstab(y, resultados, rownames=['Real'], colnames=['Predito'], margins=True))
    return np.mean(cross_val_score(clf, X, y, cv=5))

print(avaliaModelo(pip_simples, tweets['full_text'], tweets['reclamacao']))

# Testando o modelo.
predicted = pip_simples.predict(tests['full_text'])
print(predicted)

# Precisão do modelo.
print(np.mean(predicted == tests['reclamacao']))

'''
with open("../twitter_scraping/tweets_testes.csv", "r", encoding="utf-8") as file:
    texto = file.read()
    
    print(texto)
'''