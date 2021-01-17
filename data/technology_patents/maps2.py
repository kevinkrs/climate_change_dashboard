import plotly.express as px
import pandas as pd
import numpy as np
import pycountry


#def get_maps_patent(): 
  #  return [get_world_map_epo(), get_world_map_uspto(), get_world_map_pct()]

df1 = pd.read_excel('data/technology_patents/epo_compared.xlsx')
df2 = pd.read_excel('data/technology_patents/uspto_compared.xlsx')
df3= pd.read_excel('data/technology_patents/pct_compared.xlsx')

def alpha3code(country):
    try:
        result = pycountry.countries.search_fuzzy(country)
    except Exception:
        return np.nan
    else:
        return result[0].alpha_3    

iso_map = {country: alpha3code(country) for country in df1["Country"].unique()}

df1["CODE"] = df1["Country"].map(iso_map)
df2["CODE"] = df2["Country"].map(iso_map)
df3["CODE"] = df3["Country"].map(iso_map)

def get_world_map_epo():
        #avg = df1['log_value'].mean()
        fig = px.choropleth(df1, locations="CODE",
                    color="Relative", # lifeExp is a column of gapminder
                    hover_name="Country", # column to add to hover information
                    color_continuous_scale='Greens',
                    labels = {'log_value' : 'Patent count (log)', 'CODE' : 'Code'},
                    #hover_data = {'log_value' : False, 'Value' : 'Value' },
                   # scope = "",
                    animation_frame='Year',)

        fig.update_layout(margin=dict(l=20,r=0,b=0,t=70,pad=0),height= 700,title_text = 'Environmental-technology patents filed to EPO',font_size=18)
        return fig


def get_world_map_uspto():
        #avg = df1['log_value'].mean()
        fig = px.choropleth(df2, locations="CODE",
                    color="Relative", # lifeExp is a column of gapminder
                    hover_name="Country", # column to add to hover information
                    color_continuous_scale='Greens',
                    labels = {'log_value' : 'Patent count (log)', 'CODE' : 'Code'},
                    #hover_data = {'log_value' : False, 'Value' : 'Value' },
                   # scope = "",
                    animation_frame='Year',)

        fig.update_layout(margin=dict(l=20,r=0,b=0,t=70,pad=0),height= 700,title_text = 'Environmental-technology patents filed to USPTO',font_size=18)
        return fig


def get_world_map_pct():
        #avg = df1['log_value'].mean()
        fig = px.choropleth(df1, locations="CODE",
                    color="Relative", # lifeExp is a column of gapminder
                    hover_name="Country", # column to add to hover information
                    color_continuous_scale='Greens',
                    labels = {'log_value' : 'Patent count (log)', 'CODE' : 'Code'},
                    #hover_data = {'log_value' : False, 'Value' : 'Value' },
                   # scope = "",
                    animation_frame='Year',)

        fig.update_layout(margin=dict(l=20,r=0,b=0,t=70,pad=0),height= 700,title_text = 'Environmental-technology patents filed to PCT',font_size=18)
        return fig