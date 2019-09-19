import spacy
from sacremoses import MosesTruecaser, MosesTokenizer

nlp = spacy.load("pt_core_news_sm")

mtr = MosesTruecaser()
mtok = MosesTokenizer(lang='en')

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

text = "no bairro bodocongó a rua joão sergio de almeida esta cheio de lixos"
text = pre_processamento(text)
print(text)
a = mtr.truecase(text.title())
print(a)
doc = nlp(" ".join(a))

for i in doc.ents:
    print(i.text, i.label_)


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