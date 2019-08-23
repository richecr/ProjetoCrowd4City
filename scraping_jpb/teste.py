import pandas as pd
import pickle

data = pd.read_pickle('./textos_videos.csv')

from gensim import matutils, models
import scipy.sparse

tdm = data.transpose()
tdm.head()

sparse_counts = scipy.sparse.csr_matrix(tdm)
corpus = matutils.Sparse2Corpus(sparse_counts)