import plotly.express as px
import pandas as pd


df1 = pd.read_excel('data/technology_patents/files/epo_total_unity.xlsx')
df2 = pd.read_excel('data/technology_patents/files/epo_env_unity.xlsx')

df3 = pd.read_excel('data/technology_patents/files/uspto_total_unity.xlsx')
df4 = pd.read_excel('data/technology_patents/files/uspto_env_unity.xlsx')

df5 = pd.read_excel('data/technology_patents/files/pct_total_unity.xlsx')
df6 = pd.read_excel('data/technology_patents/files/pct_env_unity.xlsx')



def get_graphs_patent(): 

    return [get_world_graph_epo_env(), get_world_graph_uspto_env(), get_world_graph_pct_env(),get_world_graph_epo_total(), get_world_graph_uspto_total(), get_world_graph_pct_total()]


# Environmental-related patents
def get_world_graph_epo_env():
    fig = px.line(df2, x="Year", y="Value", color="Country",
                  hover_data=['Value'], color_discrete_map= {'World' : '#3321BB', 'OECD' : '#B62DD5', 'BRIC' : '#28CDD0', 'European Union' : '#DBD831'}, 
                  title = 'Distribution of Patents regarding world oragnisations')
   

    return fig

def get_world_graph_uspto_env():
    fig = px.line(df4, x="Year", y="Value", color="Country", color_discrete_map= {'World' : '#3321BB', 'OECD' : '#B62DD5', 'BRIC' : '#28CDD0', 'European Union' : '#DBD831'},
                  hover_data=['Value'],title = 'Distribution of Patents regarding world oragnisations')
    

    return fig

def get_world_graph_pct_env():
    fig = px.line(df6, x="Year", y="Value", color="Country", color_discrete_map= {'World' : '#3321BB', 'OECD' : '#B62DD5', 'BRIC' : '#28CDD0', 'European Union' : '#DBD831'},
                  hover_data=['Value'], title = 'Distribution of Patents regarding world oragnisations')
    
    
    return fig


#total patents

def get_world_graph_epo_total():
    fig = px.line(df1, x="Year", y="Value", color="Country",
                  hover_data=['Value'], color_discrete_map= {'World' : '#3321BB', 'OECD' : '#B62DD5', 'BRIC' : '#28CDD0', 'European Union' : '#DBD831'}, 
                  title = 'Distribution of Patents regarding world oragnisations')
    

    return fig

def get_world_graph_uspto_total():
    fig = px.line(df3, x="Year", y="Value", color="Country", color_discrete_map= {'World' : '#3321BB', 'OECD' : '#B62DD5', 'BRIC' : '#28CDD0', 'European Union' : '#DBD831'},
                  hover_data=['Value'],title = 'Distribution of Patents regarding world oragnisations')
   

    return fig

def get_world_graph_pct_total():
    fig = px.line(df5, x="Year", y="Value", color="Country", color_discrete_map= {'World' : '#3321BB', 'OECD' : '#B62DD5', 'BRIC' : '#28CDD0', 'European Union' : '#DBD831'},
                  hover_data=['Value'], title = 'Distribution of Patents regarding world oragnisations')
    
    
    return fig