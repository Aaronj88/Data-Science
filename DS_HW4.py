import pandas as pd
titanic = pd.read_csv('Titanic.csv')


print[titanic[(titanic["Sex"] == "male")&(titanic["Pclass"] == 1)]]
print(titanic[(titanic["Sex"] == "male")&(titanic["Pclass"] == 2)])
print(titanic[(titanic["Sex"] == "male")&(titanic["Pclass"] == 3)])

print(titanic[(titanic["Sex"] == "female")&(titanic["Pclass"] == 1)])
print(titanic[(titanic["Sex"] == "female")&(titanic["Pclass"] == 2)])
print(titanic[(titanic["Sex"] == "female")&(titanic["Pclass"] == 3)])


print(titanic[titanic["Survived"] == 1])
