# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from flask import Flask, request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)
pickle_in = open('classifier.pkl','rb')
classifier = pickle.load(pickle_in)

@app.route('/')
def welcome():
    return 'Welcome All'

@app.route('/predict')
def predict_note_authentication():
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    kurtosis = request.args.get('kurtosis')
    entropy = request.args.get('entropy')
    preditcion = classifier.predict([[variance, skewness, kurtosis, entropy]])
    return 'The predicted value is'+str(prediction)

@app.route('/predict_file',methods=['POST'])
def predict_note_file():
    df_test = pd.read_csv(request.files.get('file'))
    prediction = classifier.predict(df_test)
    return 'The predicted values for the csv is+' + str(list(prediction))

if __name__ == '__main__':
    app.run()
