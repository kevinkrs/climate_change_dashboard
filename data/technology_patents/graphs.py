import plotly.express as px
import pandas as pd
import pycountry

df1 = pd.read_csv('data/technology_patents/files/epo_total.csv', sep = ";")

df1.head()
def alpha3code(column): 
    CODE = []
    for country in column:
        try: 
            code = pycountry.countries.get(name=country).alpha_3
            CODE.append(code)
        except: 
            CODE.append('None')
    return CODE

df1['CODE'] = alpha3code(df1.Country)

def get_map():
        fig = px.choropleth(df1, locations="CODE",
                    color="Value", # lifeExp is a column of gapminder
                    hover_name="Country", # column to add to hover information
                    color_continuous_scale='Inferno',
                    animation_frame='Year',
                    color_continuous_midpoint = -0.009)

        fig.update_layout(margin=dict(l=20,r=0,b=0,t=70,pad=0),paper_bgcolor="white",height= 700,title_text = 'Patents in technology domains',font_size=18)
        return fig