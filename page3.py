from lib.lib import *
import json
from data.technology_patents.maps import *
from data.technology_patents.graphs import *


#==> import external method from .py file from folder /data,  wwhich is plotting the graph


def p3_updateLayout():
    #Defining Spaces ==> Insert your plot into the spaces
    leftSpace = html.Div([
        html.H4('Indicators', style = {'color' : 'white'}),
            dcc.Dropdown(id = 'dropdown_po', 
                    options =[{'label' : 'EPO', 'value' : '0' },
                            {'label' : 'USPTO', 'value' : '1'},
                            {'label' : 'PCT', 'value' : '2'}], 
                            value = '0',
                            placeholder = 'Select patent office',  style = {'margin-bottom' : 10}),
            dcc.Dropdown(id ='dropdown_number',
                    options =[{'label' : 'Relative (%)', 'value' : '0'},
                                {'label' : 'Environmental', 'value' : '1'},
                                {'label' : 'Total', 'value' : '2' }],
                            value = '2',
                            placeholder = 'Select technology domain')], 
                        style = {'margin-top' : 200, 'padding' : 10, 'margin-left' : 10, 'background-color' : 'lightgreen', 'border-radius' : 5})
        #Example : leftSpace = html.Div(Call_method_of_plotted_graph)
    #midSpace = html.Div(dcc.Graph(figure = get_world_map_epo_total())) 
    midSpace = html.Div(dcc.Loading(dcc.Graph(id = 'worldmap_patents'),color='#45bf55', type='default', className='pv6'), style={'padding':30, 'background-color':'#FFFFFF', 'border-radius': 10}) 
    #rightSpace = html.Div("Rechter Space")

    bot_leftSpace = html.Div(dcc.Loading(dcc.Graph(id = 'scatter_patents_env'),color='#45bf55', type='default', className='pv6'))
    #bot_midSpace = html.Div("Mid Space")
    bot_rightSpace = html.Div(dcc.Loading(dcc.Graph(id = 'histogram_total_env'),color='#45bf55', type='default', className='pv6'))

    #In "content" the grid gets initialised and styled via HTML and CSS ==> If your graph doesent get displayed the right way you can adjust the styling or text Konstantin
    content = html.Div([
        dbc.Row( [
            dbc.Col(
            [leftSpace, html.Div([        
            ])],
             className='col-2', style ={'padding':20,'width':'100%', 'height':'100%'}),

            dbc.Col(
            [midSpace, html.Div(
            )], className='col-10',style ={'padding':30}),]),

        dbc.Row( [
            dbc.Col(
            bot_leftSpace, className='col-6', style ={'padding':20}),
            dbc.Col(
            [bot_rightSpace, html.Div(
            )], className='col-6',style ={'padding':20}),]
            )],
            style={ 'width' : 'auto',  'overflow' : 'hidden', 'padding' : '30'}) # other nice color #7ED6F0

    return content



