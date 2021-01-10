
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

# Testing

#df1['iso_a3']  = df1['iso_a3'].astype(str)


#with open('data/Worldmap shapes/custom.geo.json') as f: 
 #   gj = json.load(f)

# print(gj["features"][5])


def p3_updateLayout():
    #Defining Spaces ==> Insert your plot into the spaces
    leftSpace = html.Div([
            dbc.Col([
                dbc.Row([
                html.H4('Options'),
                dcc.Dropdown(id = 'dropdown_po', 
                options =[{'label' : 'EPO', 'value' : '0' },
                          {'label' : 'USPTO', 'value' : '1'},
                          {'label' : 'PCT', 'value' : '2'}], 
                          value = '0',
                          placeholder = 'Select patent office', style = {'margin-bottom' : 10, 'margin-top' : 10, 'width': '95%'}),
                dcc.Dropdown(id ='dropdown_number',
                options =[{'label' : 'Environmental-related', 'value' : '0'},
                        {'label' : 'Total', 'value' : '1' },],
                          value = '0',
                          placeholder = 'Select technology domain', style ={ 'width': '95%'})]),
                dbc.Row([
                    html.H4('Information Box', style = { 'margin' : '10px'}),                    
                    dbc.Button("Informations", id="open"),
                    dbc.Modal(
                        [
                            dbc.ModalHeader("Major infos"),
                            dbc.ModalBody([html.Div("For each countries : 3 questions were asked to 2 thousands people."),
                                        html.Div("Question 1 : Do you consider we are living a climate change ?"),
                                        html.Div("            1 : Yes, of course"),
                                        html.Div("            2 : Yes, a little bit"),
                                        html.Div("            3 : Not really"),
                                        html.Div("            4 : Not at all"),
                                        html.Div("            5 : I don't know"),
                                        html.Div("Question 2 : Did you change your habits in order to improve climate situation ?"),
                                        html.Div("            1 : Yes, of course"),
                                        html.Div("            2 : Yes, a little bit"),
                                        html.Div("            3 : Not really"),
                                        html.Div("            4 : Not at all"),
                                        html.Div("            5 : I don't know"),
                                        html.Div("Question 3 : Who must fight in priority global warming"),
                                        html.Div("            1 : Scientists and technical progress"),
                                        html.Div("            2 : Ourselves, our behaviour and our habits"),
                                        html.Div("            3 : It is too late to stop global warming"),
                                        html.Div("            4 : I don't know")]
                            ),
                            dbc.ModalFooter(
                                dbc.Button("Close", id="close", className="ml-auto")
                    ),
            ],
            id="modal",
            scrollable = True
        ),],style = {'background-color' : 'lightgrey', 'padding' : '30px', 'margin-top' : '30px'})])],

                style={'width': '100%', 'height': 500, 'margin-left' : '15px', 'margin-top' : '15px',  
                        'display' : 'flex', 'flex-direction' : 'column', 'align-items': 'center'})
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
            ])], className='col-2', style ={'padding':20}),

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

