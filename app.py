import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle
app = Flask(__name__, template_folder='templates',static_folder = 'static')
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    return render_template('index.html', prediction_text='Attack is {}'.format(prediction))


if __name__ == '__main__':
    app.run(host='0.0.0.0')

