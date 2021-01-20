try:
    
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
    
    from info_box.infop1 import get_infoBox1
    
except Exception as e:
    print("Failed to load libraries :\n" + str(e))

# In[]: Graph function

def renewable():
    dataset = pd.read_csv('data/World_Situation/Situation_renewable-share-energy.csv')
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


def energie():
    dataset = pd.read_csv('data/World_Situation/data_situation3.csv')
    dataset.columns = ['Number','Entity','Year','Oil', 'Coal', 'Gas']
    dataset["Indice"] = 0
    
    for i in range(3087):
        if dataset.iloc[i, 1] == "United States":
            dataset.iloc[i, 1] = "US"
        if dataset.iloc[i, 1] == "World":
            dataset.iloc[i, 6] = 1
     
    df0 = dataset[dataset.Entity.isin(["World"])]
    df1 = dataset[dataset.Entity.isin(["India"])]
    df2 = dataset[dataset.Entity.isin(["Africa"])]
    df3 = dataset[dataset.Entity.isin(["US"])]
    df4 = dataset[dataset.Entity.isin(["China"])]
    df5 = dataset[dataset.Entity.isin(["Europe"])]
     
    dataset = pd.concat([df0, df1,df2,df3, df4, df5], ignore_index=True)       
    
    fig_energie = px.bar(dataset, x="Entity", y=["Oil", "Coal", "Gas"], title="Long-Form Input", animation_frame="Year")
    fig_energie.update_layout(yaxis_range=[0,300])
    
    fig_energie.update_layout(title = "Energy consumption per capita", title_x = 0.5, title_font_size = 15, showlegend=False)
    fig_energie.update_layout(xaxis_title='Entity', yaxis_title='Energy')
    return fig_energie

def get_worldMaps_page_1_2():
    return [renewable(),energie()]


def world_map_page1_1():
    df = pd.read_csv('data/World_Situation/data_situation2.csv')
    fig = px.choropleth(df, locations="CODE",
                        color="CO2_emissions", # lifeExp is a column of gapminder
                        hover_name="COUNTRY", # column to add to hover information
                        color_continuous_scale=px.colors.sequential.Plasma)
    #fig.update_layout(title='CO2 emission per capita : 2019')
    fig.update_layout(margin=dict(l=20,r=0,b=0,t=70,pad=0),paper_bgcolor="white",height= 700,title_text = 'CO2 emission per capita : 2019',font_size=18)
    return fig

def world_map_page1_2():
    df = pd.read_csv('data/World_Situation/data_situation2.csv')
    fig = px.choropleth(df, locations="CODE",
                        color="Death_from_air_pollution", # lifeExp is a column of gapminder
                        hover_name="COUNTRY", # column to add to hover information
                        color_continuous_scale=px.colors.sequential.Plasma)
    #fig.update_layout(title='Death from air pollution : 2019')
    fig.update_layout(margin=dict(l=20,r=0,b=0,t=70,pad=0),paper_bgcolor="white",height= 700,title_text = 'Death from air pollution : 2019',font_size=18)
    return fig

def world_map_page1_3():
    df = pd.read_csv('data/World_Situation/data_situation2.csv')
    fig = px.choropleth(df, locations="CODE",
                        color="Ozone_concentration", # lifeExp is a column of gapminder
                        hover_name="COUNTRY", # column to add to hover information
                        color_continuous_scale=px.colors.sequential.Plasma)
    #fig.update_layout(title='Ozone concentration : 2019')
    fig.update_layout(margin=dict(l=20,r=0,b=0,t=70,pad=0),paper_bgcolor="white",height= 700,title_text = 'Ozone concentration : 2019',font_size=18)
    return fig

def get_worldMaps_page_1_1():
    return [world_map_page1_1(),world_map_page1_2(),world_map_page1_3()]

def temperature_page1():
    dataset = pd.read_csv('data/World_Situation/Situation_temperature-anomaly.csv')
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

    
## PAGE 1 ##

def p1_updateLayout():

    leftSpace = html.Div([
                html.H4('Indicators', style = {'color' : 'white'}),
                dcc.Dropdown(
                    id = 'p1WorldMap_dm',
                    options = [
                        {'label' : 'CO2 emissions', 'value': '0'},
                        {'label' : 'Death from air pollution', 'value' : '1'},
                        {'label' : 'Ozone concentration', 'value' : '2'}
                    ],
                    value = '0',style = {'margin-bottom' : 10}),
                dcc.Dropdown(
                    id = 'p1WorldMap_dm2',
                    options = [
                        {'label' : 'Renewable', 'value': '0'},
                        {'label' : 'Energy', 'value' : '1'},
                    ],
                    value = '0',)
                ], style = {'margin-top' : 200, 'padding' : 10, 'margin-left' : 10, 'background-color' : 'lightgreen', 'border-radius' : 5} )
    
    midSpace = html.Div(
        dcc.Graph(id='p1WorldMap'), style={'padding':30, 'background-color':'#FFFFFF'} )
    
    bot_rightSpace = html.Div(
        dcc.Graph(id='p1WorldMap2'),style={'padding':30, 'background-color':'#FFFFFF'})
    
    bot_leftSpace = html.Div(dcc.Graph(figure=temperature_page1()),style={'padding':30, 'background-color':'#FFFFFF'})
    
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
