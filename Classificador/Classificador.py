import nltk
import re
import pandas as pd
from nltk import word_tokenize
from sklearn import metrics
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_predict
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

### Carregando dados.
data = pd.read_csv('tweets.csv', encoding='utf-8')

### Pre-Processamento dos dados.
# Remove duplicadas, caso exista.
data.drop_duplicates(['full_text'], inplace=True)

# Separando os dados de sua classificação
tweets = data['full_text']
reclamacao = data['reclamacao']

# Instala bibliotecas e baixa a base de dados
nltk.download('stopwords')
nltk.download('rslp')

#Funções de Pre-Processamento.
# Função que remove as palavras consideradas irrelevantes para o conjunto de resultados.
def RemoveStopWords(instancia):
    stopwords = set(nltk.corpus.stopwords.words('portuguese'))
    palavras = [i for i in instancia.split() if not i in stopwords]
    return (" ".join(palavras))

# Função para o processo de reduzir palavras flexionadas.
def Stemming(instancia):
    stemmer = nltk.stem.RSLPStemmer()
    palavras = []
    for w in instancia.split():
        palavras.append(stemmer.stem(w))
    return (" ".join(palavras))

# Função que faz a limpeza dos tweets: Removendo links, marcações e etc.
def limpa_dados(instancia):
    instancia = re.sub(r"http\S+", "", instancia).lower().replace('.','').replace(';','').replace('-','').replace(':','').replace(')','')
    return (instancia)

# Aplicando funções de pre-processamento.
def preprocessamento(instancia):
    stemmer = nltk.stem.RSLPStemmer()
    instancia = re.sub(r"http\S+", "", instancia).lower().replace('.','').replace(';','').replace('-','').replace(':','').replace(')','')
    stopwords = set(nltk.corpus.stopwords.words('portuguese'))
    palavras = [stemmer.stem(i) for i in instancia.split() if not i in stopwords]
    return (" ".join(palavras))

# Aplica a função em todos os dados
tweets = [preprocessamento(i) for i in tweets]

# Testando o modelo com algumas instâncias simples
testes = pd.read_csv('testes.csv', encoding='utf-8')
r = testes['reclamacao']
testes = testes['full_text']

# Aplica a função de Pré-processamento nos dados de testes.
testes = [preprocessamento(i) for i in testes]

## Modelo usando pipelines.
pipeline_simples = Pipeline([
  ('counts', CountVectorizer()),
  ('classifier', MultinomialNB())
])

# Gera modelo simples.
pipeline_simples.fit(tweets, reclamacao)
pipeline_simples.steps

# Validando os Modelos com Validação Cruzada
resultados = cross_val_predict(pipeline_simples, tweets, reclamacao, cv=10)

# Função para avaliar a eficácia do modelo. 
def avaliaModelo():
    # Validando os Modelos com Validação Cruzada
    resultados = cross_val_predict(pipeline_simples, tweets, reclamacao, cv=10)
    # Medindo a acurácia média do modelo.
    print(metrics.accuracy_score(reclamacao, resultados))
    reclamacao1 = ['neg','pos']
    print (metrics.classification_report(reclamacao, resultados, reclamacao1))
    print (pd.crosstab(reclamacao, resultados, rownames=['Real'], colnames=['Predito'], margins=True))

# Medindo a acurácia média do modelo.
avaliaModelo()

predicoes = pipeline_simples.predict(testes)
print(predicoes)

print(np.mean(r == predicoes))

'''
### Bigrams
vectorizer = CountVectorizer(ngram_range=(1,2))
freq_tweets = vectorizer.fit_transform(tweets)
modelo = MultinomialNB()
modelo.fit(freq_tweets, reclamacao)

resultados = cross_val_predict(modelo, freq_tweets, reclamacao, cv=10)

print(metrics.accuracy_score(reclamacao, resultados))

reclamacao1 = ['não','sim']
print (metrics.classification_report(reclamacao, resultados, reclamacao1))

print (pd.crosstab(reclamacao, resultados, rownames=['Real'], colnames=['Predito'], margins=True))

print(modelo.predict(freq_testes))

---------

### Criando o modelo.
# Instancia o objeto que faz a vetorização dos dados de texto.
vectorizer = CountVectorizer(analyzer="word")

# Aplica o vetorizador nos dados de texto
freq_tweets = vectorizer.fit_transform(tweets)
type(freq_tweets)


modelo = MultinomialNB()
modelo.fit(freq_tweets, reclamacao)

# Formato (Linhas, Colunas) da matriz
freq_tweets.shape
freq_tweets.A

# Aplica a função de Pré-processamento nos dados de testes.
testes = [preprocessamento(i) for i in testes]

# Transforma os dados de teste em vetores de palavras.
freq_testes = vectorizer.transform(testes)

# Probabilidades de cada classe
print (modelo.classes_)
modelo.predict_proba(freq_testes).round(2)

# Fazendo a classificação com o modelo treinado.
for t, c in zip (testes,modelo.predict(freq_testes)):
    print (t +", "+ c)

'''