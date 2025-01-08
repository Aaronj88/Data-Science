import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import LabelEncoder


ad_in = pd.read_csv("adult_income_dataset.csv",sep=", ")
ad_in = ad_in[["age","workclass","education","marital-status","occupation","relationship","race","gender","capital-gain","capital-loss","hours-per-week","native-country","income"]]

print(ad_in.info())
print(ad_in.describe())
print(ad_in.head())



LE = LabelEncoder()
ad_in["income"] = LE.fit_transform(ad_in["income"]) #false(0) = <50k
print(ad_in)

occ_inc = ad_in.groupby("occupation")["capital-gain"].mean().sort_values()
print(occ_inc)

high_inc = ad_in[ad_in["income"] == 1]
low_inc = ad_in[ad_in["income"] == 0]
race_counts = high_inc["race"].value_counts()
gender_counts = high_inc["gender"].value_counts()
age_low = low_inc["age"].value_counts().sort_index(ascending=True)
age_high = high_inc["age"].value_counts().sort_index(ascending=True)
hours_high = high_inc["hours-per-week"]
hours_low = low_inc["hours-per-week"]
hours_high_avg = high_inc["hours-per-week"].mean()
hours_low_avg = low_inc["hours-per-week"].mean()
print(age_high)
print(age_low)




plt.figure(figsize=(12, 8))
plt.bar(occ_inc.index,occ_inc.values)
plt.title("How Much Capital Each Occupation Gains (on average)")
plt.xlabel("Occupation")
plt.ylabel("Capital Gain")
plt.xticks(rotation = 30)
plt.show()


plt.figure(figsize=(10, 6))
plt.hist(x=ad_in["age"], bins=30, color="lightgreen", edgecolor="black")
plt.title("Age Distribution in the Adult Income Dataset")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()


plt.figure(figsize=(10, 6))
plt.scatter(x=ad_in['age'], y=ad_in["capital-gain"])
plt.title("Age vs Capital Gain")
plt.xlabel("Age")
plt.ylabel("Capital Gain")
plt.show()


plt.figure(figsize=(10,6))
plt.pie(race_counts.values, labels=race_counts.index,autopct='%.1f%%',startangle=0,shadow=True) #how do I adjust the text (angle) to make it not overlap?
plt.title("The Races of People Making more than 50 thousand")
plt.show()
#these two are pretty similar (↑↓)
plt.figure(figsize=(10,6))
plt.pie(gender_counts.values, labels=gender_counts.index,autopct='%.1f%%',startangle=0,shadow=True)
plt.title("The Genders of People Making more than 50 thousand")
plt.show()


plt.figure(figsize=(10, 6))
plt.hist(hours_low,bins=np.arange(1,hours_low.max(),10))
plt.title("How Many Hours per Week People Earning Less Than 50k Were Working")
plt.xlabel("Hours/Week")
plt.ylabel("Frequency")
plt.show()


plt.figure(figsize=(10, 6))
plt.hist(hours_high,bins=np.arange(1,hours_high.max(),10))
plt.title("How Many Hours People Earning More Than 50k Were Working")
plt.xlabel("Hours/Week")
plt.ylabel("Frequency")
plt.show()


plt.figure(figsize=(10,6))
plt.scatter(low_inc["age"],low_inc["income"],color="red")
plt.scatter(high_inc["age"],high_inc["income"],color="blue")
plt.title("Amount of People Earning Less Than vs More Than 50k by Age")
plt.xlabel("Age")
plt.ylabel("Amount Earning <50k")
plt.show()
