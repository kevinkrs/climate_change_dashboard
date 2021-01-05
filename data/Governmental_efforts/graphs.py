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
dataset = pd.read_excel('data\Governmental_efforts\data/Fund_Status.xlsx')
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
dataset_pledges = pd.read_excel('data\Governmental_efforts\data\Governmental_efforts_climate funding_Pledges.xlsx')
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
