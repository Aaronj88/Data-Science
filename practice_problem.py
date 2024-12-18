import pandas as pd
import plotly.graph_objects as go

covid = pd.read_csv("WHO_covid_data.csv")



user_c = input("What country would you like to see the daily cases and deaths of?")

c = covid[covid["Country"]==user_c]
c["DateReported"] = pd.to_datetime(c["DateReported"])

fig1 = go.Figure(data = [
    go.Scatter(x=c["DateReported"],y=c["New_cases"],name="New Cases"),
    go.Scatter(x=c["DateReported"],y=c["New_deaths"],name="New Deaths")
])
fig1.write_html("country_deaths and cases.html",auto_open=True)



