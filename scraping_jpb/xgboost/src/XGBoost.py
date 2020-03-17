from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from gensim.parsing.preprocessing import STOPWORDS
from sklearn.base import BaseEstimator
from sklearn.pipeline import Pipeline
from nltk.stem.porter import *
from nltk.stem import *
import xgboost as xgb
import pandas as pd
import numpy as np
import spacy.cli
import gensim
import spacy
import nltk

spacy.cli.download("pt_core_news_sm")
nltk.download('wordnet')

data = pd.read_csv('textos_videos.csv')

X = data['texto']
y = data['classes_problema']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Pré-processamento dos dados.

stemmer = PorterStemmer()
nlp = spacy.load('pt_core_news_sm')

# Pré-processamento dos dados.

stemmer = PorterStemmer()
nlp = spacy.load('pt_core_news_sm')

# Lematização
def lemmatize_stemming(text):
    return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))

# Colocando todas as palavras para caixa baixa.
def preprocess(text):
  return lemmatize_stemming(text.lower())

class Text2TfIdfTransformer(BaseEstimator):
    def __init__(self):
        self._model = TfidfVectorizer()
        pass

    def fit(self, x, y=None):
        x = x.apply(lambda x : preprocess(x))
        self._model.fit(x)
        return self

    def transform(self, x):
        return self._model.transform(x)

pl_xgb_tf_idf = Pipeline(steps=[('tfidf', Text2TfIdfTransformer()),
                         ('xgboost', xgb.XGBClassifier(objective='multi:softmax'))])

pl_xgb_tf_idf.fit(X_train, y_train)
p = pl_xgb_tf_idf.predict(X_test)

result = np.mean(p == y_test)
print("%.3f" % result)

# Antes de executar esse código deve retirar esse texto do documento de testes.
# p = pl_xgb_tf_idf.predict(["o calendário JPB esteve no bairro Nova Conquista em Patos no dia 26 de agosto deste ano os moradores da Rua São Vicente Olha aí as imagens tenho que conviver com a situação inusitada os postes da rede elétrica no meio da rua a gente mostrou o quanto eles atrapalhavam o trânsito de veículos e de pedestres o caso parou no Ministério Público Federal depois que nem a prefeitura nem a concessionária de energia se responsabilizava pela retirada desses postes nós Prometemos voltar dois meses depois e a repórter herta riama teve lá hoje de manhã Olá Denise hoje nós temos uma boa notícia no calendário JPB quem tá muito agradecido ao calendário são os moradores da Rua São Vicente no Conjunto Nova Conquista aqui em Patos lembra que essa rua os postes eram um bem ou no meio da Via Pois é o problema foi resolvido depois que o calendário esteve aqui deu um prazo que se venceu no último dia 26 e agora está tudo como deveria ser mas nós vamos conversar com a população que nos chamou mas que hoje que agradecer pelo problema tem sido resolvido uma dessas pessoas e a Ivanilda que foi quem me chamou aqui para mostrar esse problema que vocês tinham durante anos e agora como tá depois de tudo isso sido resolvido Agora graças a Deus foi resolvido o nosso problema né a gente tá muito feliz e É uma pena a gente ter sido preciso usar a imprensa é um problema que vinha mais de 23 anos a gente já tinha tentado resolver através de meios legais em conversa mas infelizmente eles jogaram a culpa de um para o outro de um órgão para outro até que eu resolvi mandar um e-mail para o calendário JPB Obrigada nada querida vamos falar com a Sueli que a dona de casa que relatam que ficava preocupada com as crianças que brincavam aqui na rua com aqueles potes dos carros transitavam e agora essa preocupação não existe mais as crianças podem brincar à vontade é verdade finalmente faz 15 anos que eu moro aqui eu acompanhava essa situação e depois que vocês vieram aqui em 2 dias o que me impressiona é mais isso em dois dias Eles resolveram o problema da Rede Inteira quem também tá muito feliz com essa solução desse problema é a Gisele aqui na frente da casa dela bem na frente da garagem tem um poste Quando ia sair era aquela dificuldade agora gicélia problema resolvido você que tá feliz também sim muito feliz né é Acordamos né com trabalho né do pessoal com a equipe da Energisa é meu esposo também ficou muito feliz ele disse que bom né Graças a Deus que agora vai ser fácil eu tirar e guardar o carro calendário veio o problema foi resolvido e a nossa missão Está cumprida é com você de mim 15"])
# print(p)