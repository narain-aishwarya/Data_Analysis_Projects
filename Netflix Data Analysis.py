#This data analysis on based on Netfix data of 2019. <Currently working on creating data-set for year 2023 >
import numpy as np
import pandas as pd
import plotly.express as px #for data visualization
from textblob import TextBlob # for sentiment analysis.

data = pd.read_csv("/kaggle/input/netflix-shows/netflix_titles.csv")
data.shape
data.columns
#Now , looking at the Distribution of Content before starting the analysis.
d = data.groupby(['rating']).size().reset_index(name='counts')
pieChart = px.pie(d,values='counts',names='rating',
                 title="Distribution of Content Rating on Netflix",
                 color_discrete_sequence = px.colors.qualitative.Set1)
pieChart.show()

#Now analysis the top director.
data['director']=data['director'].fillna('No director specified')
filtered_directors = pd.DataFrame()
filtered_directors = data['director'].str.split(',',expand=True).stack()
filtered_directors = filtered_directors.to_frame()
filtered_directors.cloumns = ['Director']
directors = filtered_directors.groupby(['Director']).size().reset_index(name='Total Content')
directors = directors[directors.Director != 'No Director Specified']
directors = directors.sort_values(by=['Total Content'],asending = False)
directorsTop5 = directors.head()
directorsTop5 = directorsTop5.sort_values(by=['Total Content'])
fig1 = px.bar(directorsTop5, x='Total Content', y='Director', title='Top 5 directors on Netflix')
fig1.show()
