# %%
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import statsmodels.api as sm
import json
# %%
from pandas_datareader import data as pdr

import yfinance as yf


#Collecting and plotting Stock Market information on iShares Green Bond ETF
yf.pdr_override() # Override pandas datareader

def get_iGreenBondData():
    # download dataframe
    iGreenBond = pdr.get_data_yahoo("BGRN")
    graph  = px.line(iGreenBond, 
            x=iGreenBond.index, y="Adj Close", title='iShares Global Green Bond ETF', labels={'y':'Adjusted Close'})
    return graph

#######################################################################################################################################################################################

# %%
# ### Drop of GDP
# Importing the dataset with GDP Drop data and with created OECD Regions
df1 = pd.read_excel('data/Economic_Impact/GDP/C_Percentage change in regional GDP.xlsx')
df1_ols = pd.read_excel('data/Economic_Impact/GDP/C_Percentage change in regional GDP_ols.xlsx')
df2 = pd.read_excel('data/Economic_Impact/GDP/OECD Region.xlsx') #Datasheet with OECD Regions, Countries and country Codes
df1 = pd.melt(df1, id_vars=['Date'],value_vars=['OECD Europe', 'OECD Pacific', 'OECD America', 'Latin America',
       'Rest of Europe and Asia', 'Middle East and North Africa',
       'South and South-East Asia', 'Sub-Saharan Africa'])
df1_ols = pd.melt(df1_ols, id_vars=['Date'],value_vars=['OECD Europe', 'OECD Pacific', 'OECD America', 'Latin America',
        'Rest of Europe and Asia', 'Middle East and North Africa',
       'South and South-East Asia', 'Sub-Saharan Africa'])

df3=  pd.merge(df1, df2, on="variable")

#Map measures in percentage, so multiply with 100
df1['value']=df1['value']*100
df1_ols['value']=df1_ols['value']*100
df3['value']=df3['value']*100

# PLot
def get_dropGDP():
        #GDP Drop figgure Total Data
        graph  = px.bar(df1, 
            x='Date', 
            y="value", 
            color="variable", 
            title='Percentage change in regional GDP due to selected climate change impacts', 
            labels={'x':'Year', 'y':'Percentage change in regional GDP'},
            color_continuous_scale='Greens',
            )

        graph.update_xaxes(title='Year')
        graph.update_yaxes(title='Change of GDP in %')
        #graph.update_yaxes(autorange="reversed")

        #GDP Drop figgure for Trend
        fig_trend= (px.scatter( x=df1_ols['Date'], y=df1_ols['value'], trendline="ols", labels={'x':'Year', 'y':'Regression Value'},color_discrete_sequence=["#148C3F"], title='Trend of Percentage change in regional GDP due to selected climate change impacts'))
        #fig_trend.update_yaxes(autorange="reversed")
        return [graph,fig_trend]


def get_dropGDP_W():
        fig = px.choropleth(df3, locations="CODE",
                    color="value", # lifeExp is a column of gapminder
                    hover_name="variable", # column to add to hover information
                    color_continuous_scale=px.colors.sequential .OrRd[::-1],
                    animation_frame='Date',
                    range_color=[-4, 0])
        fig.update_layout(margin=dict(l=20,r=0,b=0,t=70,pad=0),paper_bgcolor="white",height= 700,title_text = 'Percentage change in regional GDP due to selected climate change impacts',font_size=18)
        
        return fig

# Variable time span : 2010-2060
# Data published by : OECD
# Link : https://www.oecd.org/statistics/climate-change-consequences-of-inaction.htm

#######################################################################################################################################################################################

# %%
# ### Climate Risk Assesment Drop in GDP 1999-2018
# Importing the dataset with Climate Risk Assesment data 
df1_gcr = pd.read_excel('data/Economic_Impact/GDP/Climate Risk Assesment/GLOBALCLIMATE RISKINDEX 2020_data concerning 1999-2018.xlsx')
df2_gcr = pd.read_excel('data/Economic_Impact/GDP/Climate Risk Assesment/GLOBALCLIMATE RISKINDEX 2020_data concerning 2018.xlsx')
df3_gcr = pd.read_excel('data/Economic_Impact/GDP/OECD Region.xlsx')   #Datasheet with OECD Regions, Countries and country Codes

df1_gcr=  pd.merge(df1_gcr, df3_gcr, on="Country")
df2_gcr=  pd.merge(df2_gcr, df3_gcr, on="Country")

# PLot
#Worldmap timespan 1999-2018
def get_RiskindexWorldmap1():
        fig_gcr = px.choropleth(df1_gcr, locations="CODE",
                    #color="Losses per unit GDP in % 1999-2018 (Rank)",
                    color='CRI score',
                    #hover_name="Country ", # column to add to hover information
                    color_continuous_scale=px.colors.sequential .Reds[::-1],
                    #color_continuous_midpoint = -0.9,
                    range_color=[100,0]
                    )
        fig_gcr.update_layout(margin=dict(l=20,r=0,b=0,t=70,pad=0),paper_bgcolor="white",height= 700,title_text = 'Climate Risk Index for 1999-2018',font_size=18)

        return fig_gcr

#Worldmap timespan 2018
def get_RiskindexWorldmap2():
        fig_gcr = px.choropleth(df2_gcr, locations="CODE",
                    color="CRI score", 
                    #hover_name="Country", # column to add to hover information
                    color_continuous_scale=px.colors.sequential .Reds[::-1],
                    range_color=[100,0]
                    )
        fig_gcr.update_layout(margin=dict(l=20,r=0,b=0,t=70,pad=0),paper_bgcolor="white",height= 700,title_text = 'Climate Risk Index for 2018',font_size=18)

        return fig_gcr

# Variable time span : 1999-2018
# Data published by : Germanwatch
# Link : https://www.germanwatch.org/fr/17307

#######################################################################################################################################################################################


#Collect all World Maps Figgures and return them according to drop down order

def get_worldMaps():
        return [get_dropGDP_W(),get_RiskindexWorldmap2(),get_RiskindexWorldmap1()]


#######################################################################################################################################################################################
# %%
# ### Economic damage caused by weather and climate-related extreme events in Europe (1980-2019)
# Importing the dataset
df_eea = pd.read_csv('data/Economic_Impact/EU_DMG/natural-disasters-events-3.csv', sep=',')
# PLot
def get_dmgEU():
        df_eea2 = df_eea.loc[df_eea['Chart'] == 'EU-28']
        fig = go.Figure(layout=go.Layout(
        title=go.layout.Title(text="Damage dealt to the EU economy by natural disasters in millions")
        ))
        fig.update_layout(barmode='stack')
        fig.update_xaxes(title='Year')
        fig.update_yaxes(title='EUR in millions')
        fig.add_trace(go.Bar(
        x=df_eea2['Year'],
        #y=df_eea['Type']=='Geophysical events',
        y=df_eea2.loc[df_eea2['Type'] == 'Geophysical events']['Value'],
        name='Geophysical events',
        marker_color='#148C3F',
        ))
        fig.add_trace(go.Bar(
        x=df_eea2['Year'],
        y=df_eea2.loc[df_eea2['Type'] == 'Climatological event']['Value'],
        name='Climatological event',
        marker_color='#45bf55'
        ))
        fig.add_trace(go.Bar(
        x=df_eea2['Year'],
        y=df_eea2.loc[df_eea2['Type'] == 'Hydrological event']['Value'],
        name='Hydrological event',
        marker_color='#97ed8a'
        ))
        fig.add_trace(go.Bar(
        x=df_eea2['Year'],
        y=df_eea2.loc[df_eea2['Type'] == 'Meteorological events']['Value'],
        name='Meteorological event',
        marker_color='#0b6129'
        ))

        #fig = px.bar(df_eea.loc[df_eea['Chart']=='EU-28'], x="Year", y="Value", color="Type", title="Damage dealt to the EU economy by natural disasters in millions",labels={'x':'Year', 'y':'EUR in million'})
        fig_trend= (px.scatter( x=df_eea['Year'], y=df_eea['Value'], trendline="ols", labels={'x':'Year', 'y':'Regression Value'},color_discrete_sequence=["#148C3F"], title='Trend of economic damage caused by<br> weather and climate-related extreme events in Europe'))

        return [fig, fig_trend]

# Variable time span : 1980-2019
# Data published by : European Environment Agency
# Link : https://www.eea.europa.eu/data-and-maps/daviz/natural-disasters-events-4#tab-googlechartid_chart_51




##################################################################################################################################################################
'''
# %%
# ### Damage dealt by floods in predic
# Importing the dataset with Dmg Flood data 
df1 = pd.read_excel('data\Economic_Impact\GDP\OECD Region.xlsx')

df1 = df1.rename(columns={"variable": "Region"})
df_dmg1= pd.read_excel('data\Economic_Impact\Impacts\Climate-related potential urban flood damages by region.xlsx')
df_dmg1 = df_dmg1.groupby(['Region']).sum()
df3=  pd.merge(df1, df_dmg1, on="Region")
df3.columns = df3.columns.map(str)
df3 = pd.melt(df3, id_vars=['CODE','Country','Region'],value_vars=['2010', '2030', '2080', '2080-GFDL','2080-IPSL', '2080-MIROC', '2080-NorESM'])


#Map measures in percentage, so multiply with 100
df3['value']=df3['value']*100

print(df_dmg1)
# PLot

def get_dropGDP_W1():
        fig = px.choropleth(df3, locations="CODE",
                    color="value", # lifeExp is a column of gapminder
                    hover_name="variable", # column to add to hover information
                    color_continuous_scale='reds',
                    animation_frame='variable',
                    #color_continuous_midpoint = -0.9,
                    range_color=[0,1000])

        fig.update_layout(margin=dict(l=20,r=0,b=0,t=70,pad=0),paper_bgcolor="white",height= 700,title_text = 'Percentage change in regional GDP due to selected climate change impacts',font_size=18)
        
        return fig

get_dropGDP_W1().show()

# Variable time span : 2010-2060
# Data published by : OECD
# Link : https://www.oecd.org/statistics/climate-change-consequences-of-inaction.htm

'''
