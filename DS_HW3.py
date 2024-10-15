import pandas as pd


iris = pd.read_csv('Iris.csv')

print(iris.head())
print(' ')

print(iris["petal_length"].mean())
print(iris["petal_length"].min())
print(iris["petal_length"].max())

print(' ')

print(iris["petal_width"].mean())
print(iris["petal_width"].min())
print(iris["petal_width"].max())

print(' ')

print(iris["sepal_length"].mean())
print(iris["sepal_length"].min())
print(iris["sepal_length"].max())

print(' ')

print(iris["sepal_width"].mean())
print(iris["sepal_width"].min())
print(iris["sepal_width"].max())
