try:
        import plotly.express as px
        import pandas as pd
        import numpy as np
        import pycountry
        import pandas              as pd
        import json
except Exception as e:
    print("Failed to load libraries :\n" + str(e))


def get_maps_patent():
        return [get_world_map_epo_env(),get_world_map_uspto_env(), get_world_map_pct_env(),get_world_map_epo_total(),get_world_map_uspto_total(), get_world_map_pct_total()]

df1 = pd.read_excel('data/technology_patents/files/epo_total_c.xlsx')




def alpha3code(country):
    try:
        result = pycountry.countries.search_fuzzy(country)
    except Exception:
        return np.nan
    else:
        return result[0].alpha_3    

iso_map = {country: alpha3code(country) for country in df1["Country"].unique()}

df1["CODE"] = df1["Country"].map(iso_map)
df1['log_value'] = np.log(df1['Value'])

with open('data/Worldmap shapes/custom.geo.json') as f:
  geojson = json.load(f)

def get_world_map_epo_total():
        #avg = df1['log_value'].mean()
        fig = px.choropleth_mapbox(df1, geojson = geojson, locations="CODE",
                mapbox_style="carto-positron",
                featureidkey="properties.sov_a3",
                color="log_value", # lifeExp is a column of gapminder
                hover_name="Country", # column to add to hover information
                color_continuous_scale='tempo',
                labels = {'log_value' : 'Patent count (log)', 'CODE' : 'Code'},
                zoom=1,
                opacity=0.8,
                center = {"lat": 50.958427, "lon": 10.436234},
                #hover_data = {'log_value' : False, 'Value' : 'Value' },
                # scope = "",
                #animation_frame='Year',
                range_color = [-2,11])

        fig.update_layout(margin=dict(l=20,r=0,b=0,t=70,pad=0),height= 700,title_text = 'Patents on technology filed to EPO',font_size=18)
        return fig


# Map epo_env
df2 = pd.read_excel('data/technology_patents/files/epo_env_c.xlsx')

df2["CODE"] = df2["Country"].map(iso_map)
df2['log_value'] = np.log(df2['Value'])
#print(df2.head())

def get_world_map_epo_env():
        #avg = df1['log_value'].mean()
        fig = px.choropleth(df2, locations="CODE",
                    color="log_value", # lifeExp is a column of gapminder
                    hover_name="Country", # column to add to hover information
                    color_continuous_scale='Greens',
                    labels = {'log_value' : 'Patent count (log)', 'CODE' : 'Code'},
                    #hover_data = {'log_value' : False, 'Value' : 'Value' },
                   # scope = "",
                    animation_frame='Year',
                    range_color = [-2,8])

        fig.update_layout(margin=dict(l=20,r=0,b=0,t=70,pad=0),height= 700,title_text = 'Patents on environmental-related technologies filed to EPO',font_size=18)
        return fig



df3 = pd.read_excel('data/technology_patents/files/uspto_env_c.xlsx')

df3["CODE"] = df3["Country"].map(iso_map)
df3['log_value'] = np.log(df3['Value'])
##print(df3.head())

def get_world_map_uspto_env():
        #avg = df1['log_value'].mean()
        fig = px.choropleth(df3, locations="CODE",
                    color="log_value", # lifeExp is a column of gapminder
                    hover_name="Country", # column to add to hover information
                    color_continuous_scale='Greens',
                    labels = {'log_value' : 'Patent count (log)', 'CODE' : 'Code'},
                    #hover_data = {'log_value' : False, 'Value' : 'Value' },
                   # scope = "",
                    animation_frame='Year',
                    range_color = [-2,8])

        fig.update_layout(margin=dict(l=20,r=0,b=0,t=70,pad=0),height= 700,title_text = 'Patents on environmental-related technologies filed to USPTO',font_size=18)
        return fig



df4= pd.read_excel('data/technology_patents/files/uspto_total_c.xlsx')

df4["CODE"] = df4["Country"].map(iso_map)
df4['log_value'] = np.log(df4['Value'])
#print(df4.head())

def get_world_map_uspto_total():
        #avg = df1['log_value'].mean()
        fig = px.choropleth(df4, locations="CODE",
                    color="log_value", # lifeExp is a column of gapminder
                    hover_name="Country", # column to add to hover information
                    color_continuous_scale='tempo',
                    labels = {'log_value' : 'Patent count (log)', 'CODE' : 'Code'},
                    #hover_data = {'log_value' : False, 'Value' : 'Value' },
                   # scope = "",
                    animation_frame='Year',
                    range_color = [-2,11])

        fig.update_layout(margin=dict(l=20,r=0,b=0,t=70,pad=0),height= 700,title_text = 'Patents on technology filed to USPTO',font_size=18)
        return fig


df5 = pd.read_excel('data/technology_patents/files/pct_env_c.xlsx')

df5["CODE"] = df5["Country"].map(iso_map)
df5['log_value'] = np.log(df5['Value'])
#print(df5.head())

def get_world_map_pct_env():
        #avg = df1['log_value'].mean()
        fig = px.choropleth(df5, locations="CODE",
                    color="log_value", # lifeExp is a column of gapminder
                    hover_name="Country", # column to add to hover information
                    color_continuous_scale='Greens',
                    labels = {'log_value' : 'Patent count (log)', 'CODE' : 'Code'},
                    #hover_data = {'log_value' : False, 'Value' : 'Value' },
                   # scope = "",
                    animation_frame='Year',
                    range_color = [-2,8])

        fig.update_layout(margin=dict(l=20,r=0,b=0,t=70,pad=0),height= 700,title_text = 'Patents on environmental-related technologies filed to PCT',font_size=18)
        return fig


df6 = pd.read_excel('data/technology_patents/files/pct_total_c.xlsx')

df6["CODE"] = df6["Country"].map(iso_map)
df6['log_value'] = np.log(df6['Value'])
#print(df6.head())

def get_world_map_pct_total():
        #avg = df1['log_value'].mean()
        fig = px.choropleth(df6, locations="CODE",
                    color="log_value", # lifeExp is a column of gapminder
                    hover_name="Country", # column to add to hover information
                    color_continuous_scale='tempo',
                    labels = {'log_value' : 'Patent count (log)', 'CODE' : 'Code'},
                    #hover_data = {'log_value' : False, 'Value' : 'Value' },
                   # scope = "",
                    animation_frame='Year',
                    range_color = [-2,11])

        fig.update_layout(margin=dict(l=20,r=0,b=0,t=70,pad=0),height= 700,title_text = 'Patents on technology filed to PCT',font_size=18)
        return fig
