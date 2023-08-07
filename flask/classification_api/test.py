import MeCab
import tensorflow as tf
import numpy as np
from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
import MeCab
import re
import pickle


def preprocess_data(new_sentence):
    with open('tokenizer.pkl', 'rb') as f:
        tokenizer = pickle.load(f) # 학습하기 위해 사용했던 토크나이저 load

        max_len = 33
        stopwords = ['도', '는', '다', '의', '가', '이', '은', '한', '에', '하', '고', '을', '를', '인', '듯', '과', '와', '네', '들', '듯', '지', '임', '게']
        mecab = MeCab.Tagger()
        
        new_sentence = re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣 ]','', new_sentence)
        
        # new_sentence = mecab.morphs(new_sentence)
        new_sentence = mecab.parse(new_sentence)
        
        new_sentence = new_sentence.replace('\t', ' ')
        new_sentence = new_sentence.replace('\n', ' ')
        
        new_sentence = new_sentence.split(' ')[::2]
        new_sentence = new_sentence[:-1]
        new_sentence = [word for word in new_sentence if word not in stopwords]
        encoded = tokenizer.texts_to_sequences([new_sentence]) 
        pad_new = pad_sequences(encoded, maxlen=max_len)

        return pad_new
    

model = tf.keras.models.load_model('C:/classification_api/CNN_model.h5')

pad_data = preprocess_data('사용자가 월세를 안줘')
prediction = model.predict(pad_data)
max_index = int(np.argmax(prediction)) + 1

if max_index == 1:
    predicted_label = '계약이행'
elif max_index == 2:
    predicted_label = '매매'
elif max_index == 3:
    predicted_label = '명예훼손'
elif max_index == 4:
    predicted_label = '부동산'
elif max_index == 5:
    predicted_label = '손해배상'
elif max_index == 6:
    predicted_label = '용역'
elif max_index == 7:
    predicted_label = '채무'
elif max_index == 8:
    predicted_label = '통지'
    
    
print(predicted_label)
