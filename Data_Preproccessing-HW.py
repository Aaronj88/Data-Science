import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder

iris = pd.read_csv('Iris.csv')

X = iris[["sepal_length","sepal_width","petal_length","petal_width"]] #features
y = iris["species"] #target

#print(X.isnull().sum()) #no missing values

l = LabelEncoder()
y_encoded = l.fit_transform(y)
print(y_encoded)

#splitting into testing/training datasets
X_train,X_test,y_train,y_test = train_test_split(X,y_encoded,train_size=0.9,random_state= 88)

#scale
scaler = StandardScaler()
X_train[["sepal_length","sepal_width","petal_length","petal_width"]] = scaler.fit_transform(X_train[["sepal_length","sepal_width","petal_length","petal_width"]])


