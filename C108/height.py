import pandas as pd
import plotly.figure_factory as ff
df = pd.read_csv('data.csv')
height = df['Height(Inches)'].tolist()
weight = df['Weight(Pounds)'].tolist()
graph = ff.create_distplot([height], ['height'],show_hist=False)
graph.show()