import plotly.graph_objects as go
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app

# needed if running single page dash app instead
#external_stylesheets = [dbc.themes.LUX]

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("Datas Vizualisation"), className="mb-2")
        ])
    ])
        ])