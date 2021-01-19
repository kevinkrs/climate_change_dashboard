# -*- coding: utf-8 -*-
# %%
# libraries
try:
    import plotly.express   as px
    import pandas              as pd
except Exception as e:
    print("Failed to load libraries :\n" + str(e))



# %%
# ### Funding by type
# Importing the dataset
dataset = pd.read_excel('data/Governmental_efforts/data/Fund_Status.xlsx')
dataset.columns = ['Fund','Fund Type', 'Fund Focus', 'Pledge (USD mn)', 'Deposit (USD mn)', 'Approval (USD mn)', 'Disbursement (USD mn)', 'Number of projects approved', 'Date reported', 'Date collected']
dataset['Date reported']=pd.to_datetime(dataset['Date reported'],format="%m%Y")

# PLot
def get_fundingGraph():
    graph  = px.bar(dataset, 
            x='Fund Type', y="Pledge (USD mn)", title='Funding', labels={'x':'Fund Type', 'y':'Pledge (USD mn)'})
    return graph


# Variable time span : -
# Data published by : Climate Funds Update - Heinrich Böll Stiftung
# Link : https://climatefundsupdate.org/data-dashboard/#1541245664232-8e27b692-05c8


# %%
# ### Money pledged to spend on climate funds by countries
# Importing the dataset
dataset_pledges = pd.read_excel('data/Governmental_efforts/data/Governmental_efforts_climate funding_Pledges.xlsx')
dataset_pledges.columns = ['Fund','Fund Type', 'Fund Focus', 'Contributor', 'Country', 'Country Income Level','Region', 'Pledged (USD million current)', 'Deposited (USD million current)','test','test1']

# PLot
# PLot
def get_pledgedGraph():
    graph  = px.bar(dataset_pledges.nlargest(10, 'Pledged (USD million current)'), 
            x='Country', y="Pledged (USD million current)", title='Money pledged to give to climate funds by countries', labels={'x':'Country', 'y':'Pledged (USD million current)'})
    return graph

# Variable time span : -
# Data published by : Climate Funds Update - Heinrich Böll Stiftung
# Link : https://climatefundsupdate.org/data-dashboard/#1541245664232-8e27b692-05c8


'''def get_world_map():
        #avg = df1['log_value'].mean()
        fig = px.choropleth(df1, locations="CODE",
                    color="log_value", # lifeExp is a column of gapminder
                    hover_name="Country", # column to add to hover information
                    color_continuous_scale='tempo',
                    labels = {'log_value' : 'Patent count (log)', 'CODE' : 'Code'},
                    #hover_data = {'log_value' : False, 'Value' : 'Value' },
                   # scope = "",
                    animation_frame='Year',)

        fig.update_layout(margin=dict(l=20,r=0,b=0,t=70,pad=0),height= 700,title_text = 'Patents on technology filed to EPO',font_size=18)
        return fig'''

# %%
# ### Funding by type
# Importing the dataset
df_nzc = pd.read_csv('data\Governmental_efforts\ClimateWatch\net_zero_content.csv', sep=',')
df3_gcr = pd.read_excel('data/Economic_Impact/GDP/OECD Region.xlsx')   #Datasheet with OECD Regions, Countries and country Codes

df_nzc=  pd.merge(df_nzc, df3_gcr, on="Country")

# PLot
#Worldmap Net Zero Target Tracker
def get_NetZeroTargetWM():
        fig_nzc = px.choropleth(df_nzc, locations="CODE",
                    #color="Losses per unit GDP in % 1999-2018 (Rank)",
                    color='Indicator name',
                    #hover_name="Country ", # column to add to hover information
                    color_continuous_scale=px.colors.sequential .Greens[::-1],
                    #color_continuous_midpoint = -0.9,
                    )
        fig_nzc.update_layout(margin=dict(l=20,r=0,b=0,t=70,pad=0),paper_bgcolor="white",height= 700,title_text = 'Net-Zero Tracker',font_size=18)

        return fig_nzc


# Variable time span : -
# Data published by : Climate Watch
# Link : https://www.climatewatchdata.org/data-explorer/net-zero-content?net-zero-content-categories=&net-zero-content-countries=All%20Selected&net-zero-content-indicators=nz_status&page=1
