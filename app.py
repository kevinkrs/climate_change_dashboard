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
from data.technology_patents.maps import *
from data.technology_patents.graphs import *
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
        html.H2("Name", className="display-4"),
        html.Hr(),
        html.P(
            "Explanation", className="lead"
        ),

        #Navbar containing the menu list
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Topic 1", href="/page1", active="exact"),
                dbc.NavLink("Topic 2", href="/page2", active="exact"),
                dbc.NavLink("Topic 3", href="/page3", active="exact"),
                dbc.NavLink("Topic 4", href="/page4", active="exact"),
                dbc.NavLink("Topic 5", href="/page5", active="exact"),
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
        return dbc.Col([sidebar,home_updateLayout(),], style={ 'width' : '100%', 'height' : '100%',}, ),
    elif pathname == "/page1":
        return dbc.Col([sidebar,p1_updateLayout(),], style={ 'width' : '100%', 'height' : '100%',}, ),
    elif pathname == "/page2":
        return dbc.Col([sidebar,p2_updateLayout(),], style={ 'width' : '100%', 'height' : '100%',}, ),
    elif pathname == "/page3":
        return dbc.Col([sidebar,p3_updateLayout(),], style={ 'width' : '100%', 'height' : '100%',}, ),
    elif pathname == "/page4":
        return dbc.Col([sidebar,p4_updateLayout(),], style={ 'width' : '100%', 'height' : '100%',}, ),
    elif pathname == "/page5":
        return dbc.Col([sidebar,p5_updateLayout(),], style={ 'width' : '100%', 'height' : '100%',}, ),
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ])



@app.callback(
    Output('worldmap_patents', 'figure'),
    Input('dropdown1-left', 'value'))
def get_patent_map(selection):
    fig = get_world_maps()[int(selection)]
    return fig

@app.callback(
    Output('graph1_patents', 'figure'),
    Input('dropdown1-left', 'value'))
def get_patent_map(selection):
    fig = get_world_lg()[int(selection)]
    
    return fig

@app.callback(
    Output('graph2_patents', 'figure'),
    Input('dropdown1-left', 'value'))   
def get_patent_map(selection):
    fig = get_world_sg()[int(selection)]

    return fig


if __name__ == "__main__":
    app.run_server()