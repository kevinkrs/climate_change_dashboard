import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input
from dash.dependencies import Output
from home import home_updateLayout
from page1 import p1_updateLayout
from page2 import p2_updateLayout
from page3 import p3_updateLayout
from page4 import p4_updateLayout
from page5 import p5_updateLayout
from data.Economic_Impact.graphs import get_dmgEU, get_dropGDP, get_worldMaps

from data.technology_patents.maps import *
from data.technology_patents.graphs import *
from data.technology_patents.histograms import *
#Inititalise app    and it's style for the theme
app = dash.Dash(external_stylesheets=[dbc.themes.FLATLY, '/assets/style.css'])



# the styles for the main content position it to the right of the sidebar and
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}
#Sidebar containing the menu
sidebar = html.Div(
    [
        html.H2("Seminar", className="display-4"),
        html.Hr(),
        html.P(
            "Topics", className="lead"
        ),

        #Navbar containing the menu list
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact", className='nav-item'),
                dbc.NavLink("Topic 1", href="/page1", active="exact", className='nav-item'),
                dbc.NavLink("Topic 2", href="/page2", active="exact", className='nav-item'),
                dbc.NavLink("Topic 3", href="/page3", active="exact", className='nav-item'),
                dbc.NavLink("Topic 4", href="/page4", active="exact", className='nav-item'),
                dbc.NavLink("Topic 5", href="/page5", active="exact", className='nav-item'),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className='sidebar', 
)

#Footer
footer = dbc.Container(html.Div(dbc.Container("Footer", className='text-center p-3',),
    className='container-fluid',), className='fixed-bottom', )

app.layout = html.Div([dcc.Location(id="url"), html.Div(id='page-content'), footer], style={ 'width' : '100%', 'height' : '100%',},) 

#Routing for the mutiple pages
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return dbc.Col([sidebar,home_updateLayout(),], style={ 'width' : '100%', 'height' : '100%',}, className='innerFrame' ),
    elif pathname == "/page1":
        return dbc.Col([sidebar,p1_updateLayout(),], style={ 'width' : '100%', 'height' : '100%',}, className='innerFrame', ),
    elif pathname == "/page2":
        return dbc.Col([sidebar,p2_updateLayout(),], style={ 'width' : '100%', 'height' : '100%',}, className='innerFrame', ),
    elif pathname == "/page3":
        return dbc.Col([sidebar,p3_updateLayout(),], style={ 'width' : '100%', 'height' : '100%',}, className='innerFrame', ),
    elif pathname == "/page4":
        return dbc.Col([sidebar,p4_updateLayout(),], style={ 'width' : '100%', 'height' : '100%',}, className='innerFrame', ),
    elif pathname == "/page5":
        return dbc.Col([sidebar,p5_updateLayout(),], style={ 'width' : '100%', 'height' : '100%',}, className='innerFrame', ),
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ])


# Callback for different patent worldmaps 
@app.callback(
    Output('worldmap_patents', 'figure'),
    Input('dropdown_po', 'value'),
    Input('dropdown_number', 'value'))
def get_patent_map(selection_x,selection_y):
    if(selection_x == '0' and selection_y == '0'):
        fig = get_maps_patent()[0]
        return fig

    elif(selection_x == '1' and selection_y == '0'):
        fig = get_maps_patent()[1]
        return fig
    
    elif(selection_x == '2' and selection_y == '0'):
        fig = get_maps_patent()[2]
        return fig

    elif(selection_x == '0' and selection_y == '1'):
        fig = get_maps_patent()[3]
        return fig

    elif(selection_x == '1' and selection_y == '1'):
        fig = get_maps_patent()[4]
        return fig

    else:
        fig = get_maps_patent()[5]
        return fig 

# Callback for different scatter plots on evrionmental related technology patents
@app.callback(
    Output('scatter_patents_env', 'figure'),
    Input('dropdown_po', 'value'),
    Input('dropdown_number', 'value'))   
def get_graphs(selection_x, selection_y):
    if(selection_x == '0' and selection_y == '0'):
        fig =get_graphs_patent()[0]
        return fig

    elif(selection_x == '1' and selection_y == '0'):
        fig = get_graphs_patent()[1]
        return fig
    
    elif(selection_x == '2' and selection_y == '0'):
        fig = get_graphs_patent()[2]
        return fig

    elif(selection_x == '0' and selection_y == '1'):
        fig = get_graphs_patent()[3]
        return fig

    elif(selection_x == '1' and selection_y == '1'):
        fig = get_graphs_patent()[4]
        return fig

    else:
        fig = get_graphs_patent() [5]
        return fig 

@app.callback(
    Output('histogram_total_env', 'figure'),
    Input('dropdown_po', 'value'))
def get_patent_hist(selection):
    fig = get_hist_patents()[int(selection)]

    return fig




#Callback Page 4 ==> EU Graph (Left Bottom)
@app.callback(
    Output('eu_fig', 'figure'),
    Input('eu_fig_rb', 'value'))

def update_figure(selection):
    fig=get_dmgEU()[int(selection)]
    return fig

#Callback Page 4 ==> GDP Graph (Mid Bottom)
@app.callback(
    Output('gdp_fig', 'figure'),
    Input('gdp_fig_rb', 'value'))

def update_figure(selection):
    fig=get_dropGDP()[int(selection)]
    return fig

#Callback Page 4 ==> WorldMap
@app.callback(
    Output('p4WorldMap', 'figure'),
    Input('p4WorldMap_dm', 'value'))

def update_output(selection):
    fig=get_worldMaps()[int(selection)]
    return fig

if __name__ == "__main__":
    app.run_server()