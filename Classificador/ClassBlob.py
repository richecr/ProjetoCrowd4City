from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import pandas as pd

tweets = pd.read_csv("tweets.csv", encoding='utf-8')
testes = [
    ("Gostaria de pedir uma ajuda. A Escola Municipal Érico Verissimo que fica localizada no bairro Fazenda Botafogo  perto de Acari. Os alunos estão sem aula e ficaram até sexta porque marginais roubaram os fios da escola ela 4° vez esse ano","sim"),
    ("Rua joao sergio com lixo em toda parte","sim"),
    ("escola na rua são josé está sem funcionar","sim"),
    ("escola sem aula","sim"),
    ("Escola municipal do bairro mangabeira esta sem aulas ha mais de semanas","sim"),
    ("pessoas são um lixo","não"),
    ("ALUNOS SEM AULA POR FALTA DE ENERGIA País de alunos da escola municipal Rubens Machado no bairro Vale Verde, aguardam conserto do transformador para que a escola volte a ter aulas normalmente. A resposta que... https://t.co/GRXA2Sv3Lw","sim")
]

def preprocessa(tweets, reclamacao):
    saida = []
    for i in range(len(tweets)):
        saida.append((tweets[i], reclamacao[i]))

    return saida

tw = preprocessa(tweets['full_text'], tweets['reclamacao'])
c = NaiveBayesClassifier(tw)

print(c.accuracy(testes))