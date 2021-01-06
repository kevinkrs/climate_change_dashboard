# %%
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import statsmodels.api as sm

# %%
from pandas_datareader import data as pdr

import yfinance as yf

# %%

#Collecting and plotting Stock Market information on iShares Green Bond ETF
yf.pdr_override() # Override pandas datareader

def get_iGreenBondData():
    # download dataframe
    iGreenBond = pdr.get_data_yahoo("BGRN")
    graph  = px.line(iGreenBond, 
            x=iGreenBond.index, y="Adj Close", title='iShares Global Green Bond ETF', labels={'y':'Adjusted Close'})
    return graph


# %%
# ### Drop of GDP
# Importing the dataset with GDP Drop data and with created OECD Regions
df1 = pd.read_excel('data\Economic_Impact\GDP\C_Percentage change in regional GDP.xlsx')
df2 = pd.read_excel('data\Economic_Impact\GDP\OECD Region.xlsx')
df1 = pd.melt(df1, id_vars=['Date'],value_vars=['OECD Europe', 'OECD Pacific', 'OECD America', 'Latin America',
       'World', 'Rest of Europe and Asia', 'Middle East and North Africa',
       'South and South-East Asia', 'Sub-Saharan Africa'])

df3=  pd.merge(df1, df2, on="variable")

#Map measures in percentage, so multiply with 100
df3['value']=df3['value']*100

# PLot
def get_dropGDP():
    graph  = px.bar(df1, 
            x='Date', y="value", color="variable", title='Percentage change in regional GDP due to selected climate change impacts', labels={'x':'Fund Type', 'y':'Pledge (USD mn)'})
    return graph
def get_dropGDP_W():
        fig = px.choropleth(df3, locations="CODE",
                    color="value", # lifeExp is a column of gapminder
                    hover_name="variable", # column to add to hover information
                    color_continuous_scale='Inferno',
                    animation_frame='Date',
                    color_continuous_midpoint = -0.9,
                    range_color=[-4,0])

        fig.update_layout(margin=dict(l=20,r=0,b=0,t=70,pad=0),paper_bgcolor="white",height= 700,title_text = 'Percentage change in regional GDP due to selected climate change impacts',font_size=18)
        
        return fig

# Variable time span : 2010-2060
# Data published by : OECD
# Link : https://www.oecd.org/statistics/climate-change-consequences-of-inaction.htm

#######################################################################################################################################################################################

# %%
# ### Economic damage caused by weather and climate-related extreme events in Europe (1980-2019)
# Importing the dataset
df_eea = pd.read_csv('data/Economic_Impact/EU_DMG/natural-disasters-events-3.csv', sep=',')
# PLot
def get_dmgEU():
        fig = go.Figure()
        fig.add_trace(go.Bar(
        x=df_eea['Year'],
        #y=df_eea['Type']=='Geophysical events',
        y=df_eea.loc[df_eea['Type'] == 'Geophysical events']['Value'],
        name='Geophysical events',
        marker_color='rgba(122, 166, 78)'
        ))
        fig.add_trace(go.Bar(
        x=df_eea['Year'],
        y=df_eea.loc[df_eea['Type'] == 'Climatological event']['Value'],
        name='Climatological event',
        marker_color='rgba(255, 200, 72)'
        ))
        fig.add_trace(go.Bar(
        x=df_eea['Year'],
        y=df_eea.loc[df_eea['Type'] == 'Hydrological event']['Value'],
        name='Hydrological event',
        marker_color='rgba(35, 132, 217)'
        ))
        fig_trend= (px.scatter( x=df_eea['Year'], y=df_eea['Value'], trendline="ols", labels={'x':'Year', 'y':'Regression Value'}, title='Trend of economic damage caused by weather <br>and climate-related extreme events in Europe '))

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
