import oauth2
import urllib.parse
import json

class Twitter:

    def __init__(self, consumer_key, consumer_secret, token_key, token_secret):
        self.conexao(consumer_key, consumer_secret, token_key, token_secret)

    def conexao(self, consumer_key, consumer_secret, token_key, token_secret):
        self.consumer = oauth2.Consumer(consumer_key, consumer_secret)
        self.token = oauth2.Token(token_key, token_secret)
        self.cliente = oauth2.Client(self.consumer, self.token)

    def novoTweet(self, novo_tweet):
        query_codificada = urllib.parse.quote(novo_tweet, safe='')  # Para pesquisar com sinais(ex: #, acentos etc).
        requisicao = self.cliente.request('https://api.twitter.com/1.1/statuses/update.json?status=' + query_codificada,
                                     method='POST')
        decodificar = requisicao[1].decode()
        objeto = json.loads(decodificar)
        return objeto

    def search(self, query, lang):
        query_codificada = urllib.parse.quote(query, safe='')  # Para pesquisar com sinais(ex: #, acentos etc).
        requisicao = self.cliente.request('https://api.twitter.com/1.1/search/tweets.json?q=' + query_codificada + '&lang=' + lang)
        decodificar = requisicao[1].decode()
        objeto = json.loads(decodificar)
        tweetes = objeto['statuses']
        return tweetes
