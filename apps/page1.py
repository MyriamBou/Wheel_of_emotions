import plotly.graph_objects as go
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
import dash_bootstrap_components as dbc
from app import app
import plotly.express as px
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
# needed only if running this as a single page app
#external_stylesheets = [dbc.themes.LUX]

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('Emotion_final.csv')
df2 = pd.read_csv('text_emotion.csv')

# rename columns
#df.rename(columns={'Text': 'Text','Emotion': 'Emotion'},inplace=True)

# change to app.layout if running as single page app instead

tab1_content= dash_table.DataTable(
        id='datatable', data =df.to_dict('records'), columns=[{'id':c, 'name':c} for c in df.columns],
        style_table={'overflowX': 'auto',
        'width':'1000px',
        'height':'400px',
        },
       export_format='csv',
       #export_format_style={'BackgroundColor':'white'},
       #style_button={'backgroundColor': '#25597f', 'color': 'white'},
       
       style_header={'backgroundColor': '#25597f', 'color': 'white'},
        css=[ {'selector': '.row', 'rule': 'margin: 0'} ],
        style_cell={
            'backgroundColor': 'white',
            'color': 'black',
            'fontSize': 13,
            'font-family': 'Nunito Sans',
            'textAlign':'left'}),

tab2_content= dash_table.DataTable(
        id='datatable', data =df2.to_dict('records'), columns=[{'id':c, 'name':c} for c in df2.columns],
        style_table={'overflowX': 'auto',
        'width':'1000px',
        'height':'400px',
                        'padding': 10},
        style_header={'backgroundColor': '#25597f', 'color': 'white'},
        export_format='csv',
        css=[ {'selector': '.row', 'rule': 'margin: 0'}],
        style_cell={
            'backgroundColor': 'white',
            'color': 'black',
            'fontSize': 13,
            'font-family': 'Nunito Sans',
            'textAlign':'left'}),
fig1 = px.histogram(df,x="Emotion", color="Emotion", marginal="rug", 
hover_name="Text", histfunc="sum")
fig2= px.sunburst(df2, path=["sentiment"],color="sentiment",hover_data=df2.columns)
fig4= listEmotion = df["Emotion"].unique()
listEmotionCat = df["Emotion"].unique()
def percentage (l,sentiment) :
    i = 0
    sum = 0
    for i in range (len(l)):
        if l[i] == sentiment:
            sum += 1
    return round((sum/len(l))*100)

listE = []
sumE = 0
for i in range (len(listEmotion)):
    sumE = percentage(df["Emotion"],listEmotionCat[i])

    listE.append(sumE)

fig4= px.pie(values=listE, names=listEmotion, title='Pourcentage des Emotions')


#Figure 5 -

fig5 = go.Figure(data=[go.Pie(labels=df.Emotion.unique(),
                             values=df.groupby('Emotion').Text.nunique(), 
                             textinfo='label+percent',
                            )],
                layout ={
                   'title':'Proportion Emotion for Kaggle set',
                   'font_color':'grey'
               })

# - Figure 6 -

fig6 = go.Figure(data=[go.Pie(labels=df2.sentiment.unique(),
                             values=df2.groupby('sentiment').content.nunique(), 
                             textinfo='label+percent',
                            )],
                             layout ={
                   'title':'Proportion Emotion for World set',
                   'font_color':'grey'
               })




layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("Datas Visualisation"), className="mb-2")
        ]),
        dbc.Row([
            dbc.Col(html.H6(children='Let s discover our two sets of data !'), className="mb-4")
        ]),

        dbc.Row([
            dbc.Col(dbc.Card(html.H3(children='Data analysis before classification',
                                     className="text-center text-light bg-dark"), body=True, color="dark")
                    , className="mb-4")
        ]),

        dbc.Row([
          dbc.Tabs([dbc.Tab(tab1_content, label="Data Kaggle"),
        dbc.Tab(tab2_content, label="Data World"),
        ]
)  
        ]),
         
  dbc.Row([
            dbc.Col(html.H1("Frequency of occurrence of Emotions"), className="mb-2")
        ]),
        dbc.Row([
                dbc.Col(dcc.Graph (id='Graphique5', figure=fig5)),
                dbc.Col(dcc.Graph (id='Graphique6', figure=fig6)),
            ], align='center'),      
        
        dbc.Row([
            dbc.Col(dcc.Graph (id='Graphique1', figure=fig1))
        ]),


         dbc.Row([
            dbc.Col(html.H1("Frequency of occurrence of words"), className="mb-2")
        ]),

        
          

         

        

       
        
         
         
        
      



]),

])
# page callbacks
# choose between condensed table and full table


# needed only if running this as a single page app
# if __name__ == '__main__':
#     app.run_server(host='127.0.0.1', debug=True)