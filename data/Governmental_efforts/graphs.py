# -*- coding: utf-8 -*-
# %%
# libraries
try:
    import plotly.express   as px
    import plotly.graph_objs as go
    import pandas              as pd
    import json
except Exception as e:
    print("Failed to load libraries :\n" + str(e))



# %%
# ### Money pledged to spend on climate funds by countries
# Importing the dataset
dataset_pledges = pd.read_excel('data/Governmental_efforts/data/Governmental_efforts_climate funding_Pledges.xlsx')
dataset_pledges.columns = ['Fund','Fund Type', 'Fund Focus', 'Contributor', 'Country', 'Country Income Level','Region', 'Pledged (USD million current)', 'Deposited (USD million current)','test','test1']
dataset_pledges=dataset_pledges.groupby(by=["Country"])['Pledged (USD million current)', 'Deposited (USD million current)'].sum().reset_index()
dataset_pledges = dataset_pledges.nlargest(15, 'Pledged (USD million current)')
# PLot
def get_fundingGraph():
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=dataset_pledges['Country'],
        y=dataset_pledges['Pledged (USD million current)'],
        name='Pledged (USD million)',
        #marker_color='indianred'
    ))

    fig.add_trace(go.Bar(
        x=dataset_pledges['Country'],
        y=dataset_pledges['Deposited (USD million current)'],
        name='Deposited (USD million)',
        #marker_color='lightsalmon'
    ))


    # Here we modify the tickangle of the xaxis, resulting in rotated labels.
    fig.update_layout(barmode='group', xaxis_tickangle=-45, title='Money pledged and deposited for climate funds by countries')
    return fig




# Variable time span : -
# Data published by : Climate Funds Update - Heinrich Böll Stiftung
# Link : https://climatefundsupdate.org/data-dashboard/#1541245664232-8e27b692-05c8

'''
# %%
# ### Funding by type
# Importing the dataset
df_nzc = pd.read_excel('data/Governmental_efforts/ClimateWatch/net_zero_content.xlsx')
df3_gcr = pd.read_excel('data/Economic_Impact/GDP/OECD Region.xlsx')   #Datasheet with OECD Regions, Countries and country Codes

df_nzc=  pd.merge(df_nzc, df3_gcr, on="Country")
# PLot
#Worldmap Net Zero Target Tracker
def get_NetZeroTargetWM():
        fig_nzc = px.choropleth(df_nzc, locations="CODE",
                    color='Target Year',
                    color_continuous_scale='Greens',
                    hover_name='Country',
                    hover_data=['Target Year'],
                    )
        fig_nzc.update_layout(margin=dict(l=20,r=0,b=0,t=70,pad=0),paper_bgcolor="white",height= 700,title_text = 'Net-Zero Tracker',font_size=18)

        return fig_nzc

# Variable time span : -
# Data published by : Climate Watch
# Link : https://www.climatewatchdata.org/data-explorer/net-zero-content?net-zero-content-categories=&net-zero-content-countries=All%20Selected&net-zero-content-indicators=nz_status&page=1

'''
# %%
# ### Funding by type
# Importing the dataset
df_nzc = pd.read_csv('data/Governmental_efforts/Net Zero Tracker/countries.csv')

with open('data/Worldmap shapes/custom.geo.json') as f:
  geojson = json.load(f)

# PLot
#Worldmap Net Zero Target Tracker
def get_NetZeroTargetWM():
        fig_nzc = px.choropleth_mapbox(df_nzc, geojson=geojson, locations="Abbreviation",
                    color='Target Status',
                    mapbox_style="carto-positron",
                    featureidkey="properties.sov_a3",
                    hover_name='Title',
                    hover_data=['Target Year'],
                    zoom=1,
                    opacity=0.8,
                    center = {"lat": 50.958427, "lon": 10.436234},
                    )
        fig_nzc.update_layout(margin=dict(l=20,r=0,b=0,t=70,pad=0),paper_bgcolor="white",height= 700,title_text = 'Net-Zero Tracker',font_size=18)
        
        return fig_nzc

# Variable time span : -
# Data published by : Climate Watch
# Link : https://www.climatewatchdata.org/data-explorer/net-zero-content?net-zero-content-categories=&net-zero-content-countries=All%20Selected&net-zero-content-indicators=nz_status&page=1
