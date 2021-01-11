
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import json
import geojson
from data.technology_patents.maps import *
from data.technology_patents.graphs import *
#==> import external method from .py file from folder /data,  wwhich is plotting the graph




def p3_updateLayout():
    #Defining Spaces ==> Insert your plot into the spaces
    leftSpace = html.Div([
            dbc.Col([
                html.H4('Options', style = {'color' : 'white'}),
                dcc.Dropdown(id = 'dropdown_po', 
                options =[{'label' : 'EPO', 'value' : '0' },
                          {'label' : 'USPTO', 'value' : '1'},
                          {'label' : 'PCT', 'value' : '2'}], 
                          value = '0',
                          placeholder = 'Select patent office',  style = {'margin-bottom' : 10, 'margin-top' : 50, 'width': '100%'}),
                dcc.Dropdown(id ='dropdown_number',
                options =[{'label' : 'Environmental-related', 'value' : '0'},
                        {'label' : 'Total', 'value' : '1' },],
                          value = '0',
                          placeholder = 'Select technology domain', style = {'width': '100%'})], 
                    )], style = {'margin-top' : 200, 'margin-left' : 20, 'background-color' : 'lightgreen', 'padding' : 10, 'border-radius' : 5} )
        #Example : leftSpace = html.Div(Call_method_of_plotted_graph)
    #midSpace = html.Div(dcc.Graph(figure = get_world_map_epo_total())) 
    midSpace = html.Div(dcc.Graph(id = 'worldmap_patents')) 
    #rightSpace = html.Div("Rechter Space")

    bot_leftSpace = html.Div(dcc.Graph(id = 'scatter_patents_env'))
    #bot_midSpace = html.Div("Mid Space")
    bot_rightSpace = html.Div(dcc.Graph(id = 'histogram_total_env'))

    #In "content" the grid gets initialised and styled via HTML and CSS ==> If your graph doesent get displayed the right way you can adjust the styling or text Konstantin
    content = html.Div([
        dbc.Row( [
            dbc.Col(
            [leftSpace, html.Div([        
            ])],
             className='col-2', style ={'padding':20}),

            dbc.Col(
            [midSpace, html.Div(
            )], className='col-10',style ={'padding':20}),]),

        dbc.Row( [
            dbc.Col(
            bot_leftSpace, className='col-6', style ={'padding':20}),
            dbc.Col(
            [bot_rightSpace, html.Div(
            )], className='col-6',style ={'padding':20}),]
            )],
            style={ 'width' : 'auto',  'overflow' : 'hidden',},) # other nice color #7ED6F0

    return content



