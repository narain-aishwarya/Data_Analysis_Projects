#This data analysis on based on Netfix data of 2019. <Currently working on 2024 >
import numpy as np
import pandas as pd
import plotly.express as px #for data visualization
from textblob import TextBlob # for sentiment analysis.

data = pd.read_csv("/kaggle/input/netflix-shows/netflix_titles.csv")
data.shape
