from textblob.classifiers import NaiveBayesClassifier
import pandas as pd

tweets = pd.read_csv("tweets.csv", encoding='utf-8')

def preprocessa(tweets, reclamacao):
    # TODO

c = NaiveBayesClassifier(tweets['full_text'])