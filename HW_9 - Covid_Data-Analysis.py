import pandas as pd
import plotly.express as px

c = pd.read_csv("covid_data.csv")
covid = c[["Province_State","Country_Region","Last_Update","Confirmed","Recovered","Deaths","Active"]]


country = covid.groupby("Country_Region")
a = country.sum().sort_values("Recovered",ascending=False)
toptenr = a.head(10)

a = country.sum().sort_values("Deaths",ascending=False)
toptend = a.head(10)

a = country.sum().sort_values("Confirmed")
lowestc = a.head(5)

us = covid[covid["Country_Region"]=="US"]
a = us.sort_values("Confirmed",ascending=False)
us_affected = a.head(10)



fig1 = px.scatter(toptenr,x=toptenr.index,y="Recovered",size="Recovered",size_max=25,color=toptenr.index,title="Which Countries Had The Highest Recovery Rates")
fig1.write_html("Recoveries.html",auto_open=True)

fig2 = px.scatter(toptend,x=toptend.index,y="Deaths",size="Deaths",size_max=25,color=toptend.index,title="Which Countries Had The Highest Amount of Deaths")
fig2.write_html("Deaths.html",auto_open=True)

fig3 = px.bar(lowestc,x=lowestc.index,y="Confirmed",height=650,color=lowestc.index,title="Which Countries Were Least Affected by Covid 19")
fig3.write_html("Least Affected.html",auto_open=True)

fig4 = px.bar(us_affected,x="Province_State",y="Confirmed",height=700,color="Province_State",title="Which American States Were Most Affected by Covid-19")
fig4.write_html("Affected by US States.html",auto_open=True)


