import os
import re
import csv
import nltk
import spacy
import gensim
import scipy.sparse
import pandas as pd

from string import punctuation
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

from gensim.models.coherencemodel import CoherenceModel
from gensim.utils import simple_preprocess, lemmatize
from gensim.models import LdaModel, LdaMulticore
from smart_open import smart_open
from gensim import matutils, models
from gensim import corpora
from pprint import pprint

nltk.download('stopwords')
stop_words = stopwords.words('portuguese')

stop_words = stop_words + ["vez", "vem", "olha", "pessoal", "tudo", "dia", "aqui", "gente", "tá", "né", "calendário", "jpb", "agora", "voltar", "lá", "hoje", "aí", "ainda", "então", "vai", "porque", "moradores", "fazer", "rua", "bairro", "prefeitura", "todo", "vamos", "problema", "fica", "ver", "tô"]

### Carregando dados.
data = pd.read_csv('../textos_videos.csv', encoding='utf-8')
t = data['texto']

textos = []
for texto in t:
    textos.append(texto.lower())
# print(textos)

nlp = spacy.load('pt_core_news_sm')
data_processada = []

def buscar_entidade(palavra, entidades):
    for ent in entidades:
        if (ent.text == palavra):
            return ent
    return -1

allowed_postags = ['NOUN', 'ADJ', 'PRON']
for texto in textos:
    doc_out = []
    doc = nlp(texto)
    for token in doc:
        if (token.text not in stop_words):
            if (token.pos_ in allowed_postags):
                doc_out.append(token.text)
            else:
                continue
        else:
            continue
    data_processada.append(doc_out)

# print(data_processada[0][:5])

dct = corpora.Dictionary(data_processada)

t = data_processada
corpus = [dct.doc2bow(line) for line in t]

lda_model = LdaModel(corpus=corpus,
                    id2word=dct,
                    num_topics=5, 
                    random_state=100,
                    update_every=1,
                    passes=80,
                    alpha='asymmetric',
                    per_word_topics=True)

topics = lda_model.print_topics(-1)
for topic in topics:
    print(topic)

coherence_model_lda = CoherenceModel(model=lda_model, texts=data_processada, corpus=corpus, dictionary=dct, coherence='c_v')
coherence_lda = coherence_model_lda.get_coherence()
print('\nCoherence Score LDAModel: ', coherence_lda)

print("------------------------")
mallet_path = '/home/rick/Documentos/mallet-2.0.8/bin/mallet'
ldamallet = gensim.models.wrappers.LdaMallet(mallet_path, corpus=corpus, num_topics=5, id2word=dct)
# print(ldamallet.show_topics(formatted=False))
coherence_model_ldamallet = CoherenceModel(model=ldamallet, texts=data_processada, dictionary=dct, coherence='c_v')
coherence_ldamallet = coherence_model_ldamallet.get_coherence()
print('\nCoherence Score LDAMallet: ', coherence_ldamallet)
topics = ldamallet.print_topics(-1)
for topic in topics:
    print(topic)



'''
(0, [('situação', 0.021352313167259787), ('nada', 0.017334404775571115), ('lixo', 0.01658822178854322), ('sabe', 0.013947881988290667), ('passar', 0.013603489840431637), ('carro', 0.013086901618643095), ('ninguém', 0.011938927792446333), ('vezes', 0.011192744805418436), ('faz', 0.010389163127080702), ('dá', 0.008839398461715072)])
(1, [('obra', 0.04798346553457714), ('comunidade', 0.01653446542285778), ('prazo', 0.010780918333147134), ('parte', 0.009998882806390347), ('data', 0.009552005362529327), ('mês', 0.009160987599150933), ('resposta', 0.008714110155289912), ('secretário', 0.008602390794324656), ('secretaria', 0.008099653669981008), ('dar', 0.007932074628533126)])
(2, [('escola', 0.026628748707342297), ('resolvido', 0.01809720785935884), ('ano', 0.011504653567735263), ('local', 0.00969493278179938), ('boa', 0.008725439503619441), ('ficou', 0.00814374353671148), ('muro', 0.007885211995863495), ('chegou', 0.007562047569803516), ('grande', 0.007303516028955533), ('lado', 0.006851085832471561)])
(3, [('água', 0.0330845624963272), ('casa', 0.030498912851854028), ('esgoto', 0.01974496092143151), ('situação', 0.015102544514309221), ('cagepa', 0.014044778750661104), ('chuva', 0.013986013986013986), ('resolver', 0.012928248222365869), ('buraco', 0.012340600575894693), ('tava', 0.01098901098901099), ('resolvido', 0.010636422401128283)])
(4, [('praça', 0.02206913369505578), ('coisa', 0.014265683106748766), ('tava', 0.013595074071816132), ('comunidade', 0.013107358410046942), ('vendo', 0.011766140340181674), ('quadra', 0.010790709016643297), ('certeza', 0.009876242150826069), ('fazendo', 0.009754313235383772), ('bom', 0.008839846369566542), ('ginásio', 0.008413095165518502)])

(0, '0.018*"obra" + 0.008*"situação" + 0.007*"comunidade" + 0.006*"calçamento" + 0.005*"serviço" + 0.005*"nada" + 0.005*"volta" + 0.005*"mês" + 0.005*"tava" + 0.004*"mercado"')
(1, '0.014*"escola" + 0.008*"resolvido" + 0.008*"comunidade" + 0.007*"nada" + 0.006*"lixo" + 0.006*"tava" + 0.005*"obra" + 0.005*"situação" + 0.005*"serviço" + 0.005*"muro"')
(2, '0.022*"água" + 0.015*"casa" + 0.013*"esgoto" + 0.011*"situação" + 0.007*"cagepa" + 0.007*"buraco" + 0.007*"chuva" + 0.006*"obra" + 0.005*"carro" + 0.005*"calçamento"')
(3, '0.017*"praça" + 0.013*"obra" + 0.009*"comunidade" + 0.005*"tempo" + 0.005*"nada" + 0.005*"tava" + 0.004*"sabe" + 0.004*"dá" + 0.004*"vendo" + 0.004*"resolvido"')
(4, '0.015*"escola" + 0.010*"quadra" + 0.006*"situação" + 0.006*"reforma" + 0.006*"comunidade" + 0.006*"ano" + 0.006*"tava" + 0.006*"ginásio" + 0.005*"coisa" + 0.005*"obra"')
'''