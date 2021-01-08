# CDxx #

try:
    
    import os
    import dash
    
    import matplotlib.pyplot         as plt
    import numpy                     as np
    import pandas                    as pd
    import plotly.express            as px
    import pandas                    as pd
    import plotly.graph_objects      as go
    import dash_html_components      as html
    import dash_bootstrap_components as dbc
    import dash_core_components      as dcc
    
    from dash.dependencies import Input, Output
    
except Exception as e:
    print("Failed to load libraries :\n" + str(e))


def renewable():
    dataset = pd.read_csv("/Users/" + os.environ["USER"] + "/Desktop/Dashboard/Archive2/Situation_renewable-share-energy.csv")
    dataset.columns = ['Entity','Code','Year', 'Renewables']
    dataset["Indice"] = 0
    
    for i in range(4284):
        if dataset.iloc[i, 0] == "United States":
            dataset.iloc[i, 0] = "US"
        if dataset.iloc[i, 0] == "World":
            dataset.iloc[i, 4] = 1
    
    df0 = dataset[dataset.Entity.isin(["World"])]
    df1 = dataset[dataset.Entity.isin(["India"])]
    df2 = dataset[dataset.Entity.isin(["Africa"])]
    df3 = dataset[dataset.Entity.isin(["US"])]
    df4 = dataset[dataset.Entity.isin(["China"])]
    df5 = dataset[dataset.Entity.isin(["Europe"])]
    
    dataset = pd.concat([df0, df1,df2,df3, df4, df5], ignore_index=True)
    
    histogram = px.histogram(dataset, x = "Entity", y = "Renewables", histfunc='avg',
                            color = "Indice",
                            animation_frame="Year")
    
    histogram.update_layout(yaxis_range=[0,20])
    histogram.update_layout(title = "Share of renewable energies", title_x = 0.5, title_font_size = 15, showlegend=False)
    
    histogram.update_layout(xaxis_title='Entity', yaxis_title='Percentage')
        
    return histogram


def world_map1():
    df = pd.read_csv('/Users/mati/Desktop/Dashboard/Data/data_situation2.csv')
    fig = px.choropleth(df, locations="CODE",
                        color="CO2_emissions", # lifeExp is a column of gapminder
                        hover_name="COUNTRY", # column to add to hover information
                        color_continuous_scale=px.colors.sequential.Plasma)
    
    fig.update_layout(title='CO2 emission per capita : 2019')
    
    return fig

def world_map2():
    df = pd.read_csv('/Users/mati/Desktop/Dashboard/Data/data_situation2.csv')
    fig = px.choropleth(df, locations="CODE",
                        color="Death_from_air_pollution", # lifeExp is a column of gapminder
                        hover_name="COUNTRY", # column to add to hover information
                        color_continuous_scale=px.colors.sequential.Plasma)
    
    fig.update_layout(title='CO2 emission per capita : 2019')
    
    return fig

def world_map3():
    df = pd.read_csv('/Users/mati/Desktop/Dashboard/Data/data_situation2.csv')
    fig = px.choropleth(df, locations="CODE",
                        color="Ozone_concentration", # lifeExp is a column of gapminder
                        hover_name="COUNTRY", # column to add to hover information
                        color_continuous_scale=px.colors.sequential.Plasma)
    
    fig.update_layout(title='CO2 emission per capita : 2019')
    
    return fig

def get_worldMaps():
    return [world_map1(),world_map2(),world_map3()]



def temperature():
    
    dataset = pd.read_csv("/Users/" + os.environ["USER"] + "/Desktop/Dashboard/Archive2/Situation_temperature-anomaly.csv")
    dataset = dataset[(dataset.Entity == "Global")]
    dataset.columns = ['Entity','Year', 'Median', 'Upper_bound', 'Lower_bound']

    month = dataset['Year']
    
    Lower_bound = dataset['Lower_bound']
    Upper_bound = dataset['Upper_bound']
    Median = dataset['Median']
    
    fig = go.Figure()
    # Create and style traces
    fig.add_trace(go.Scatter(x=month, y=Median, name='Median',
                             line=dict(color='firebrick', width=2)))
    fig.add_trace(go.Scatter(x=month, y=Upper_bound, name='Upper bound',
                             line=dict(color='grey', width=1,dash='dot')))
    fig.add_trace(go.Scatter(x=month, y=Lower_bound, name='Lower bound',
                             line = dict(color='grey', width=1, dash='dot')))

    
    # Edit the layout
    fig.update_layout(title='Global average temperatures',
                       xaxis_title='Year',
                       yaxis_title='Temperature change')
    return fig

## PAGE HOME ##

def home_updateLayout():
#Defining Spaces ==> Insert your plot into the spaces
    leftSpace = html.Div("Linker Space")
        #Example : leftSpace = html.Div(Call_method_of_plotted_graph)
    midSpace = html.Div("Mid Space")
    rightSpace = html.Div("Rechter Space")

    #Including and external graph via iFrame
    bot_leftSpace = html.Iframe( src = "https://datahub.io/core/glacier-mass-balance/view/0", style ={'width' : "100%", 'overflow' : 'hidden', 'height' : 475, 'frameborder' :0,} )
    bot_midSpace = html.Div("Mid Space")
    bot_rightSpace = html.Div("Rechter Space")

    #In "content" the grid gets initialised and styled via HTML and CSS ==> If your graph doesent get displayed the right way you can adjust the styling or text Konstantin
    content = html.Div(
        [dbc.Row( [
            dbc.Col(
            [leftSpace, html.Div(
                style={'width': '100%', 'height': 500, 'background-color' : '#59FF00'},
            )],className='col-2', style ={'padding':20}),
            dbc.Col(
            [midSpace, html.Div(
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

## PAGE 1 ##

def p1_updateLayout():

    #Defining Spaces ==> Insert your plot into the spaces
    #Example : leftSpace = html.Div(Call_method_of_plotted_graph)
    leftSpace = html.Div(
        dcc.Dropdown(
            id = 'p1WorldMap_dm',
            options = [
                {'label' : 'CO2_emissions', 'value': '0'},
                {'label' : 'Death_from_air_pollution', 'value' : '1'},
                {'label' : 'Ozone_concentration', 'value' : '2'}
            ],
            value = '0',
            ))
    
    midSpace = html.Div(
        dcc.Graph(id='p4WorldMap'))
    
    bot_leftSpace = html.Div(dcc.Graph(figure=temperature()))
    bot_rightSpace = html.Div(dcc.Graph(figure=renewable()))

    #In "content" the grid gets initialised and styled via HTML and CSS ==> If your graph doesent get displayed the right way you can adjust the styling or text Konstantin
    content = html.Div(
        [dbc.Row( [
            dbc.Col(
            leftSpace,className='col-2', style ={'padding':20}),
            dbc.Col(
            midSpace, className='col-10',style ={'padding':20}),]),
            
            dbc.Row( [
            dbc.Col(
            bot_leftSpace,className='col-6',style ={'padding':20}),
            dbc.Col(
            bot_rightSpace, className='col-6',style ={'padding':20}),],
            )],
        
            style={ 'width' : 'auto', 'padding' : 30, 'overflow' : 'hidden'},)
    
    return content

## PAGE 2 ##

def p2_updateLayout():
    #Defining Spaces ==> Insert your plot into the spaces
    leftSpace = html.Div("Mid Space")
        #Example : leftSpace = html.Div(Call_method_of_plotted_graph)
    midSpace = html.Div("Mid Space")
    rightSpace = html.Div("Mid Space")

    bot_leftSpace = html.Iframe( src = "https://datahub.io/core/glacier-mass-balance/view/0", style ={'width' : "100%", 'overflow' : 'hidden', 'height' : 475, 'frameborder' :0,} )
    bot_midSpace = html.Div("Mid Space")
    bot_rightSpace = html.Div("Rechter Space")

    #In "content" the grid gets initialised and styled via HTML and CSS ==> If your graph doesent get displayed the right way you can adjust the styling or text Konstantin
    content = html.Div(
        [dbc.Row( [
            dbc.Col(
            [leftSpace, html.Div(
                style={'width': '100%', 'height': 500, 'background-color' : '#000000'},
            )],className='col-2', style ={'padding':20}),
            dbc.Col(
            [midSpace, html.Div(
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

## PAGE 3 ##

def p3_updateLayout():
    #Defining Spaces ==> Insert your plot into the spaces
    leftSpace = html.Div("Linker Space")
        #Example : leftSpace = html.Div(Call_method_of_plotted_graph)
    midSpace = html.Div("Mid Space")
    rightSpace = html.Div("Rechter Space")

    bot_leftSpace = html.Iframe( src = "https://datahub.io/core/glacier-mass-balance/view/0", style ={'width' : "100%", 'overflow' : 'hidden', 'height' : 475, 'frameborder' :0,} )
    bot_midSpace = html.Div("Mid Space")
    bot_rightSpace = html.Div("Rechter Space")

    #In "content" the grid gets initialised and styled via HTML and CSS ==> If your graph doesent get displayed the right way you can adjust the styling or text Konstantin
    content = html.Div(
        [dbc.Row( [
            dbc.Col(
            [leftSpace, html.Div(
                style={'width': '100%', 'height': 500, 'background-color' : '#FF00EC'},
            )],className='col-2', style ={'padding':20}),
            dbc.Col(
            [midSpace, html.Div(
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

## PAGE 4 ##


def p4_updateLayout():
    #Defining Spaces ==> Insert your plot into the spaces
    leftSpace = html.Div("Linker Space")
        #Example : leftSpace = html.Div(Call_method_of_plotted_graph)
    midSpace = html.Div("Mid Space")
    rightSpace = html.Div("Rechter Space")

    bot_leftSpace = html.Iframe( src = "https://datahub.io/core/glacier-mass-balance/view/0", style ={'width' : "100%", 'overflow' : 'hidden', 'height' : 475, 'frameborder' :0,} )
    bot_midSpace = html.Div("Mid Space")
    bot_rightSpace = html.Div("Rechter Space")

    #In "content" the grid gets initialised and styled via HTML and CSS ==> If your graph doesent get displayed the right way you can adjust the styling or text Konstantin
    content = html.Div(
        [dbc.Row( [
            dbc.Col(
            [leftSpace, html.Div(
                style={'width': '100%', 'height': 500, 'background-color' : '#FFFB00'},
            )],className='col-2', style ={'padding':20}),
            dbc.Col(
            [midSpace, html.Div(
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

## PAGE 5 ##

def p5_updateLayout():
    #Defining Spaces ==> Insert your plot into the spaces
    leftSpace = html.Div("Linker Space")
        #Example : leftSpace = html.Div(Call_method_of_plotted_graph)
    midSpace = html.Div("Mid Space")
    rightSpace = html.Div("Rechter Space")

    bot_leftSpace = html.Iframe( src = "https://datahub.io/core/glacier-mass-balance/view/0", style ={'width' : "100%", 'overflow' : 'hidden', 'height' : 475, 'frameborder' :0,} )
    bot_midSpace = html.Div("Mid Space")
    bot_rightSpace = html.Div("Rechter Space")

    #In "content" the grid gets initialised and styled via HTML and CSS ==> If your graph doesent get displayed the right way you can adjust the styling or text Konstantin
    content = html.Div(
        [dbc.Row( [
            dbc.Col(
            [leftSpace, html.Div(
                style={'width': '100%', 'height': 500, 'background-color' : '#FF6400'},
            )],className='col-2', style ={'padding':20}),
            dbc.Col(
            [midSpace, html.Div(
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

########################################################################################################################################

#Inititalise app    and it's style for the theme
app = dash.Dash(external_stylesheets=[dbc.themes.LUX])


# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "display" : "inline-block",
    "float" : "left",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "height": "100vh",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}
#Sidebar conaining the menu
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
    style=SIDEBAR_STYLE,
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
    Output('p4WorldMap', 'figure'),
    Input('p4WorldMap_dm', 'value'))

def update_figure(selection):
    fig = get_worldMaps()[int(selection)]
    return fig

if __name__ == "__main__":
    app.run_server(port = 8050)
