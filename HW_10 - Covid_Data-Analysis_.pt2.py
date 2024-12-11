import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

c = pd.read_csv("covid_data.csv")
covid = c[["Province_State","Country_Region","Last_Update","Confirmed","Recovered","Deaths","Active"]]

brz = covid[covid["Country_Region"]=="Brazil"]
a = brz.sort_values("Confirmed",ascending=False)
toptenb = a.head(10)

ind = covid[covid["Country_Region"]=="India"]
a = ind.sort_values("Confirmed",ascending=False)
in_conf = a.head(10)



fig1 = px.scatter(toptenb,x=toptenb["Province_State"],y="Confirmed",size="Confirmed",size_max=25,color=toptenb.index,title="Which Countries Were Most Affected")
fig1.write_html("Affected.html",auto_open=True)

fig2 = go.Figure(data=[
    go.Bar(name="Confirmed Cases",x=in_conf["Province_State"],y=in_conf["Confirmed"]),
    go.Bar(name="Recoveries",x=in_conf["Province_State"],y=in_conf["Recovered"]),
    go.Bar(name="Deaths",x=in_conf["Province_State"],y=in_conf["Deaths"])
    ])
fig2.write_html("India.html",auto_open=True)


