import nltk
import re
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn import metrics
from sklearn.model_selection import cross_val_predict

# Limpa os tweets: retirando marcações, links.
def limpa_dados(instancia):
    instancia = re.sub(r"http\S+", "", instancia).lower().replace('.','').replace(';','').replace('-','').replace(':','').replace(')','')
    return (instancia)

# Função para avaliar a eficácia do modelo. 
def avaliaModelo():
    # Validando os Modelos com Validação Cruzada
    resultados = cross_val_predict(modelo, freq_tweets, classes, cv=10)
    # Medindo a acurácia média do modelo.
    print(metrics.accuracy_score(classes, resultados))
    reclamacao1 = ['não','sim']
    print (metrics.classification_report(classes, resultados, reclamacao1))
    print (pd.crosstab(classes, resultados, rownames=['Real'], colnames=['Predito'], margins=True))

# Carregando os dados.
tweets = pd.read_csv("tweets.csv", encoding='utf-8')
tests = pd.read_csv("testes.csv", encoding='utf-8')

# Limpando os dados para melhor utilização.
tweets_ = [limpa_dados(i) for i in tweets['full_text'].values]
classes = tweets['reclamacao']

# Criação do modelo e treinamento do mesmo.
vectorizer = CountVectorizer(analyzer="word")
freq_tweets = vectorizer.fit_transform(tweets_)
modelo = MultinomialNB()
modelo.fit(freq_tweets,classes)

# Avaliando o modelo.
avaliaModelo()

# Realizando testes no modelo.
freq_testes = vectorizer.transform(tests['full_text'].values)
predicted = modelo.predict(freq_testes)
print(predicted)

# Verificando resultados dos testes.
print(np.mean(predicted == tests['reclamacao']))