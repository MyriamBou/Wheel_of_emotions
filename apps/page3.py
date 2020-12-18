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

from sklearn.pipeline import Pipeline
#for machine Learning - classification
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report, confusion_matrix, f1_score, make_scorer
from sklearn.metrics import recall_score
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

# for visualization
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import string


df = pd.read_csv('Emotion_final.csv')

targets = list(df["Emotion"])
corpus = list(df["Text"])

X = corpus
y = targets
X_train, X_test, y_train, y_test = train_test_split(X, y,random_state=0)

pipe1 = Pipeline([('vect', CountVectorizer()), ('sgd', SGDClassifier()),])
pipe1.fit(X_train, y_train)



layout = html.Div([
    dbc.Container([
        dbc.Row([dbc.Col(html.H1("Prediction Game "), className="mb-2")]),
        dbc.Row([dbc.Col(html.H6(children='Please enter a sentence for the prediciton : prediction made on the first data set '), className="mb-4")]),
        dbc.Row([dbc.Col(dcc.Input(id='Prediction', type="text", debounce=True))]),
        dbc.Row([html.H6(id="output")])
        
    ]),

    
])

@app.callback (
    Output("output","children"),
    Input("Prediction","value")
)
def pred(Prediction):
    a=[Prediction]
    if Prediction is None :
        return ""
    else :
        y_pred= pipe1.predict(a)
        return u"Emotion :{} ".format(y_pred)

