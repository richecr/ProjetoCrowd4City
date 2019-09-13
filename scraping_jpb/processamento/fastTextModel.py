import fasttext

model = fasttext.train_supervised(input="./textos.txt")