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
        dcc.Dropdown(
        id='p4WorldMap_dm',
        options=[
            {'label': 'GDP', 'value': '0'},
            {'label': 'Risk 2018', 'value': '1'},
            {'label': 'Risk 1999-2018', 'value': '2'}
        ],
        value='0',
        #className='btn btn-success disabled',
        #labelStyle={'display': 'inline-block', 'padding-right':'10px'}
        ),
    ],)


        #Example : leftSpace = html.Div(Call_method_of_plotted_graph)
    midSpace = html.Div(
        dcc.Graph(id='p4WorldMap'))


    bot_leftSpace = html.Div([dcc.RadioItems(
        id='eu_fig_rb',
        options=[
            {'label': 'Full data', 'value': '0'},
            {'label': 'Trend', 'value': '1'}
        ],
        value='0',
        className='btn btn-success disabled',
        labelStyle={'display': 'inline-block', 'padding-right':'10px'}), 
        dcc.Graph(id='eu_fig')])

    bot_midSpace = html.Div([dcc.RadioItems(
        id='gdp_fig_rb',
        options=[
            {'label': 'Full data', 'value': '0'},
            {'label': 'Trend', 'value': '1'}
        ],
        value='0',
        className='btn btn-success disabled',
        labelStyle={'display': 'inline-block', 'padding-right':'10px'}), 
         
        dcc.Graph(id='gdp_fig')])

    #bot_rightSpace = html.Div(dcc.Graph(figure=get_iGreenBondData()))

    #In "content" the grid gets initialised and styled via HTML and CSS ==> If your graph doesent get displayed the right way you can adjust the styling or text Konstantin
    content = html.Div(
        [dbc.Row( [
            dbc.Col(
            leftSpace,
            className='col-2', style ={'padding':20}),
            dbc.Col(
            midSpace,
            className='col-10',style ={'padding':20}),],
            ),
            dbc.Row( [
            dbc.Col(
            bot_leftSpace,className='col-6',style ={'padding':20}),
            dbc.Col(
            bot_midSpace, className='col-6', style ={'padding':20}),
 #           dbc.Col(
 #           bot_rightSpace, className='col-4',style ={'padding':20}),],
 #            )
            ])],
            style={ 'width' : 'auto', 'padding' : 30, 'overflow' : 'hidden'})
    return content
