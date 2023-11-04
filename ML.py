import numpy as np
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

heart_data = pd.read_csv('V:\irs flower detection\Heart_Disease_Prediction.csv')

X = heart_data.drop(columns='Heart Disease', axis=1)
Y = heart_data['Heart Disease']

X_train , X_test, Y_train , Y_test = train_test_split(X, Y, test_size=0.2 , stratify=Y,)
model = LogisticRegression()
model.fit(X_train , Y_train)

X_train_prediction = model.predict(X_train)
X_test_prediction = model.predict(X_test)

pickle.dump(model, open('ml.pkl', 'wb'))
