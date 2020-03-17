#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df_final = pd.read_csv('textos_videos.csv')


# In[3]:


import nltk
from nltk.corpus import stopwords
stopwords = set(stopwords.words('english'))
nltk.download('wordnet')
nltk.download('stopwords')
from nltk.tokenize import TweetTokenizer
from nltk.corpus import wordnet as wn
tknzr = TweetTokenizer()
def get_tokens(sentence):
#     tokens = nltk.word_tokenize(sentence)  # now using tweet tokenizer
    tokens = tknzr.tokenize(sentence)
    tokens = [token for token in tokens if (token not in stopwords and len(token) > 1)]
    tokens = [get_lemma(token) for token in tokens]
    return (tokens)
def get_lemma(word):
    lemma = wn.morphy(word)
    if lemma is None:
        return word
    else:
        return lemma
token_list = (df_final['texto'].apply(get_tokens))


# In[4]:


from keras.preprocessing.text import Tokenizer
from keras.layers import Embedding


# In[5]:


t = Tokenizer()
t.fit_on_texts(token_list)
vocab_size = len(t.word_index) + 1


# In[6]:


# The maximum number of words to be used. (most frequent)
MAX_NB_WORDS = 1000
# Max number of words in each complaint.
MAX_SEQUENCE_LENGTH = 50
# This is fixed.
EMBEDDING_DIM = 768

# tokenizer = Tokenizer(num_words=MAX_NB_WORDS, filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~', lower=True)
# tokenizer.fit_on_texts(X.values)
# word_index = tokenizer.word_index
print('Found %s unique tokens.' % len(t.word_index))


# In[7]:


from bert_serving.client import BertClient
bc = BertClient(ip='150.165.75.172')


# In[ ]:


embedding_matrix = np.random.random((len(t.word_index) + 1, EMBEDDING_DIM))
for word, i in t.word_index.items():
    embedding_vector = bc.encode([word])
    if embedding_vector is not None:
        # words not found in embedding index will be all-zeros.
        embedding_matrix[i] = embedding_vector


# In[ ]:


embedding_layer = Embedding(len(t.word_index) + 1,
                            EMBEDDING_DIM,weights=[embedding_matrix],
                            input_length=MAX_SEQUENCE_LENGTH,trainable=True)


# In[ ]:


from sklearn.model_selection import train_test_split
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences


# In[ ]:


X_1 = tokenizer.texts_to_sequences(df_final['texto'])
X_1 = pad_sequences(X_1, maxlen=MAX_SEQUENCE_LENGTH)
print('Shape of data tensor:', X_1.shape)


# In[ ]:


Y_1 = pd.get_dummies(df_final['classes_problema']).values
print('Shape of label tensor:', Y_1.shape)


# In[ ]:


X_train, X_test, Y_train, Y_test = train_test_split(X_1,Y_1, test_size = 0.20, random_state = 42)
print(X_train.shape,Y_train.shape)
print(X_test.shape,Y_test.shape)


# In[ ]:


from keras.layers import Dense, Dropout, Embedding, LSTM, Bidirectional, TimeDistributed, Flatten, Input
from keras.models import Model


# In[ ]:


input = Input(shape=(MAX_SEQUENCE_LENGTH,))
model = Embedding(vocab_size,768,weights=[embedding_matrix],input_length=MAX_SEQUENCE_LENGTH)(input)
model =  Bidirectional (LSTM (100,return_sequences=True,dropout=0.50),merge_mode='concat')(model)
model = TimeDistributed(Dense(100,activation='relu'))(model)
model = Flatten()(model)
model = Dense(100,activation='relu')(model)
output = Dense(27,activation='softmax')(model)
model = Model(input,output)
model.compile(loss='categorical_crossentropy',optimizer='adam', metrics=['accuracy'])


# In[ ]:


model.fit(X_train,Y_train,validation_split=0.15, epochs = 20, verbose = 2)


# In[ ]:


# evaluate the model
loss, accuracy = model.evaluate(X_test, Y_test, verbose=2)
print('Accuracy: %f' % (accuracy*100))


# In[66]:


from sklearn.metrics import classification_report,confusion_matrix
Y_pred = model.predict(X_test)
y_pred = np.array([np.argmax(pred) for pred in Y_pred])
print('  Classification Report:\n',classification_report(Y_test,y_pred),'\n')

