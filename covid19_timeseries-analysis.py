import pandas as pd
import plotly.graph_objects as go

covid = pd.read_csv("WHO_covid_data.csv")
covid["DateReported"] = pd.to_datetime(covid["DateReported"])

bydate = covid.groupby(["DateReported"]).sum()

fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=bydate.index,y=bydate["Cumulative_cases"],fill="tonexty",fillcolor="blue",line_color="red"))
fig1.update_layout(title="Cumulative Cases by Date")
fig1.write_html("Cumulative_Cases_by_Date.html",auto_open=True)


fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=bydate.index,y=bydate["New_cases"]))
fig2.write_html("New_Cases_by_Date.html",auto_open=True)


fig3 = go.Figure(data=[
    go.Scatter(x=bydate.index,y=bydate["New_cases"]),
    go.Scatter(x=bydate.index,y=bydate["New_deaths"])
])
fig3.write_html("New_Cases_vs_Deaths_by_Day.html",auto_open=True)


fig4 = go.Figure(data=[
    go.Bar(x=bydate.index,y=bydate["Cumulative_cases"]),
    go.Bar(x=bydate.index,y=bydate["Cumulative_deaths"])
])
fig4.write_html("Cumulative_Cases_vs_Cumulative_Deaths_by_Day.html",auto_open=True)

