import pandas as pd
import matplotlib.pyplot as plt


ad_in = pd.read_csv("adult_income_dataset.csv",sep=", ")
ad_in = ad_in[["age","workclass","education","marital-status","occupation","relationship","race","gender","capital-gain","capital-loss","hours-per-week","native-country","income"]]

print(ad_in.info())
print(ad_in.describe())
print(ad_in.head())





