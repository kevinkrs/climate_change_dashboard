

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
    
    from dash.dependencies           import Input, Output
    
except Exception as e:
    print("Failed to load libraries :\n" + str(e))


def renewable():
    dataset = pd.read_csv("https://raw.githubusercontent.com/kevinkrs7/dashboard_seminar20/main/Mathis/Data/Situation_renewable-share-energy.csv?token=AR4CLWSRBHN72M52JJEC4DDAARUFQ")
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

wide_df = px.data.medals_wide()


def world_map1():
    df = pd.read_csv('https://raw.githubusercontent.com/kevinkrs7/dashboard_seminar20/main/Mathis/Data/data_situation2.csv?token=AR4CLWUP4A67XQ7FN6LAMMTAARUII')
    fig = px.choropleth(df, locations="CODE",
                        color="CO2_emissions", # lifeExp is a column of gapminder
                        hover_name="COUNTRY", # column to add to hover information
                        color_continuous_scale=px.colors.sequential.Plasma)
    fig.update_layout(title='CO2 emission per capita : 2019')
    return fig

def world_map2():
    df = pd.read_csv('https://raw.githubusercontent.com/kevinkrs7/dashboard_seminar20/main/Mathis/Data/data_situation2.csv?token=AR4CLWUP4A67XQ7FN6LAMMTAARUII')
    fig = px.choropleth(df, locations="CODE",
                        color="Death_from_air_pollution", # lifeExp is a column of gapminder
                        hover_name="COUNTRY", # column to add to hover information
                        color_continuous_scale=px.colors.sequential.Plasma)
    fig.update_layout(title='Death from air pollution : 2019')
    return fig

def world_map3():
    df = pd.read_csv('https://raw.githubusercontent.com/kevinkrs7/dashboard_seminar20/main/Mathis/Data/data_situation2.csv?token=AR4CLWUP4A67XQ7FN6LAMMTAARUII')
    fig = px.choropleth(df, locations="CODE",
                        color="Ozone_concentration", # lifeExp is a column of gapminder
                        hover_name="COUNTRY", # column to add to hover information
                        color_continuous_scale=px.colors.sequential.Plasma)
    fig.update_layout(title='Ozone concentration : 2019')
    return fig

def get_worldMaps():
    return [world_map1(),world_map2(),world_map3()]

def temperature():
    dataset = pd.read_csv("https://raw.githubusercontent.com/kevinkrs7/dashboard_seminar20/main/Mathis/Data/Situation_temperature-anomaly.csv?token=AR4CLWSOHWQSS7C2FCKMMFLAARUJW")
    dataset = dataset[(dataset.Entity == "Global")]
    dataset.columns = ['Entity','Year', 'Median', 'Upper_bound', 'Lower_bound']
    month = dataset['Year']
    Lower_bound = dataset['Lower_bound']
    Upper_bound = dataset['Upper_bound']
    Median = dataset['Median']
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=month, y=Median, name='Median',
                             line=dict(color='firebrick', width=2)))
    fig.add_trace(go.Scatter(x=month, y=Upper_bound, name='Upper bound',
                             line=dict(color='grey', width=1,dash='dot')))
    fig.add_trace(go.Scatter(x=month, y=Lower_bound, name='Lower bound',
                             line = dict(color='grey', width=1, dash='dot')))
    fig.update_layout(title='Global average temperatures',
                       xaxis_title='Year',
                       yaxis_title='Temperature change')
    return fig


def p1_updateLayout():

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
        dcc.Graph(id='p1WorldMap'))
    
    bot_leftSpace = html.Div(dcc.Graph(figure=temperature()))
    bot_rightSpace = html.Div(dcc.Graph(figure=renewable()))

    content = html.Div(
        [dbc.Row( [
            dbc.Col(
            leftSpace,className='col-2', style ={'padding':20}),
            dbc.Col(
            midSpace, className='col-12',style ={'padding':20}),]),
            
            dbc.Row( [
            dbc.Col(
            bot_leftSpace,className='col-6',style ={'padding':20}),
            dbc.Col(
            bot_rightSpace, className='col-6',style ={'padding':20}),],
            )],
        
            style={ 'width' : 'auto', 'padding' : 30, 'overflow' : 'hidden'},)
    
    return content
