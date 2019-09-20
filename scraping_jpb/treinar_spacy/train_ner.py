import spacy
from sacremoses import MosesTruecaser, MosesTokenizer

import stanfordnlp

import nltk
from nltk.tokenize import sent_tokenize
from nltk import tokenize
import re

nlp = spacy.load("pt_core_news_sm")


# TENTATIVA 1:
mtr = MosesTruecaser()
mtok = MosesTokenizer(lang='pt')

tokenized_docs = [mtok.tokenize(line) for line in open('../processamento/textos.txt')]

mtr.train(tokenized_docs, save_to='textos.truecasemodel')

def pre_processamento(texto):
    novo_texto = ""
    lista = ["rua", "r.", "bairro", "avenida", "av", "travessa", "trav."]
    for palavra in texto.split():
        if (palavra.lower() in lista):
            novo_texto += palavra[0].upper() + palavra[1:] + " "
        else:
            novo_texto += palavra + " "

    return novo_texto.strip()

text = "a avenida João pessoa esta com lixo em toda parte"
# text = pre_processamento(text)
print(text)
a = mtr.truecase(text, return_str=True)
print(a)
doc = nlp(a)

for d in doc:
    print(d.text, d.pos_)

for i in doc.ents:
    print(i.text, i.label_)


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