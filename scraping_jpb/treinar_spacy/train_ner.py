from sacremoses import MosesTruecaser, MosesTokenizer

mtr = MosesTruecaser()
mtok = MosesTokenizer(lang='en')

tokenized_docs = [mtok.tokenize(line) for line in open('../processamento/textos.txt')]

mtr.train(tokenized_docs, save_to='textos.truecasemodel')

a = mtr.truecase("Quem está de volta agora com o calendário jpb hoje tem Missão Nova para nossa equipe uma praça abandonada no Ernani Sátiro aqui na capital Na verdade eu nem sei se a gente pode chamar de Praça sim viu Plínio Almeida foi até lá para conferir de um lado a Rua Abílio Paiva desse outro aqui a Auta de Luna Freire no bairro Ernani Sátiro E no meio tem algo que um dia já pode ser chamado de Praça mas do jeito que tá hoje com tudo quebrado esquecido abandonado mato lixo e sem condições nenhuma de uso Se tem uma coisa que isso aqui não é mais é uma praça os moradores dizem que faz mais ou menos uns 10 anos da última vez que alguém chegou aqui para fazer algum tipo de conserto manutenção nessa praça né Ficar Com certeza isso aqui assim eu eu eu tenho 41 anos aqui como ele tem como você já tá vendo aqui que as pessoas lhe darem a gente precisa de uma praça a gente precisa de um lazer a gente tem criança a gente precisa disso as crianças já se furaram aqui as crianças já pegaram o germe de cachorro aqui ali ó ferro enfiado para cavalo para animal aqui só serve para isso que não tem condições de andar eu mesmo vou fazer uma caminhada de Zezinho saiu daqui na rua aí rodeio e venho Quando estivesse pronto eu sou uma pracinha aqui tá certo é pequeno mas a gente aumentar o número de volta né Não só sou eu sou muito idosa que tem aqui temos a prefeitura ela tem aí uma creche em frente à praça das crianças aí vem para aí que eu já vi que ia subir aí e desceu aí pode se acidentar aí tudo rasgado tudo quebrado brincando do jeito que tá aí no jeito que tá aí criança vem amanhã à tarde para pegar porque tá vendo a hora que acidentado que a gente não pagamos também no nosso IPTU né não pagamos temos direito como colocar o outro cidadão exatamente nesse local aqui que tá cheio de mato tem Metralha também tem vários buracos era uma quadra não é isso Léo como era que antes antes de uma quadra de areia Aqui é onde a comunidade se divertir né Tem várias crianças aqui no bairro e a gente joga futebol a gente praticava vôlei não é isso para comunidade isso é muito importante queria que ele viesse reformar fazer uma quadra não colocaria novamente mas fazer uma quadra fazer um espaço que o pessoal fazer caminhada colocar ali os aparelhos para prática também de musculação isso que nós precisamos a gente que é o mesmo direito que as outros bairros tem que as outras praças tem dona Eronildes é uma das pessoas que mora aqui pertinho da praça e que tem muita vontade de fazer caminhada né mas nessas condições olha ali buraco não dá não tem não tem condições porque")
print(a)

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