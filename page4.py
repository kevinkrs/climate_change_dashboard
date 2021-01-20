import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from data.Economic_Impact.graphs import get_iGreenBondData
from info_box.infop4 import get_infoBox4
#==> import external method from .py file from folder /data,  wwhich is plotting the graph

def p4_updateLayout():

    #Defining Spaces ==> Insert your plot into the spaces
    leftSpace = html.Div([
        html.H4('Indicators', style = {'color' : 'white'}),
        dcc.Dropdown(
        id='p4WorldMap_dm',
        options=[
            {'label': 'GDP', 'value': '0'},
            {'label': 'CRI 2018', 'value': '1'},
            {'label': 'CRI 1999-2018', 'value': '2'}
        ],
        value='0',
        #className='btn btn-success disabled',
        #labelStyle={'display': 'inline-block', 'padding-right':'10px'}
        ),
    ],style = {'margin-top' : 200, 'padding' : 10, 'margin-left' : 10, 'background-color' : 'lightgreen', 'border-radius' : 5})


        #Example : leftSpace = html.Div(Call_method_of_plotted_graph)
    midSpace = html.Div(
        dcc.Graph(id='p4WorldMap'), style={'padding':30, 'background-color':'#FFFFFF', 'border-radius': 10})


    bot_leftSpace = html.Div([dcc.RadioItems(
        id='eu_fig_rb',
        options=[
            {'label': 'Full data', 'value': '0'},
            {'label': 'Trend', 'value': '1'}
        ],
        value='0',
        className='btn btn-success disabled',
        style={'background-color':'#45bf55', 'border-color' : '#148C3F'},
        labelStyle={'display': 'inline-block', 'padding-right':'10px'}), 
        dcc.Graph(id='eu_fig')], style={'padding':30, 'background-color':'#FFFFFF', 'border-radius': 5})

    bot_midSpace = html.Div([dcc.RadioItems(
        id='gdp_fig_rb',
        options=[
            {'label': 'Full data', 'value': '0'},
            {'label': 'Trend', 'value': '1'}
        ],
        value='0',
        className='btn btn-success disabled',
        style={'background-color':'#45bf55', 'border-color' : '#148C3F'},
        labelStyle={'display': 'inline-block', 'padding-right':'10px'}), 
         
        dcc.Graph(id='gdp_fig')], style={'padding':30, 'background-color':'#FFFFFF', 'border-radius': 5})

    #bot_rightSpace = html.Div(dcc.Graph(figure=get_iGreenBondData()))

    #In "content" the grid gets initialised and styled via HTML and CSS ==> If your graph doesent get displayed the right way you can adjust the styling or text Konstantin
    content = html.Div(
        [dbc.Row( [
            dbc.Col(
            leftSpace,
            className='col-2', style ={'padding':15,'width':'100%', 'height':'100%'}),
            dbc.Col(
            midSpace,
            className='col-10',style ={'padding':35}),],
            ),
            dbc.Row( [
            dbc.Col(
            bot_leftSpace,className='col-6',style ={'padding':25}),
            dbc.Col(
            bot_midSpace, className='col-6', style ={'padding':25}),
 #           dbc.Col(
 #           bot_rightSpace, className='col-4',style ={'padding':20}),],
 #            )
            ])],
            style={ 'width' : 'auto', 'padding' : 30, 'overflow' : 'hidden'})
    return content
