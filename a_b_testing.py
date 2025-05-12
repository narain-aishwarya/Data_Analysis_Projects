import pandas as pd
import datetime
from datetime import date, timedelta
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly_white"

control_data = pd.read_csv("/kaggle/input/example-dataset-for-ab-test/control_group.csv", sep = ";")
test_data = pd.read_csv("/kaggle/input/example-dataset-for-ab-test/test_group.csv", sep = ";")

print(control_data.head())
print(test_data.head())

control_data.columns = ["Campaign Name", "Date", "Amount Spent", "Number of Impressions",  "Reach", "Website Clicks", "Searches Received", "Content Viewed", "Added to Cart", "Parchases"]
test_data.columns = ["Campaign Name", "Date", "Amount Spent", "Number of Impressions",  "Reach", "Website Clicks", "Searches Received", "Content Viewed", "Added to Cart", "Parchases"]
print(control_data.isnull().sum())
