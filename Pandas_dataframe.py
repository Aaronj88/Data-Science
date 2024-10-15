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

#essentially summary of dataframe
print(titanic.info())

#statistical summary
print(titanic.describe())

#get values of multiple columns (not one but not all)
print(titanic[["Name","Age"]])

#filtering rows
print(titanic[titanic["Age"]>18])

print(titanic[(titanic["Pclass"] == 1)&(titanic["Age"]>18)])

print(titanic[(titanic["Sex"] == "female")|(titanic["Pclass"] == 1)])


#slicing datasets

#index based:
print(titanic.iloc[215:432,2:5]) #iloc = index location

#conditional slicing:
print(titanic.loc[titanic["Age"]>18,["Name","Sex"]])

#changing values
titanic.loc[0:2,"Name"] = ["Thomas Wood","Alex Baker","Jack Something"]
print(titanic.head(3))

#add column
titanic["Discounted Fare"] = titanic["Fare"]/2
print(titanic.head(10))

#getting column names
print(titanic.columns)

#renaming columns
titanic.rename(columns={"Siblings/Spouses Aboard":"Family Aboard","Fare":"Ticket Cost"},inplace = True)
print(titanic.columns)



#saving (changes to) a csv file:
#titanic.to_csv("fake_titanic.csv")


