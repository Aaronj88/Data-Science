import pandas as pd

d = pd.read_csv("Dataset.csv")
print(d.head())


#split into features and target
X = d[["Country","Age","Salary"]]
y = d["Purchased"]

print(X,y)

#checking for missing values
print(X.isnull().sum())
X.dropna(inplace=True)
print(X.isnull().sum())









