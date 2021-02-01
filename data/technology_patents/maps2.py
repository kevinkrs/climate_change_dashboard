try:
        from lib.lib import *
except Exception as e:
    print("Failed to load libraries :\n" + str(e))


def get_maps_patent_relative(): 
    return [get_world_map_epo(), get_world_map_uspto(), get_world_map_pct()]

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
        fig = px.choropleth_mapbox(df1, geojson = geojson, locations="CODE",
                mapbox_style="carto-positron",
                featureidkey="properties.iso_a3",
                color="Relative", # lifeExp is a column of gapminder
                hover_name="Country", # column to add to hover information
                color_continuous_scale='Greens',
                labels = {'Relative' : 'Relativ'},
                zoom=1,
                opacity=0.8,
                center = {"lat": 50.958427, "lon": 10.436234},
                #hover_data = {'log_value' : False, 'Value' : 'Value' },
                # scope = "",
                animation_frame='Year',
                range_color = [0,1])

        fig.update_layout(margin=dict(l=20,r=0,b=0,t=70,pad=0),height= 700,title_text = 'EPO: ENV-TECH relative to Total Patents',font_size=18, paper_bgcolor='#f8f7f7')
        return fig


def get_world_map_uspto():
        #avg = df1['log_value'].mean()
        fig = px.choropleth_mapbox(df2, geojson = geojson, locations="CODE",
                mapbox_style="carto-positron",
                featureidkey="properties.iso_a3",
                color="Relative", # lifeExp is a column of gapminder
                hover_name="Country", # column to add to hover information
                color_continuous_scale='Greens',
                labels = {'Relative' : 'Relativ'},
                zoom=1,
                opacity=0.8,
                center = {"lat": 50.958427, "lon": 10.436234},
                    #hover_data = {'log_value' : False, 'Value' : 'Value' },
                   # scope = "",
                    animation_frame='Year',)

        fig.update_layout(margin=dict(l=20,r=0,b=0,t=70,pad=0),height= 700,title_text = 'USPTO: ENV-TECH relative to Total Patents',font_size=18)
        return fig


def get_world_map_pct():
        #avg = df1['log_value'].mean()
        fig = px.choropleth_mapbox(df3, geojson = geojson, locations="CODE",
                mapbox_style="carto-positron",
                featureidkey="properties.iso_a3",
                color="Relative", # lifeExp is a column of gapminder
                hover_name="Country", # column to add to hover information
                color_continuous_scale='Greens',
                labels = {'Relative' : 'Relativ'},
                zoom=1,
                opacity=0.8,
                center = {"lat": 50.958427, "lon": 10.436234},
                    #hover_data = {'log_value' : False, 'Value' : 'Value' },
                   # scope = "",
                    animation_frame='Year',)

        fig.update_layout(margin=dict(l=20,r=0,b=0,t=70,pad=0),height= 700,title_text = 'PCT: ENV-TECH relative to Total Patents',font_size=18)
        return fig