import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder

d = pd.read_csv("Dataset.csv")
print(d.head())


#split into features and target
X = d[["Country","Age","Salary"]]
y = d["Purchased"]

print(X,y)

#checking for missing values
print(X.isnull().sum())

#X.dropna(inplace=True) #removes the entire row wherever any value is missing

#treating the missing value
a = SimpleImputer(missing_values=np.nan,strategy="median")
X[["Age","Salary"]] = a.fit_transform(X[["Age","Salary"]])
print(X.isnull().sum())
print(X)


#encoding feature categorical values
X_encoded = pd.get_dummies(X,columns=["Country"],dtype=int)
print(X_encoded)

#encoding target categorical values
#y.replace({"Yes":1,"No":0},inplace=True)

b = LabelEncoder()
y_encoded = b.fit_transform(y)
print(y)


#splitting dataset into training set and test set
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X_encoded,y_encoded,train_size=0.8,random_state= 32) #ORDER MATTERS
print(X_train)
print(X_test)
print(y_train)
print(y_test)


#scaling data
#technique 1: standard scaling
from sklearn.preprocessing import StandardScaler
c = StandardScaler()
X_train[["Age","Salary"]] = c.fit_transform(X_train[["Age","Salary"]])
print(X_train)







