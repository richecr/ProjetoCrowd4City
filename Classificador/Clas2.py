from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import confusion_matrix

import numpy as np
import itertools
import matplotlib.pyplot as plt
import pandas as pd

tweets = pd.read_csv("tweets_testes.csv", encoding='utf-8')
tests = pd.read_csv("testes.csv", encoding='utf-8')

with open("tweets_testes.csv", "r", encoding='utf-8') as text_file:
    data = text_file.read().split('\n')

def preprocessing_data(data):
    processing_data = []
    for single_data in data:
        if (single_data == ""):
            continue
        else:
            processing_data.append(single_data.split(",      "))

    return processing_data

def training_step(data, vectorizer):
    training_text = [data[0] for data in data]
    training_result = [data[1] for data in data]
    training_text = vectorizer.fit_transform(training_text)

    return BernoulliNB().fit(training_text, training_result)

values = preprocessing_data(data)


vectorizer = CountVectorizer(binary = 'true')
classifier = training_step(values, vectorizer)

result = classifier.predict(vectorizer.transform(["Escola municipal do bairro mangabeira esta sem aulas ha mais de semanas"]))
print(result[0])
