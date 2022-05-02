import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('saved_model.pkl', 'rb'))

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
            data[index] = float(value)
    df = pd.DataFrame(data=[data.values],columns=data.index)

    return df

@app.route('/predict',methods=['POST'])
def predict():
  
    df = process(request.form)
    prediction = model.predict_proba(df)[0]
    return render_template('predict.html', prediction = round(prediction[1]*100,2))


if __name__ == "__main__":
    app.run(debug=True,port=8000)