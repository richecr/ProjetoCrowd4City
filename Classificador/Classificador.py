import re

class Classificador():
    def __init__(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train
        self.chaves_seguranca = [("segurança", 5), ("perigo", 3), ("perigoso", 3), ("falta", 1), ("bandido", 5), ("bandidos", 5), ("ladrão", 5), ("ladrões", 5), ("andar", 3), ("ruim", 2)]
        self.chaves_lixos = [("lixo", 5), ("higiene", 4), ("lixeira", 5), ("falta", 1), ("jogado", 3), ("entulho", 4)]
        self.chaves_saude = [("saúde", 5), ("hospitais", 5), ("hospital", 5), ("médico", 5), ("fechado", 3), ("posto", 4), ("enfermeira", 5)]
        self.chaves_educacao = [("educação", 5), ("escolas", 5), ("escola", 5), ("universidades", 5), ("universidade", 5), ("falta", 1), ("ruim", 2), ("professores", 5), ("merenda", 4)]

    def predicts(self, x_test):
        predicts = []
    
    def chave(self, texto):
        palavras = texto.split(" ")

        pSeguranca = self.pontosSeguranca(palavras)
        pLixo = self.pontosLixo(palavras)
        pSaude = self.pontosSaude(palavras)
        pEducacao = self.pontosEducacao(palavras)

        if (pSeguranca > pLixo):
            return "SEGURANÇA"
        elif (pSaude > pLixo):
            return "SAÚDE"
        elif (pEducacao > pLixo):
            return "EDUCAÇÃO"
        else:
            return "LIXO"

    def pontosSeguranca(self, texto):
        pontos = 0
        for palavra in texto:
            pontos += self.contemSeguranca(palavra)
        
        return pontos

    def contemSeguranca(self, palavra):
        for tupla in self.chaves_seguranca:
            if (re.search(tupla[0], palavra) != None):
                return tupla[1]

        return 0

    def pontosLixo(self, texto):
        pontos = 0
        for palavra in texto:
            pontos += self.contemLixo(palavra)
        
        return pontos

    def contemLixo(self, palavra):
        for tupla in self.chaves_lixos:
            if (re.search(tupla[0], palavra) != None):
                return tupla[1]

        return 0
    
    def pontosSaude(self, texto):
        pontos = 0
        for palavra in texto:
            pontos += self.contemSaude(palavra)
        
        return pontos

    def contemSaude(self, palavra):
        for tupla in self.chaves_saude:
            if (re.search(tupla[0], palavra) != None):
                return tupla[1]

        return 0

    def pontosEducacao(self, texto):
        pontos = 0
        for palavra in texto:
            pontos += self.contemEducacao(palavra)
        
        return pontos
    
    def contemEducacao(self, palavra):
        for tupla in self.chaves_educacao:
            if (re.search(tupla[0], palavra) != None):
                return tupla[1]
        
        return 0

c = Classificador([], [])

print( c.chave("rua com hospital fechado") )
print( c.chave("rua sem segurança alguma") )
print( c.chave("rua cheio de lixo, não dá nem pra andar") )
print( c.chave("minha rua é um lixo de segurança, é bastante perigoso andar por aqui") )
print( c.chave("Não tem uma escola boa nessa rua"))
print( c.chave("Não tem uma escola nessa rua"))
print( c.chave("escolas sem merendas, sem professores") )