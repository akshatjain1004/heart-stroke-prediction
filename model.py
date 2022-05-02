"""PRML_Course_Project.ipynb
"""
import sys
import warnings
import pandas as pd
import numpy as np
import pickle
import warnings
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from xgboost import XGBClassifier
warnings.filterwarnings('ignore')

df = pd.read_csv('heart.csv')
clf = XGBClassifier()

# selected features
selected_features= ['Age', 'Sex', 'ChestPainType', 'FastingBS', 'ExerciseAngina', 'Oldpeak', 'ST_Slope']

X = df[selected_features]
y = df['HeartDisease']

categorical_cols = [col for col in X.columns if X[col].nunique() < 10 and X[col].dtype == 'object']

numerical_cols = [col for col in X.columns if X[col].dtype in ['int64', 'float64']]

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols),
        ('num', StandardScaler(), numerical_cols)
    ])
my_pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                              ('classifier', clf)
                             ])


my_pipeline.fit(X, y)

pickle.dump(my_pipeline, open('saved_model.pkl','wb'))