import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output
from data.Economic_Impact.graphs import get_iGreenBondData
from data.Governmental_efforts.graphs import get_fundingGraph, get_fundingGraph, get_pledgedGraph
#==> import external method from .py file from folder /data,  wwhich is plotting the graph

def p2_updateLayout():
    #Defining Spaces ==> Insert your plot into the spaces
    leftSpace = html.Div("Linker Space")
        #Example : leftSpace = html.Div(Call_method_of_plotted_graph)
    midSpace = html.Div("Mid Space")
    rightSpace = html.Div("Rechter Space")

    bot_leftSpace = html.Div("Left Bottom Space")
    bot_midSpace = html.Div(dcc.Graph(figure=get_pledgedGraph()))
    bot_rightSpace = html.Div(dcc.Graph(figure=get_fundingGraph()))

    #In "content" the grid gets initialised and styled via HTML and CSS ==> If your graph doesent get displayed the right way you can adjust the styling or text Konstantin
    content = html.Div(
        [dbc.Row( [
            dbc.Col(
            leftSpace,className='col-2', style ={'padding':20}),
            dbc.Col(
            midSpace, className='col-10',style ={'padding':20, 'background-color':'#97ed8a','height' : '500'}),],
            ),
            dbc.Row( [
            dbc.Col(
            bot_leftSpace,className='col-4',style ={'padding':20, 'background-color':'#97ed8a'}),
            dbc.Col(
            bot_midSpace, className='col-4', style ={'padding':20}),
            dbc.Col(
            bot_rightSpace, className='col-4',style ={'padding':20}),],
            )],
            style={ 'width' : 'auto', 'padding' : 30, 'overflow' : 'hidden'},)
    
    return content