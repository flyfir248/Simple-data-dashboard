import dash
from dash import dcc
from dash import html

import pandas as pd
import numpy as np

app = dash.Dash()

# create a dataframe
df = pd.DataFrame({'x': np.linspace(0, 10, 100),
                   'y': np.sin(np.linspace(0, 10, 100))})

#df = pd.read_csv('data.csv')

app.layout = html.Div(children=[
    html.H1(children='My Dashboard'),

    html.Div(children='''
        A simple dashboard.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df['x'], 'y': df['y'], 'type': 'line', 'name': 'Line'},
            ],
            'layout': {
                'title': 'Line Chart'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)


