
from fklearn.training.classification import nlp_logistic_classification_learner
from fklearn.training.pipeline import build_pipeline
from fklearn.training.utils import log_learner_time

def training_pipeline(text_cols, target_column, vectorizer_params, logistic_params):
    return log_learner_time(
        build_pipeline(
            nlp_logistic_classification_learner(
                text_feature_cols=text_cols,
                target=target_column,
                vectorizer_params=vectorizer_params,
                logistic_params=logistic_params
            )
        ), "tweet_sentiment_analysis")