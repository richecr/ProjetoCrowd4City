import numpy as np
import pandas as pd
from gensim.models.doc2vec import TaggedDocument, Doc2Vec
from sklearn.base import BaseEstimator
from sklearn import utils as skl_utils
from tqdm import tqdm
import multiprocessing
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

data = pd.read_csv('textos_videos.csv')

X = data['texto']
y = data['classes_problema']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

class Doc2VecTransformer(BaseEstimator):
    def __init__(self, vector_size=100, learning_rate=0.02, epochs=20):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self._model = None
        self.vector_size = vector_size
        self.workers = multiprocessing.cpu_count() - 1

    def fit(self, df_x, df_y=None):
        tagged_x = [TaggedDocument(row.split(), [index]) for index, row in enumerate(df_x)]
        model = Doc2Vec(documents=tagged_x, vector_size=self.vector_size, workers=self.workers)

        for epoch in range(self.epochs):
            model.train(skl_utils.shuffle([x for x in tqdm(tagged_x)]), total_examples=len(tagged_x), epochs=1)
            model.alpha -= self.learning_rate
            model.min_alpha = model.alpha

        self._model = model
        return self

    def transform(self, df_x):
        return np.asmatrix(np.array([self._model.infer_vector(row.split())
                                     for index, row in enumerate(df_x)]))

class Text2TfIdfTransformer(BaseEstimator):
    def __init__(self):
        self._model = TfidfVectorizer()
        pass

    def fit(self, df_x, df_y=None):
        df_x = df_x.apply(lambda x : x)
        self._model.fit(df_x)
        return self

    def transform(self, df_x):
        return self._model.transform(df_x)

# tfidf_transformer = Text2TfIdfTransformer()
# tfidf_vectors = tfidf_transformer.fit(df_x).transform(df_x)
# print(doc2vec_features)

from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb

# Random Forest Classifier
# pl_random_forest = Pipeline(steps=[('doc2vec',Doc2VecTransformer()),
#                                    ('random_forest', RandomForestClassifier())])
# scores = cross_val_score(pl_random_forest, X, y, cv=5,scoring='accuracy')
# print('Accuracy for RandomForest : ', scores.mean())

# Logistic Regression
# pl_log_reg = Pipeline(steps=[('doc2vec',Doc2VecTransformer()),
#                              ('log_reg', LogisticRegression(multi_class='multinomial', solver='saga', max_iter=100))])
# scores = cross_val_score(pl_log_reg, X, y, cv=5,scoring='accuracy')
# print('Accuracy for Logistic Regression: ', scores.mean())

# XGBoost
pl_xgb_tf_idf = Pipeline(steps=[('tfidf', Text2TfIdfTransformer()),
                         ('xgboost', xgb.XGBClassifier(objective='multi:softmax'))])
scores = cross_val_score(pl_xgb_tf_idf, X, y, cv=5)
print('Accuracy for XGBoost Classifier : ', scores.mean())
