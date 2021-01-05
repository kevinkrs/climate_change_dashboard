# %%
import plotly.express as px
import pandas as pd

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
# Importing the dataset
df1 = pd.read_excel('data/Economic_Impact/GDP/C_Percentage change in regional GDP.xlsx')
df2 = pd.read_excel('data/Economic_Impact/GDP/OECD Region.xlsx')
df1 = pd.melt(df1, id_vars=['Date'],value_vars=['OECD Europe', 'OECD Pacific', 'OECD America', 'Latin America',
       'World', 'Rest of Europe and Asia', 'Middle East and North Africa',
       'South and South-East Asia', 'Sub-Saharan Africa'])

df3=  pd.merge(df1, df2, on="variable")

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
                    color_continuous_midpoint = -0.009)

        fig.update_layout(margin=dict(l=20,r=0,b=0,t=70,pad=0),paper_bgcolor="white",height= 700,title_text = 'Percentage change in regional GDP due to selected climate change impacts',font_size=18)
        return fig


# Variable time span : -
# Data published by : OECD
# Link : https://www.oecd.org/statistics/climate-change-consequences-of-inaction.htm
# %%
