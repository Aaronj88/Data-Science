import pandas as pd

a = {"name":["John","Mark","Tom"],"age":[25,27,32],"nationality":["Indian","American","Chinese"]}
b = pd.DataFrame(a)
print(b)
print(type(b))

#reading csv(comma seperated values) file
titanic = pd.read_csv('Titanic.csv')

#head function shows you (by default) the first 5
print(titanic.head())

#tail function shows you (by default) the last 5
print(titanic.tail())

#tells us number of rows/columns
print(titanic.shape)

#extract single column
print(titanic["Name"])

print(titanic["Age"])

#average of single column
print(titanic["Age"].mean())


