import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)
# model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

def process(form_data):
    data = pd.Series(form_data)
    continuous_column = ['Age','RestingBP','Cholesterol','FastingBS','MaxHR','Oldpeak']
    for index,value in data.iteritems():
        if index in continuous_column:
            if len(value)==0:
                value = 0
            data[index] = int(value)
    df = pd.DataFrame(data=[data.values],columns=data.index)

    return df

@app.route('/predict',methods=['POST'])
def predict():
  
    df = process(request.form)
    
    return render_template('predict.html', percent = 89.6)


if __name__ == "__main__":
    app.run(debug=True,port=8000)