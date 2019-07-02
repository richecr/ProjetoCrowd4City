from textblob.classifiers import NaiveBayesClassifier
import pandas as pd

tweets = pd.read_csv("tweets.csv", encoding='utf-8')

def preprocessa(tweets, reclamacao):
    pass
    # TODO

c = NaiveBayesClassifier(preprocessa(tweets['full_text'], tweets['reclamacao']))