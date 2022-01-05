import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
fig = go.Figure(go.Candlestick(
        x=df['Date'],
        open=df['AAPL.Open'],
        high=df['AAPL.High'],
        low=df['AAPL.Low'],
        close=df['AAPL.Close']
    ))


########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title='test dataframe'

########### Set up the layout
app.layout = html.Div(children=[
    html.H1("Apple"),
    dcc.Graph(
        id='value',
        figure=fig
    )
    ]
)

if __name__ == '__main__':
    app.run_server()
