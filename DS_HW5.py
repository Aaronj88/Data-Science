import pandas as pd

iris = pd.read_csv('Iris.csv')


a = (iris.agg({"petal_length":["min","max"],"petal_width":["min","max"]}))
print(a)


print(' ')


grouped = iris.groupby('species')
b = (grouped.agg({"sepal_length":["mean"],"sepal_width":["mean"]}))
print(b)


print(' ')


iris["species"] = iris["species"].str.upper()
print(iris["species"].value_counts())


print(' ')


c = (grouped.agg({"sepal_length":["median"],"sepal_width":["median"],"petal_length":["median"],"petal_width":["median"]}))
print(c)
