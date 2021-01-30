import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output

def home_updateLayout():
#Defining Spaces ==> Insert your plot into the spaces
    leftSpace = html.Div(dbc.NavItem([dbc.NavLink([html.H3( className='fas fa-globe-europe'), html.A("Global Situation")], href="/page1", active="exact",)],style={ 'width':'100%','text-align': 'center'}), className="panel")
        #Example : leftSpace = html.Div(Call_method_of_plotted_graph)
    midSpace = html.Div([dbc.NavItem([dbc.NavLink([html.H2("Global Climate Change Dashboard", style={'font-size':27, 'font-weight': 10})], href="/", active="exact",)],style={ 'width':'100%','text-align': 'center'}),html.P('This dashboard combines and visualizes data on global climate change to illustrate its impact and evolution in recent years and in the future.'),], className="panel")
    rightSpace = html.Div(dbc.NavItem(dbc.NavLink([html.H3( className='fas fa-university'), html.A("Governmental efforts")], href="/page2", active="exact",),style={ 'width':'100%','text-align': 'center'}),className="panel")

    #Including and external graph via iFrame
    bot_leftSpace = html.Div(dbc.NavItem([dbc.NavLink([html.H3( className='fas fa-microscope'), html.A("Patents on technology")], href="/page3", active="exact",)],style={ 'width':'100%','text-align': 'center'}), className="panel")
    bot_midSpace = html.Div(dbc.NavItem([dbc.NavLink([html.H3( className='fas fa-industry'), html.A("Economic Impact")], href="/page4", active="exact",)],style={ 'width':'100%','text-align': 'center'}), className="panel")
    bot_rightSpace = html.Div(dbc.NavItem([dbc.NavLink([html.H3( className='fa fa-group'), html.A("Population attitude")], href="/page5", active="exact",)],style={ 'width':'100%','text-align': 'center'}), className="panel")

    #In "content" the grid gets initialised and styled via HTML and CSS ==> If your graph doesent get displayed the right way you can adjust the styling or text Konstantin
    content = html.Div(
        [dbc.Row( [
            dbc.Col(
            [leftSpace],className='col-4', style ={'padding':20, 'height':'45vh'}),
            dbc.Col(
            [midSpace], className='col-4',style ={'padding':20, 'height':'45vh'}),
            dbc.Col(
            [rightSpace], className='col-4', style ={'padding':20, 'height':'45vh'}),],
            ),
            dbc.Row( [
            dbc.Col(
            bot_leftSpace,className='col-4', style ={'padding':20, 'height':'45vh'}),
            dbc.Col(
            [bot_midSpace], className='col-4', style ={'padding':20, 'height':'45vh'}),
            dbc.Col(
            [bot_rightSpace], className='col-4',style ={'padding':20, 'height':'45vh'}),],
            )],
            style={ 'width' : 'auto', 'padding' : 30, 'overflow' : 'hidden'},)
    
    return content

