
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import plotly.express as px
import plotly.graph_objs as go
import geopandas as gp 
import pandas as pd
import json
#==> import external method from .py file from folder /data,  wwhich is plotting the graph

# Testing
df = pd.read_csv('data/technology_patents/Patents_Ready.csv')
# Reading geojson file for chloropleth map
#world_map = json.load(open('/data/custom.geo.json', 'r'))

def p3_updateLayout():
    #Defining Spaces ==> Insert your plot into the spaces
    leftSpace = html.Div("Linker Space")
        #Example : leftSpace = html.Div(Call_method_of_plotted_graph)
    midSpace = html.Div("World Map")
    rightSpace = html.Div("Rechter Space")

    bot_leftSpace = html.Div("Left Space")
    bot_midSpace = html.Div("Mid Space")
    bot_rightSpace = html.Div("Rechter Space")

    #In "content" the grid gets initialised and styled via HTML and CSS ==> If your graph doesent get displayed the right way you can adjust the styling or text Konstantin
    content = html.Div(
        [dbc.Row( [
            dbc.Col(
            [leftSpace, html.Div([
                dcc.Dropdown(id = 'dropdown1-left', 
                options =[{'label' : 'EPO', 'value' : 'epo' },
                          {'label' : 'USPTO', 'value' : 'uspto'},
                          {'label' : 'PCT', 'value' : 'pct'}], 
                          value = "epo",
                          placeholder = 'Select patent office', style = {'margin-bottom' : 10}),
                html.Div(id='dropdown1-content'),
                
                dcc.Dropdown(id = 'dropdown2-left',
                options =[{'label' : 'Total', 'value' : 'total' },
                          {'label' : 'Environmental-related', 'value' : 'env'}],
                          value = 'total' ,
                          placeholder = 'Select technology domain'),
                html.Div(id='dropdown2-content')],
                style={'width': '100%', 'height': 500, 'background-color' : '#33FFFC'},
            )],className='col-2', style ={'padding':20}),
            dbc.Col(
            [midSpace, html.Div(
                style={'width': '100%', 'height': 500, 'background-color' : '#888888'},
            )], className='col-8',style ={'padding':20}),
            dbc.Col(
            [rightSpace, html.Div(
                style={'width': '100%', 'height': 500, 'background-color' : '#888888'},
            )], className='col-2', style ={'padding':20}),],
            ),
            dbc.Row( [
            dbc.Col(
            bot_leftSpace,className='col-4'),
            dbc.Col(
            [bot_midSpace, html.Div(
                style={'width': '100%', 'height': 500, 'background-color' : '#888888'},
            )], className='col-4', style ={'padding':20}),
            dbc.Col(
            [bot_rightSpace, html.Div(
                style={'width': '100%', 'height': 500, 'background-color' : '#888888'},
            )], className='col-4',style ={'padding':20}),],
            )],
            style={ 'width' : 'auto', 'padding' : 30, 'overflow' : 'hidden'},)

    return content

'''def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open'''

def display_chloropleth(): 
    fig = px.choropleth_mapbox(
        df, geojson=geo_world)
    
    fig.show()

    return fig
