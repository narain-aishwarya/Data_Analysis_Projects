import pandas as pd
import numpy as np 
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("/kaggle/input/virat-kohli-performance-analysis/Virat_Kohli.csv")
print(data.head())

print(data.isnull()) #checking for null values.
#Starting with the analysis.
data["Runs"].sum() #total runs (2008-2017)
#Average runs
data["Runs"].mean()

matches = data.index
figure = px.line(data, x=matches, y="Runs", title='Runs scored by Virat Kohli Between 2008 - 2017')
figure.show()

data["Pos"] = data["Pos"].map({1.0: "Batting At 1", 2.0: "Batting At 2",
                              3.0: "Batting At 3", 4.0: "Batting At 4",
                              5.0: "Batting At 5", 6.0: "Batting At 6", 7.0:"Batting At 7"})
Pos = data["Pos"].value_counts()
label = Pos.index
counts = Pos.values
colors = ['gold', 'lightgreen', 'pink', 'blue', 'skyblue', 'orange', 'red']

fig = go.Figure(data=[go.Pie(labels=label, values = counts)])
fig.update_layout(title_text='Number of Matches At Different Batting Positions')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                 marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


#Total runs scored in different batting position.
label = data['Pos']
counts = data['Runs']
colors = ['gold', 'lightgreen', 'pink', 'blue', 'skyblue', 'orange', 'red']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Runs by Virat Kohli at Different Batting Position')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                 marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()

##Analysis of centuries scored by Virat Kohli while batting in the 1st innings and 2nd innings
centuries = data.query('Runs >= 100')
figure = px.bar(centuries, x=centuries["Inns"], y=centuries["Runs"],
             color=centuries["Runs"], title="Centuries By Virat Kohli in First Innings Vs. Second Innings")
figure.show()

###Analysis of Dismissals of Virat Kohli.
dismissal = data["Dismissal"].value_counts()
label = dismissal.index
counts = dismissal.values
colors = ['gold', 'lightgreen', 'pink', 'blue', 'skyblue', 'orange', 'red']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text="Dismissals of Virat Kohli")
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30, marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()

#Analysis of the team Virat has scored most against.
figure = px.bar(data, x=data['Opposition'], y=data["Runs"], color=data['Runs'] ,title="Runns scored most against Teams")
figure.show()
#Now, centuries scored by Virat Kohli against different teams.
figure = px.bar(centuries, x=centuries["Opposition"], y=centuries['Runs'], color=centuries["Runs"], title="Most Centuries scores against:")
figure.show()

#Analysis of Virat Kohli's Strike Rate.
strike_rate = data.query("SR >= 120")
print(strike_rate)
figure = px.bar(strike_rate, x=strike_rate["Inns"], y=strike_rate["SR"],
               color=strike_rate['SR'], title="Virat Kohli Strike Rate in 1st Vs 2nd innings")
figure.show()

#Analysis of Runns and 4s
figure = px.scatter(data_frame = data, x="Runs", y="4s", size="SR", trendline='ols', title="Relationship between the Runs and 4s scored")
figure.show()
#Now with 6s
figure = px.scatter(data_frame = data, x="Runs", y="6s", size="SR", trendline="ols", title="Relationship between the Runs and 6s scored")
figure.show()
