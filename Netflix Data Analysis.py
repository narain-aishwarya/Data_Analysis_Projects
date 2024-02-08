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

#Analysis of the top 5 actors on Netflix
data['cast'] = data['cast'].fillna('No Cast Specified')
filtered_cast =pd.DataFrame()
filtered_cast = data['cast'].str.split(',',expand=True).stack()
filtered_cast = filtered_cast.to_frame()
filtered_cast.columns = ['Actor']
actors = filtered_cast.groupby(['Actor']).size().reset_index(name='Total Content')
actors = actors[actors.Actor != 'No Cast Specified']
actors = actors.sort_values(by=['Total Content'],ascending=False)
actorsTop5 = actors.head()
actorsTop5 = actorsTop5.sort_values(by=['Total Content'])
fig2=px.bar(actorsTop5,x='Total Content',y='Actor',title='Top 5 Actors on Netflix')
fig2.show()

#Analyzing the trend of production over the years on Netflix.
data1 = data[['type','release_year']]
data1=data1.rename(columns={'release_year': 'Release Year'})
data2 = data1.groupby(['Release Year','type']).size().reset_index(name='Total Content')
data2=data2[data2['Release Year']>=2010]
fig3 = px.line(data2,x='Release Year', y = 'Total Content',color='type',title='Trend of content produced over the years on Netflix')
fig3.show()

#Final Analysis on this Netflix data will be of Sentiment of content.
#Sentiment Analysis is a type of process of classifying whether the data generated from the text is positive,negative or neutral.
sent_data = data[['release_year','description']]
sent_data = sent_data.rename(columns={'release_year':'Release Year'})
for index,row in sent_data.iterrows():
    z=row['description']
    testimonial=TextBlob(z)
    p = testimonial.sentiment.polarity
    if p==0:
        sent='Neutral'
    elif p>0:
        sent='Positive'
    else:
        sent='Negative'
    sent_data.loc[[index,4],'Sentiment']=sent
    
    sent_data = sent_data.groupby(['Release Year','Sentiment']).size().reset_index(name ='Total Content')
    
    sent_data = sent_data[sent_data['Release Year']>=2010]
    fig4 =px.bar(sent_data, x='Release Year',y='Total Content',color='Sentiment',title='Sentiment of content on Netflix')
    fig4.show()
  #above graph displays the overall sentiment analysis of this Netfilx data.
