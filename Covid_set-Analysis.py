import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px #simpler, dynamic/interactive version of matplotlib. built on top of graph objects
import plotly.graph_objects as go #more customizable, less simple

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




us = covid[covid["Country_Region"]=="US"]
a = us.sort_values("Confirmed",ascending=False)
top_us = a.head(10)

fig3 = go.Figure(data=[
    go.Bar(name="Confirmed Cases",y=top_us["Province_State"],x=top_us["Confirmed"],orientation="h"),
    go.Bar(name="Recoveries",y=top_us["Province_State"],x=top_us["Recovered"],orientation="h"),
    go.Bar(name="Deaths",y=top_us["Province_State"],x=top_us["Deaths"],orientation="h")
    ])

fig3.update_layout(title="How the USA were affected by Covid-19",height=850)
fig3.write_html("figure3.html",auto_open=True)


