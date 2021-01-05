import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output
#==> import external method from .py file from folder /data,  wwhich is plotting the graph

def p1_updateLayout():

    #Defining Spaces ==> Insert your plot into the spaces
    #Example : leftSpace = html.Div(Call_method_of_plotted_graph)
    midSpace = html.Div("Mid Space")

    bot_leftSpace = html.Div("Left Space")
    bot_rightSpace = html.Div("Right Space")

    #In "content" the grid gets initialised and styled via HTML and CSS ==> If your graph doesent get displayed the right way you can adjust the styling or text Konstantin
    content = html.Div(
        [dbc.Row( [
            dbc.Col(
            [midSpace, html.Div(
                style={'width': '100%', 'height': 500, 'background-color' : '#888888'},
            )], className='col-12',style ={'padding':20}),]),
            dbc.Row( [
            dbc.Col(
            bot_leftSpace,className='col-6',style ={'padding':20}),
            dbc.Col(
            bot_rightSpace, className='col-6',style ={'padding':20}),],
            )],
            style={ 'width' : 'auto', 'padding' : 30, 'overflow' : 'hidden'},)
    
    return content