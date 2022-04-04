import pandas as pd
import plotly.figure_factory as ff
df = pd.read_csv('amazon.csv')
rate = df['Avg Rating'].tolist()
graph = ff.create_distplot([rate],['rate'],show_hist=False)
graph.show()