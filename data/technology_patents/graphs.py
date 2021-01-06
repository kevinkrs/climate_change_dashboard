import plotly.express as px
import pandas as pd
import numpy as np

df1 = pd.read_excel('data/technology_patents/files/epo_total_unity.xlsx')
df2 = pd.read_excel('data/technology_patents/files/epo_env_unity.xlsx')

df3 = pd.read_excel('data/technology_patents/files/uspto_total_unity.xlsx')
df4 = pd.read_excel('data/technology_patents/files/uspto_env_unity.xlsx')

df5 = pd.read_excel('data/technology_patents/files/pct_total_unity.xlsx')
df6 = pd.read_excel('data/technology_patents/files/pct_env_unity.xlsx')

#df7 = pd.merge(df1, df3, df5, on = "Country")

#print(df7.head())

def get_world_graph_epo_total():
    graph  = px.line(df1, 
            x='Year', y="Value", color="Country", title='Growth Patents Worldwide ', labels={'x':'Time', 'y':'Patents'})
    return graph

def get_world_graph_epo_env():
    fig = px.scatter(df1, x="Year", y="Value", color="Country",
                 size='Value', hover_data=['Value'])

    return fig


def get_world_graph_uspto_total():
    graph  = px.line(df1, 
            x='Year', y="Value", color="Country", title='Growth Patents Worldwide ', labels={'x':'Time', 'y':'Patents'})
    return graph

def get_world_graph_uspto_env():
    fig = px.scatter(df1, x="Year", y="Value", color="Country",
                 size='Value', hover_data=['Value'])

    return fig


def get_world_graph_pct_total():
    graph  = px.line(df1, 
            x='Year', y="Value", color="Country", title='Growth Patents Worldwide ', labels={'x':'Time', 'y':'Patents'})
    return graph

def get_world_graph_pct_env():
    fig = px.scatter(df1, x="Year", y="Value", color="Country",
                 size='Value', hover_data=['Value'])

    return fig
