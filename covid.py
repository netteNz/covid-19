import plotly.express as px
import os
import pandas as pd
import numpy as np

df = pd.read_csv("data/daily.csv",
                 usecols= ['date', 'positive', 'negative']
                 )

fig = px.histogram(df, x='date', y='positive')
fig.show()