import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

c = pd.read_csv("covid_data.csv")
covid = c[["Province_State","Country_Region","Last_Update","Confirmed","Recovered","Deaths","Active"]]


covid["Province_State"].fillna(" ",inplace=True)
covid.dropna(inplace=True)


#top 10 most affected countries
topten = covid.groupby("Country_Region")
a = topten.sum().sort_values("Confirmed",ascending=False)
topten = a.head(10)


fig1 = px.scatter(topten,x=topten.index,y="Confirmed",size="Confirmed",size_max=50,color=topten.index,title="Which Countries Were Most Affected by Covid 19")
fig1.write_html("figure.html",auto_open=False)

fig2 = px.bar(topten,x=topten.index,y="Confirmed",height=650,color=topten.index,title="Which Countries Were Most Affected by Covid 19")
fig2.write_html("figure2.html",auto_open=True)

