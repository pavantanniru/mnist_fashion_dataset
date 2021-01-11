# -*- coding: utf-8 -*-
"""flask_fun.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZYmTmcWu24zb2mQiJ03vRUctXcb0f-t8
"""

import flask
import numpy as np
from tensorflow.keras.models import load_model
import joblib

from flask import Flask,request,jsonify


flower_model = load_model('my_model.h5')
flower_scaler = joblib.load('iris_scaler.pkl')

def return_predictions(model,scaler,sample_json):

  s_len = sample_json['sepal_length']
  s_wid = sample_json['sepal_width']
  p_len = sample_json['petal_length']
  p_wid = sample_json['petal_width']

  flower = [[s_len,s_wid,p_len,p_wid]]

  scaler = scaler.transform(flower)

  classes = np.array(['setosa', 'versicolor', 'virginica'])

  class_ind = model.predict_classes(scaler)

  return classes[class_ind[0]]



app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello Pavan tanniru.'

flower_model = load_model('my_model.h5')
flower_scaler = joblib.load('iris_scaler.pkl')

@app.route('/api/flowers',methods=['POST'])

def return_predictions():
  content = request.json
  result = return_predictions(flower_model,flower_scaler,content)
  return jsonify(result)



if __name__ == '__main__':
   app.run()