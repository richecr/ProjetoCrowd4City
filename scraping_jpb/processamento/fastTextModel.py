# import fasttext

# model = fasttext.train_supervised(input="./textos.txt")

from sacremoses import MosesTruecaser, MosesTokenizer

mtr = MosesTruecaser()
mtr.train('./textos.txt')
mtr.save_model('big.truecasemodel')

a = mtr.truecase("a seleção brasileira não fez mas o pessoal de tambiá", return_str=True)
print(a)