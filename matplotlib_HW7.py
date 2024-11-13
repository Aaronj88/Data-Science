import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

titanic = pd.read_csv("Titanic.csv")
iris = pd.read_csv("Iris.csv")


#BAR

pclass = titanic["Pclass"].value_counts()
plt.bar(pclass.index,pclass)
plt.xticks(ticks=pclass.index,labels = ["Pclass "+str(p) for p in pclass.index])
plt.show()


#HISTOGRAM
ages = titanic["Age"]
bins = np.arange(0,100,10)

plt.hist(ages,bins,rwidth=1)
plt.show()


#IRIS


#PIE
species = iris["species"].value_counts()
slices = [species["setosa"],species["versicolor"],species["virginica"]]
labels = ["setosa","versicolor","virginica"]
plt.pie(slices,labels = labels,shadow=True)
plt.show()


#SCATTER
plt.scatter(iris["petal_length"],iris["petal_width"],label = "Petal lengths in comparison to widths",marker = "o",cmap=iris["species"])
plt.show()




