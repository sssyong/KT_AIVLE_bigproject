# ------------------------------------------------------------------------------------------------------------------------
"""
Flask(restx 사용 x)

"""
# from flask import Flask, render_template, request, jsonify
# import tensorflow as tf
# import numpy as np
# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences
# from konlpy.tag import Mecab
# import re
# import pickle

# app = Flask(__name__)
# model = tf.keras.models.load_model('C:\\Users\\User\\Desktop\\classification_api\\CNN_model.h5')  

# # TensorFlow 모델 로드 (경로 설정 필요)


# def preprocess_data(new_sentence):
#     with open('tokenizer.pkl', 'rb') as f:
#         tokenizer = pickle.load(f) # 학습하기 위해 사용했던 토크나이저 load

#     max_len = 33
#     stopwords = ['도', '는', '다', '의', '가', '이', '은', '한', '에', '하', '고', '을', '를', '인', '듯', '과', '와', '네', '들', '듯', '지', '임', '게']
#     mecab = Mecab('C://mecab//mecab-ko-dic') #3

#     new_sentence = re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣 ]','', new_sentence)
#     new_sentence = mecab.morphs(new_sentence)
#     new_sentence = [word for word in new_sentence if word not in stopwords]
#     encoded = tokenizer.texts_to_sequences([new_sentence]) 
#     pad_new = pad_sequences(encoded, maxlen=max_len)

#     return pad_new


# @app.route('/predict', methods=['POST'])
# def predict():
#     new_sentence = request.form['text']  # POST 요청의 JSON 데이터 가져오기
#     pad_data = preprocess_data(new_sentence)  # 데이터 전처리 함수 호출
#     prediction = model.predict(pad_data)  # 모델로 예측 수행
#     # max_index = np.argmax(prediction)+1  # 최댓값을 가지는 인덱스를 찾습니다.
#     max_index = int(np.argmax(prediction)) + 1 # JSON 형태로 반환하기 위해 int()
    
#     if max_index == 1:
#         predicted_label = '계약이행'
#     elif max_index == 2:
#         predicted_label = '매매'
#     elif max_index == 3:
#         predicted_label = '명예훼손'
#     elif max_index == 4:
#         predicted_label = '부동산'
#     elif max_index == 5:
#         predicted_label = '손해배상'
#     elif max_index == 6:
#         predicted_label = '용역'
#     elif max_index == 7:
#         predicted_label = '채무'
#     elif max_index == 8:
#         predicted_label = '통지'

#     # return render_template('predict.html', prediction=predicted_label)
#     response = {'max_index': max_index, 'predicted_label': predicted_label}
#     return jsonify(response)

# if __name__ == '__main__':
#     print("* Loading Keras model and starting Flask server..."
#           "please wait until the server has fully started")
#     app.run(debug=True)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/echo_call/<param>') #get echo api
# def get_echo_call(param):
#     return jsonify({"param": param})



# -------------------------------------------------------------------------------------------------
"""

1. pip install -r requirements.txt

2. mecab 폴더를 C:\\ 바로 밑에 두셔야합니다!!

3. 터미널에서 --> flask --debug run

"""

from flask import Flask, jsonify, request
from flask_restx import Api, Resource, fields, reqparse
import tensorflow as tf
import numpy as np
from flask_cors import CORS




from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
import MeCab
import re
import pickle

app = Flask(__name__)
CORS(app)
api = Api(
    app,
    title='classification_API Server')

model = tf.keras.models.load_model('C:/Users/PARKmaker/Desktop/ANY/4_aivle/big_project/ai_7_25_project/flask/classification_api/CNN_model.h5')

# TensorFlow 모델 로드 (경로 설정 필요)

def preprocess_data(new_sentence):
    with open('tokenizer.pkl', 'rb') as f:
        tokenizer = pickle.load(f) # 학습하기 위해 사용했던 토크나이저 load

    max_len = 33
    stopwords = ['도', '는', '다', '의', '가', '이', '은', '한', '에', '하', '고', '을', '를', '인', '듯', '과', '와', '네', '들', '듯', '지', '임', '게']
    mecab = MeCab.Tagger()
    
    new_sentence = re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣 ]','', new_sentence)
    new_sentence = mecab.parse(new_sentence)
    
    new_sentence = new_sentence.replace('\t', ' ')
    new_sentence = new_sentence.replace('\n', ' ')
    
    new_sentence = new_sentence.split(' ')[::2]
    new_sentence = new_sentence[:-1]
    new_sentence = [word for word in new_sentence if word not in stopwords]
    encoded = tokenizer.texts_to_sequences([new_sentence]) 
    pad_new = pad_sequences(encoded, maxlen=max_len)

    return pad_new


input_model = api.model('Input', {'text': fields.String(required=True, description='text_input')})
output_model = api.model('Output', {'max_index': fields.Integer, 'predicted_label': fields.String})

@api.route('/predict')
class PredictResource(Resource):
    @api.expect(input_model)
    @api.marshal_with(output_model)
    def post(self):
        text = request.json.get('text')
        new_sentence = text
        pad_data = preprocess_data(new_sentence)
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

        response = {'max_index': max_index, 'predicted_label': predicted_label}
        return response
    
if __name__ == '__main__':
    print("* Loading Keras model and starting Flask server...",
          "please wait until the server has fully started")
    app.run(host = '0.0.0.0')
