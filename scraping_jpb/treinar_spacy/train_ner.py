import spacy
from sacremoses import MosesTruecaser, MosesTokenizer

# import stanfordnlp

import nltk
from nltk.tokenize import sent_tokenize
from nltk import tokenize
import re

class Truecasing():
    def __init__(self):
        self.nlp = spacy.load("pt_core_news_sm")
        self.nlp.Defaults.stop_words |= {"vamos", "olha", "pois", "tudo", "coisa", "toda", "tava", "pessoal", "dessa", "resolvido", "aqui", "gente", "tá", "né", "calendário", "jpb", "agora", "voltar", "lá", "hoje", "aí", "ainda", "então", "vai", "porque", "moradores", "fazer", "prefeitura", "todo", "vamos", "problema", "fica", "ver", "tô"}
        self.stop_words_spacy = self.nlp.Defaults.stop_words
        self.mtr = MosesTruecaser()
        self.mtok = MosesTokenizer(lang="pt")
        tokenized_docs = [self.mtok.tokenize(line) for line in open('./textos.txt')]
        self.mtr.train(tokenized_docs, save_to='textos.truecasemodel')

    def truecasing(self, texto):
        texto = self.remove_stop_words(texto)
        # texto = self.pre_processamento(texto)
        texto = self.mtr.truecase(texto, return_str=True)
        return texto

    def pre_processamento(self, texto):
       # texto = self.remove_stop_words(texto)
        novo_texto = ""
        lista = ["rua", "r.", "bairro", "avenida", "av", "travessa", "trav."]
        prox = False
        for palavra in texto.split():
            if (prox):
                novo_texto += palavra[0].upper() + palavra[1:] + " "
                prox = False
            elif (palavra.lower() in lista):
                novo_texto += palavra[0].upper() + palavra[1:] + " "
                prox = True
            else:
                novo_texto += palavra + " "

        return novo_texto.strip()
    
    def remove_stop_words(self, texto):
        saida = ""
        for palavra in texto.split():
            if (palavra.lower() not in self.stop_words_spacy):
                saida += palavra + " "
        s = saida.strip()
        return s

'''
nlp = spacy.load("pt_core_news_sm")
text = "É hora do calendário Olha só recebi uma correspondência chamar a polícia o SAMU pedir uma pizza não são tarefas fáceis para quem mora no conjunto Colinas do Sol no bairro das Malvinas é que as ruas não têm nome aí fica complicado né Laisa grisi foi lá conversar com os moradores e hoje é dia de calendário JPB e a gente receber um chamado muito especial do pessoal Olha só do conjunto Colinas do Sol bairro das Malvinas sendo que a gente passou uns 10 minutos rodando aqui sem conseguir achar a rua porque a única referência que a gente tinha era assim ó quadra K Lote 10 Quadra k Lote 10 viu Nossa assistente motorista Rodotrem mais o carro não foi Gil foi um pouquinho viu aí você escutou quando o pessoal gritou pessoal gritou né se não tinha passado Então vamos falar com o pessoal minha gente porque se vocês não tivesse gritado a gente ia passar direto aqui Como assim quadra K Lote 10 quem acha esse endereço é difícil de encontrar correspondência a gente não tem vai completar três anos que a gente recebeu esse conjunto nós não temos nome de rua nós não temos transporte urbano nós não temos uma pracinha nós não temos posto de saúde a situação é precária mesmo de você ligou para gente né chamou o calendário Por que a principal dificuldade são essas ruas não têm nome e aí não recebe correspondência para dizer assim um ponto de referência fica difícil vai receber uma visita faz como a gente fica o DETRAN Rua da conta porque tem uma Kombi na rua vai para rua né tem que esperar na rua nessa rua quem acha tem que esperar na rua vocês já já falaram foram atrás vocês sabem quem procurar Não não vou dizer que a gente não procurou sobre o endereço não porque a gente não sabe quem procurar só um minutinho agora você eu procurei eu fui na serra me disseram que depois que foi entregue Não tem nada a ver com isso com essa é a pino é aí falaram na prefeitura eu fui na prefeitura diz que o responsável não tava no dia isso aqui foi o que um ano atrás acho um ano atrás depois disso eu não procurei mais vocês não sabem nem aqui recorrer a quem recorrer não sabemos que já tem 3 anos que vocês não venham carteira aí a gente sabe que existe mas aqui não nunca viram mas a gente é essa a gente olhar as correspondências não vem para aqui a gente só tem água e luz porque tem que pagar então direito né é divisa na hora a leitura não faz na hora leitura então se for conta para pagar olha a conta da Cagepa e a conta da Energisa chegam nas casas agora vem aqui ó Rua Projetada 100 o nome da rua Se for para receber uma correspondência para ficar mais garantido ."
t = Truecasing()
doc = t.truecasing(text.lower())
# print(a)
ents_loc = [entity for entity in doc.ents if entity.label_ == "LOC" or entity.label_ == "GPE"]
print(ents_loc)
'''


'''
nlp = spacy.load("pt_core_news_sm")
nlp.Defaults.stop_words |= {"vamos", "olha", "pois", "tudo", "coisa", "toda", "tava", "pessoal", "dessa", "resolvido", "aqui", "gente", "tá", "né", "calendário", "jpb", "agora", "voltar", "lá", "hoje", "aí", "ainda", "então", "vai", "porque", "moradores", "fazer", "prefeitura", "todo", "vamos", "problema", "fica", "ver", "tô"}
stop_words_spacy = nlp.Defaults.stop_words
def remove_stop_words(texto):
        saida = ""
        for palavra in texto.split():
            if (palavra.lower() not in stop_words_spacy):
                saida += palavra + " "
        s = saida.strip()
        return s

# TENTATIVA 1:
mtr = MosesTruecaser()
mtok = MosesTokenizer(lang='pt')

tokenized_docs = [mtok.tokenize(line) for line in open('./textos.txt')]
mtr.train(tokenized_docs, save_to='textos.truecasemodel')

text = "É hora do calendário Olha só recebi uma correspondência chamar a polícia o SAMU pedir uma pizza não são tarefas fáceis para quem mora no conjunto Colinas do Sol no bairro das Malvinas é que as ruas não têm nome aí fica complicado né Laisa grisi foi lá conversar com os moradores e hoje é dia de calendário JPB e a gente receber um chamado muito especial do pessoal Olha só do conjunto Colinas do Sol bairro das Malvinas sendo que a gente passou uns 10 minutos rodando aqui sem conseguir achar a rua porque a única referência que a gente tinha era assim ó quadra K Lote 10 Quadra k Lote 10 viu Nossa assistente motorista Rodotrem mais o carro não foi Gil foi um pouquinho viu aí você escutou quando o pessoal gritou pessoal gritou né se não tinha passado Então vamos falar com o pessoal minha gente porque se vocês não tivesse gritado a gente ia passar direto aqui Como assim quadra K Lote 10 quem acha esse endereço é difícil de encontrar correspondência a gente não tem vai completar três anos que a gente recebeu esse conjunto nós não temos nome de rua nós não temos transporte urbano nós não temos uma pracinha nós não temos posto de saúde a situação é precária mesmo de você ligou para gente né chamou o calendário Por que a principal dificuldade são essas ruas não têm nome e aí não recebe correspondência para dizer assim um ponto de referência fica difícil vai receber uma visita faz como a gente fica o DETRAN Rua da conta porque tem uma Kombi na rua vai para rua né tem que esperar na rua nessa rua quem acha tem que esperar na rua vocês já já falaram foram atrás vocês sabem quem procurar Não não vou dizer que a gente não procurou sobre o endereço não porque a gente não sabe quem procurar só um minutinho agora você eu procurei eu fui na serra me disseram que depois que foi entregue Não tem nada a ver com isso com essa é a pino é aí falaram na prefeitura eu fui na prefeitura diz que o responsável não tava no dia isso aqui foi o que um ano atrás acho um ano atrás depois disso eu não procurei mais vocês não sabem nem aqui recorrer a quem recorrer não sabemos que já tem 3 anos que vocês não venham carteira aí a gente sabe que existe mas aqui não nunca viram mas a gente é essa a gente olhar as correspondências não vem para aqui a gente só tem água e luz porque tem que pagar então direito né é divisa na hora a leitura não faz na hora leitura então se for conta para pagar olha a conta da Cagepa e a conta da Energisa chegam nas casas agora vem aqui ó Rua Projetada 100 o nome da rua Se for para receber uma correspondência para ficar mais garantido ."
text = remove_stop_words(text)
# text = pre_processamento(text)
print(text)
a = mtr.truecase(text.lower(), return_str=True)
print(a)
doc = nlp(a)
for i in doc.ents:
    print(i.text, i.label_)
'''

'''
text = "a avenida joão pessoa esta com lixo em toda parte"
def truecasing_by_sentence_segmentation(input_text):
    # split the text into sentences
    sentences = tokenize.word_tokenize(input_text, language="portuguese")
    # capitalize the sentences
    print(sentences)
    sentences_capitalized = [s.capitalize() for s in sentences]
    # join the capitalized sentences
    text_truecase = re.sub(" (?=[\.,'!?:;])", "", ' '.join(sentences_capitalized))
    return text_truecase

print(truecasing_by_sentence_segmentation(text))

from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
def truecasing_by_pos(input_text):
    # tokenize the text into words
    words = nltk.word_tokenize(text, language="portuguese")
    # apply POS-tagging on words
    tagged_words = nltk.pos_tag([word.lower() for word in words])
    # apply capitalization based on POS tags
    capitalized_words = [w.capitalize() if t in ["NN","NNS"] else w for (w,t) in tagged_words]
    # capitalize first word in sentence
    capitalized_words[0] = capitalized_words[0].capitalize()
    # join capitalized words
    text_truecase = re.sub(" (?=[\.,'!?:;])", "", ' '.join(capitalized_words))
    return text_truecase

print(truecasing_by_pos(text))
'''

'''
class Extrator:
    
    def __init__(self, text):
        self.text = text

    def named_entities(self):
        # word_tokenize should work well for most non-CJK languages
        text = nltk.word_tokenize(self.text)
        
        # TODO: this works only for english. Stanford's pos tagger supports
        # more languages
        # http://www.nltk.org/api/nltk.tag.html#module-nltk.tag.stanford
        # http://stackoverflow.com/questions/1639855/pos-tagging-in-german
        # PT corpus http://aelius.sourceforge.net/manual.html
        # 
        pos_tag = nltk.pos_tag(text)
        
        nes = nltk.ne_chunk(pos_tag)
        return nes



    def find_entities(self):
        """Parse text and tokenize it.
        """
        nes = self.named_entities()
        for ne in nes:
            if type(ne) is nltk.tree.Tree:
                if ne.label() in ['GPE', 'PERSON', 'ORGANIZATION']:
                    self.places.append(u' '.join([i[0] for i in ne.leaves()]))
'''

'''

# Testar '.upper()' e '.title()'
# E ver qual é melhor.
# texto = remove_stop_words(texto.upper())
# print(texto)
words = tokenize.word_tokenize(input_text, language="portuguese")
predsTexto = model.predict(words)
# print(predsTexto)
ents_loc = []
texto_ = texto.split()
for pos in range(len(predsTexto)):
    if (predsTexto[pos] == "B-LOCAL" or predsTexto[pos] == "I-LOCAL"):
        ents_loc.append(texto_[pos])

print(ents_loc)
# Testar título com Spacy.
titulo = titulo.split("-")[0]
print(titulo)
doc_titulo = nlp(titulo)
ents_loc1 = [entity for entity in doc_titulo.ents if entity.label_ == "LOC" or entity.label_ == "GPE"]


'''