import plotly.graph_objects as go
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import dash_table
import plotly.express as px
import plotly.graph_objs as go
from app import app

# needed if running single page dash app instead
#external_stylesheets = [dbc.themes.LUX]

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('Emotion_final.csv')
df2 = pd.read_csv('text_emotion.csv')
df3 = pd.read_csv('datak2.csv')
df4 = pd.read_csv('dataw2.csv')
# rename columns
#df.rename(columns={'Text': 'Text','Emotion': 'Emotion'},inplace=True)

# change to app.layout if running as single page app instead



        


tabs_styles = {
    'height': '44px',
   
}
tab_style = {
   'border': '1px solid #004252',
    'backgroundColor': '#004252',
    'padding': '6px',
    'fontWeight': 'bold'
    
}

tab_selected_style = {
   
    'border': '1px solid #00546C',
    'backgroundColor': '#00546C',
    'color': 'white',
    'padding': '6px'
}

tab1_content= dash_table.DataTable(
        id='datatable', data =df3.to_dict('records'), columns=[{'id':c, 'name':c} for c in df3.columns],
        style_table={'overflowX': 'auto',
        'width':'1000px',
        'height':'200px',
        },
        style_header={'backgroundColor': '#25597f', 'color': 'white'},
        css=[ {'selector': '.row', 'rule': 'margin: 0'}],
        style_cell={
            'backgroundColor': 'white',
            'color': 'black',
            'fontSize': 13,
            'font-family': 'Nunito Sans',
            'textAlign':'left'}),

tab2_content= dash_table.DataTable(
        id='datatable', data =df4.to_dict('records'), columns=[{'id':c, 'name':c} for c in df4.columns],
        style_table={'overflowX': 'auto',
        'width':'1000px',
        'height':'200px',
                        'padding': 10},
        style_header={'backgroundColor': '#25597f', 'color': 'white'},
        css=[ {'selector': '.row', 'rule': 'margin: 0'}],
        style_cell={
            'backgroundColor': 'white',
            'color': 'black',
            'fontSize': 13,
            'font-family': 'Nunito Sans',
            'textAlign':'left'}),

fig3 = layout=go.Layout(title='Kaggle dataset classifications comparison')
fig3 = go.Figure(layout=layout)
fig3.add_trace(go.Scatter(x=df3.model, y=df3.F1_score, name="F1_score",
                    line_shape='linear'))
fig3.add_trace(go.Scatter(x=df3.model, y=df3.accuracy, name="Accuracy",
                    line_shape='linear'))
fig3.add_trace(go.Scatter(x=df3.model, y=df3.precision, name="Precision",
                    line_shape='linear'))
fig3.add_trace(go.Scatter(x=df3.model, y=df3.recall, name="Recall",
                    line_shape='linear'))


fig4 = layout=go.Layout(title='World dataset classifications comparison')
fig4 = go.Figure(layout=layout)
fig4.add_trace(go.Scatter(x=df4.model, y=df4.F1_score, name="F1_score",
                    line_shape='linear'))
fig4.add_trace(go.Scatter(x=df4.model, y=df4.accuracy, name="Accuracy",
                    line_shape='linear'))
fig4.add_trace(go.Scatter(x=df4.model, y=df4.precision, name="Precision",
                    line_shape='linear'))
fig4.add_trace(go.Scatter(x=df4.model, y=df4.recall, name="Recall",
                    line_shape='linear'))


layout = html.Div([



    dbc.Container([

 dbc.Row([
            dbc.Col(html.H1("Classification modals"), className="mb-2")
        ]),     
       
dbc.Row([
          dbc.Tabs([dbc.Tab(tab1_content, label="Kaggle classifications Report"),
        dbc.Tab(tab2_content, label="World classifications Report"),
        ]
)  
        ]),



        dbc.Row([
            dbc.Col(dcc.Graph (id='Graphique3', figure=fig3))
        ]),

        dbc.Row([
            dbc.Col(dcc.Graph (id='Graphique4', figure=fig4))
        ]),
        dbc.Row([
            dbc.Col(html.H5("Analyse des données: Nous pouvons facilement voir que pour le premier jeu de donnée, le modèle de classification Knn n'est pas du tout pertinent, parce que il est basé sur les points les pluls similaires. Son seul avantage est l'horraire d'exécution du calcul. Le modèle SGDC est le plus pertinent pour notre cas. Dans le deuxième jeu de donnée, les labels sont nobreux. On obtient les meilleurs résultats avec les logreg et SVC modèles."), className="mb-2")
        ]),  

    ])
        ])


