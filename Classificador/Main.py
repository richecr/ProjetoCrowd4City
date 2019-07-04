import re
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import cross_val_score, cross_val_predict, train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

# Limpa os tweets: retirando marcações, links.
def limpa_dados(instancia):
    instancia = re.sub(r"http\S+", "", instancia).lower().replace('.','').replace(';','').replace('-','').replace(':','').replace(')','')
    return (instancia)

# Carregando os arquivos.
tweets = pd.read_csv("tweets.csv", encoding='utf-8')
tests = pd.read_csv("testes.csv", encoding='utf-8')

tweets_limpos = [limpa_dados(i) for i in tweets['full_text']]
ttweets_testes_limpos = [limpa_dados(i) for i in tests['full_text']]

# Criando o classificador.
pip_simples = Pipeline([
    ('counts', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', SGDClassifier(loss='hinge', penalty='l2',
                          alpha=1e-3, random_state=42,
                          max_iter=5, tol=None))
])

# treinando.
pip_simples.fit(tweets_limpos, tweets['reclamacao'])

# Função para avaliar a eficácia do modelo. 
def avaliaModelo():
    # Validando os Modelos com Validação Cruzada
    resultados = cross_val_predict(pip_simples, tweets_limpos, tweets['reclamacao'], cv=10)
    # Medindo a acurácia média do modelo.
    print(metrics.accuracy_score(tweets['reclamacao'], resultados))
    reclamacao1 = ['não','sim']
    print (metrics.classification_report(tweets['reclamacao'], resultados, reclamacao1))
    print (pd.crosstab(tweets['reclamacao'], resultados, rownames=['Real'], colnames=['Predito'], margins=True))

print(avaliaModelo())

# Testando o modelo.
predicted = pip_simples.predict(ttweets_testes_limpos)
print(predicted)

# Precisão do modelo.
print(np.mean(predicted == tests['reclamacao']))



'''
with open("../twitter_scraping/tweets_testes.csv", "r", encoding="utf-8") as file:
    texto = file.read()
    
    print(texto)
'''