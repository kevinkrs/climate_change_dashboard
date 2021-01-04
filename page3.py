
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import json
import pycountry
import geojson

#==> import external method from .py file from folder /data,  wwhich is plotting the graph

# Testing
df1 = pd.read_csv('data/technology_patents/epo_total_2018.csv', sep = ";")

df1.head()
def alpha3code(column): 
    CODE = []
    for country in column:
        try: 
            code = pycountry.countries.get(name=country).alpha_3
            CODE.append(code)
        except: 
            CODE.append('None')
    return CODE

df1['iso_alpha'] = alpha3code(df1.Country)
#df1['iso_a3']  = df1['iso_a3'].astype(str)

print(df1.head())

with open('data/custom.geo.json') as f: 
    gj = json.load(f)

# print(gj["features"][5])

'''world_map = go.Figure(go.Choroplethmapbox(geojson = gj, featureidkey = 'properties.iso_a3', locations = df1.iso_a3, z = df1.Value,
                                    colorscale="Viridis", zmin=0, zmax=12,
                                    marker_opacity=0.5, marker_line_width=0))
world_map.update_layout(mapbox_style="carto-positron",
                  mapbox_zoom=1.6, mapbox_center = {"lat": 49.006871, "lon": 8.40342})

world_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0})'''

'''world_map = px.choropleth(df1, locations="iso_alpha",
                    color="Value",
                    hover_name = "Country", 
                    color_continuous_scale='Viridis')'''

world_map = px.choropleth_mapbox(df1, geojson=gj, locations='iso_alpha', color='Value',
            color_continuous_scale="Viridis",
            range_color=(0, 12),
            mapbox_style="carto-positron",
            zoom=1.6, center = {"lat": 49.006871, "lon": 8.40342},
            opacity=0.5,
            #labels={'Value':'Patents'}
            )
#world_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0})



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
                options =[{'label' : 'EPO', 'value' : 'EPO' },
                          {'label' : 'USPTO', 'value' : 'USPOT'},
                          {'label' : 'PCT', 'value' : 'PCT'}], 
                          value = 'EPO',
                          placeholder = 'Select patent office', style = {'margin-bottom' : 10, 'margin-top' : 10}),
                html.Div(id='dropdown1-content'),
                
                dcc.Dropdown(id ='dropdown2-left',
                options =[{'label' : 'Total', 'value' : 'Total' },
                          {'label' : 'Environmental-related', 'value' : 'Enivornmental-related'}],
                          value = 'Environmental-related',
                          placeholder = 'Select technology domain'),
                html.Div(id='dropdown2-content')],
                style={'width': '100%', 'height': 500, 'background-color' : '#33FFFC'},
            )],className='col-2', style ={'padding':20}),
            dbc.Col(
            [midSpace, html.Div([
                dcc.Graph(figure=world_map, style = {'height' : 500})
            ],
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

