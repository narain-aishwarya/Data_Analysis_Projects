import pandas as pd
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
pio.templates.default = "plotly_white"
data = pd.read_csv("/kaggle/input/new-delhi-air-quality/NewDelhi_Air_quality.csv")
print(data.head())

print(data.describe())