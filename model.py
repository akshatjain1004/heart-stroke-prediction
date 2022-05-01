"""PRML_Course_Project.ipynb
"""

import pandas as pd
import numpy as np
import pickle
warnings.filterwarnings('ignore')

df = pd.read_csv('heart.csv')


X = df.drop('HeartDisease',axis=1)
y = df['HeartDisease']


categorical_cols = [col for col in X.columns if X[col].nunique() < 10 and X[col].dtype == "object"]

numerical_cols = [col for col in X.columns if X[col].dtype in ['int64', 'float64']]

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols),
        ('num', StandardScaler(), numerical_cols)
    ])


from sklearn.neural_network import MLPClassifier
from xgboost import  XGBClassifier

clf = XGBClassifier(use_label_encoder=False)


my_pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                              ('classifier', clf)
                             ])

my_pipeline.fit(X, y)

pickle.dump(my_pipeline, open('saved_model.pkl','wb'))