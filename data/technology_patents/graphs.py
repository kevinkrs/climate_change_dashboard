import plotly.express as px
import pandas as pd


df1 = pd.read_excel('data/technology_patents/files/epo_total_unity.xlsx')
df2 = pd.read_excel('data/technology_patents/files/epo_env_unity.xlsx')

df3 = pd.read_excel('data/technology_patents/files/uspto_total_unity.xlsx')
df4 = pd.read_excel('data/technology_patents/files/uspto_env_unity.xlsx')

df5 = pd.read_excel('data/technology_patents/files/pct_total_unity.xlsx')
df6 = pd.read_excel('data/technology_patents/files/pct_env_unity.xlsx')

df7 = pd.read_excel('data/technology_patents/epo_world_relative.xlsx')
df8 = pd.read_excel('data/technology_patents/uspto_world_relative.xlsx')
df9 = pd.read_excel('data/technology_patents/pct_world_relative.xlsx')


def get_graphs_patent_total(): 

    return [get_world_graph_epo_total(), get_world_graph_uspto_total(), get_world_graph_pct_total()]

def get_graphs_patent_relative():

    return [get_world_graph_epo_relative(), get_world_graph_uspto_relative(),get_world_graph_pct_relative()]

def get_graphs_patent_env():

    return [get_world_graph_epo_env(), get_world_graph_uspto_env(), get_world_graph_pct_env()]

# Environmental-related patents
def get_world_graph_epo_env():
    fig = px.line(df2, x="Year", y="Value", color="Country",
                  hover_data=['Value'], color_discrete_map= {'World' : '#3321BB', 'OECD' : '#B62DD5', 'BRIC' : '#28CDD0', 'European Union' : '#DBD831'}, 
                  title = 'Distribution of Patents regarding world organisations')
   

    return fig


def get_world_graph_uspto_env():
    fig = px.line(df4, x="Year", y="Value", color="Country", color_discrete_map= {'World' : '#3321BB', 'OECD' : '#B62DD5', 'BRIC' : '#28CDD0', 'European Union' : '#DBD831'},
                  hover_data=['Value'],title = 'Distribution of Patents regarding world organisations')
    

    return fig

def get_world_graph_pct_env():
    fig = px.line(df6, x="Year", y="Value", color="Country", color_discrete_map= {'World' : '#3321BB', 'OECD' : '#B62DD5', 'BRIC' : '#28CDD0', 'European Union' : '#DBD831'},
                  hover_data=['Value'], title = 'Distribution of Patents regarding world organisations')
    
    
    return fig


#total patents

def get_world_graph_epo_total():
    fig = px.line(df1, x="Year", y="Value", color="Country",
                  hover_data=['Value'], color_discrete_map= {'World' : '#3321BB', 'OECD' : '#B62DD5', 'BRIC' : '#28CDD0', 'European Union' : '#DBD831'}, 
                  title = 'Distribution of Patents regarding world organisations')
    

    return fig

def get_world_graph_uspto_total():
    fig = px.line(df3, x="Year", y="Value", color="Country", color_discrete_map= {'World' : '#3321BB', 'OECD' : '#B62DD5', 'BRIC' : '#28CDD0', 'European Union' : '#DBD831'},
                  hover_data=['Value'],title = 'Distribution of Patents regarding world organisations')
   

    return fig

def get_world_graph_pct_total():
    fig = px.line(df5, x="Year", y="Value", color="Country", color_discrete_map= {'World' : '#3321BB', 'OECD' : '#B62DD5', 'BRIC' : '#28CDD0', 'European Union' : '#DBD831'},
                  hover_data=['Value'], title = 'Distribution of Patents regarding world organisations')
    
    
    return fig


def get_world_graph_epo_relative():
    fig = px.line(df7, x="Year", y="Relative", color="Country", color_discrete_map= {'Worldwide' : '#24B33F'},
                  hover_data=['Relative'], title = 'Ratio between Worldwide Environmental-Related and Total applications ')
    
    
    return fig

def get_world_graph_uspto_relative():
    fig = px.line(df8, x="Year", y="Relative", color="Country", color_discrete_map= {'Worldwide' : '#24B33F'},
                  hover_data=['Relative'], title = 'Ratio between Worldwide Environmental-Related and Total applications')
    
    
    return fig

def get_world_graph_pct_relative():
    fig = px.line(df9, x="Year", y="Relative", color="Country", color_discrete_map= {'Worldwide' : '#24B33F'},
                  hover_data=['Relative'], title = 'Ratio between Worldwide Environmental-Related and Total applications')
    
    
    return fig