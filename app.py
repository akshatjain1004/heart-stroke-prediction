import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
# model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    print(request.form.values())

    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))



if __name__ == "__main__":
    app.run(debug=True)