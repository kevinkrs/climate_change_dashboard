# TODO Histogram with total patents vs. environmental 
import plotly.express as px
import pandas as pd


df1 = pd.read_excel('data/technology_patents/files/epo_comparision.xlsx')
df2 = pd.read_excel('data/technology_patents/files/uspto_comparision.xlsx')
df3 = pd.read_excel('data/technology_patents/files/pct_comparision.xlsx')

print(df1.head())

def get_hist_patents():
    return [get_epo_comp(), get_uspto_comp(), get_pct_comp()]


def get_epo_comp():
    fig = px.histogram(df1, x = 'Year' , y = 'Value', color = 'Name', hover_name = 'Year', hover_data={'Value' : 'Patent count'}, barmode = 'group', nbins = 18,
                        color_discrete_map={'Environmental related' : '#24B33F', 'Total' : '#3321BB'}, title = "Worldwide patent count vs. environmental related technologiy patents")
   

    return fig


def get_uspto_comp():
    fig = px.histogram(df2, x = 'Year' , y = 'Value', color = 'Name', hover_name = 'Year', hover_data={'Value' : 'Patents'}, barmode = 'group', nbins = 20,
                        color_discrete_map={'Environmental related' : '#24B33F', 'Total' : '#3321BB'}, title = "Worldwide patent count vs. environmental related technologiy patents")
    

    return fig



def get_pct_comp():
    fig = px.histogram(df3, x = 'Year' , y = 'Value', color = 'Name', hover_name = 'Year', hover_data={'Value' : 'Patents'}, barmode = 'group', nbins = 20,
                        color_discrete_map={'Environmental related' : '#24B33F', 'Total' : '#3321BB'}, title = "Worldwide patent count vs. environmental related technologiy patents")
    
    
    return fig

