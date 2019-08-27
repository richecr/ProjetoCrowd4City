import nltk
import pandas as pd
from nltk.corpus import stopwords
from sklearn.decomposition import NMF, LatentDirichletAllocation
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

def display_topics(model, feature_names, no_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print("Topic %d:" % (topic_idx))
        print(" ".join([feature_names[i]
                        for i in topic.argsort()[:-no_top_words - 1:-1]]))

dataset = pd.read_csv("../textos_videos.csv", encoding="utf-8")
documents = dataset['texto']

# Stop Words
nltk.download('stopwords')
stop_words = stopwords.words('portuguese')
stop_words = stop_words + ["tudo", "aqui", "gente", "tá", "né", "calendário", "jpb", "agora", "voltar", "lá", "hoje", "aí", "ainda", "então", "vai", "porque", "moradores", "fazer", "rua", "bairro", "prefeitura", "todo", "vamos", "problema", "fica", "ver", "tô"]

no_features = 1000
no_topics = 5
no_top_words = 10

def nmf():
    # NMF is able to use tf-idf
    tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, max_features=no_features, stop_words=stop_words)
    tfidf = tfidf_vectorizer.fit_transform(documents)
    tfidf_feature_names = tfidf_vectorizer.get_feature_names()

    # Run NMF
    nmf = NMF(n_components=no_topics, random_state=1, alpha=.1, l1_ratio=.5, init='nndsvd').fit(tfidf)
    display_topics(nmf, tfidf_feature_names, no_top_words)

def lda():
    # LDA can only use raw term counts for LDA because it is a probabilistic graphical model
    tf_vectorizer = CountVectorizer(max_df=0.99, min_df=2, max_features=no_features, stop_words=stop_words)
    tf = tf_vectorizer.fit_transform(documents)
    tf_feature_names = tf_vectorizer.get_feature_names()

    # Run LDA
    lda = LatentDirichletAllocation(n_components=no_topics, max_iter=10, learning_method='online', learning_offset=50.,random_state=0).fit(tf)
    display_topics(lda, tf_feature_names, no_top_words)

    print(lda.score(tf))
    print(lda.perplexity(tf))

print("Topic Modeling: NMF")
nmf()
print("---------------------------")
print("Topic Modeling LDA")
lda()

'''
### Carregando dados.
data = pd.read_csv('../textos_videos.csv', encoding='utf-8')
textos = data['texto']

# Stop Words
nltk.download('stopwords')
stop_words = stopwords.words('portuguese')
stop_words = stop_words + ["tudo", "aqui", "gente", "tá", "né", "calendário", "jpb", "agora", "voltar", "lá", "hoje", "aí", "ainda", "então", "vai", "porque", "moradores", "fazer", "rua", "bairro", "prefeitura", "todo", "vamos", "problema", "fica", "ver", "tô"]

no_features = 1000

# 
tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, max_features=no_features, stop_words=stop_words)
tfidf = tfidf_vectorizer.fit_transform(textos)
tfidf_feature_names = tfidf_vectorizer.get_feature_names()

no_topics = 5

nmf = NMF(n_components=no_topics, random_state=1, alpha=.1, l1_ratio=.5, init='nndsvd').fit(tfidf)

def display_topics(model, feature_names, no_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print("Topic %d:" % (topic_idx))
        print(" ".join([feature_names[i] for i in topic.argsort()[:-no_top_words - 1:-1]]))

no_top_words = 10
display_topics(nmf, tfidf_feature_names, no_top_words)
'''