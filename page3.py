
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import json
import geojson
from data.technology_patents.maps import *
from data.technology_patents.graphs import *
#==> import external method from .py file from folder /data,  wwhich is plotting the graph

# Testing

#df1['iso_a3']  = df1['iso_a3'].astype(str)


#with open('data/Worldmap shapes/custom.geo.json') as f: 
 #   gj = json.load(f)

# print(gj["features"][5])


def p3_updateLayout():
    #Defining Spaces ==> Insert your plot into the spaces
    leftSpace = html.Div([
            dbc.Col([
                dbc.Row([
                html.H4('Options'),
                dcc.Dropdown(id = 'dropdown_po', 
                options =[{'label' : 'EPO', 'value' : '0' },
                          {'label' : 'USPTO', 'value' : '1'},
                          {'label' : 'PCT', 'value' : '2'}], 
                          value = '0',
                          placeholder = 'Select patent office', style = {'margin-bottom' : 10, 'margin-top' : 10, 'width': '100%'}),
                dcc.Dropdown(id ='dropdown_number',
                options =[{'label' : 'Environmental-related', 'value' : '0'},
                        {'label' : 'Total', 'value' : '1' },],
                          value = '0',
                          placeholder = 'Select technology domain', style ={ 'width': '100%'})]),
                dbc.Row([
                    html.H4('Information Box', style = { 'margin' : '10px'}), 

                    dbc.Button("Countries", id="patent_open1", style= {'margin' : '10px', 'width' : '95%'}),
                    dbc.Modal(
                        [
                            dbc.ModalHeader("Countries"),
                            dcc.Markdown(children = markdown_text1, style = {'padding' : '15px'}),
                            dbc.ModalFooter(
                                dbc.Button("Close", id="patent_close1", className="ml-auto")
                    )],  id="patent_modal1",
                        scrollable = True),

                    dbc.Button("Patents", id="patent_open2", style= {'margin' : '10px', 'width' : '95%'}),
                    dbc.Modal(
                        [
                            dbc.ModalHeader("Patents"),
                            dcc.Markdown(children = markdown_text2, style = {'padding' : '15px'}),
                            dbc.ModalFooter(
                            dbc.Button("Close", id="patent_close2", className="ml-auto")
                    )], id="patent_modal2",
                        scrollable = True),

                    dbc.Button("Reference Country", id="patent_open3", style= {'margin' : '10px', 'width' : '95%'}),
                    dbc.Modal(
                        [
                            dbc.ModalHeader("Reference Country"),
                            dcc.Markdown(children = markdown_text3, style = {'padding' : '15px'}),
                            dbc.ModalFooter(
                                dbc.Button("Close", id="patent_close3", className="ml-auto", style= {'margin' : '10px'})
                            )], id="patent_modal3",
                        scrollable = True),

                    dbc.Button("Reference Date", id="patent_open4", style= {'margin' : '10px', 'width' : '95%'}),
                    dbc.Modal(
                        [
                            dbc.ModalHeader("Reference Date"),
                            dcc.Markdown(children = markdown_text4, style = {'padding' : '15px'}),
                            dbc.ModalFooter(
                                dbc.Button("Close", id="patent_close4", className="ml-auto")
                            )], id="patent_modal4",
                        scrollable = True),

                    dbc.Button("Technology domains and IPC", id="patent_open5", style= {'margin' : '10px', 'width' : '95%'}),
                    dbc.Modal(
                        [
                            dbc.ModalHeader("Technology domains and IPC (International Patent Clasification"),
                            dcc.Markdown(children = markdown_text5, style = {'padding' : '15px'}),
                            dbc.ModalFooter(
                                dbc.Button("Close", id="patent_close5", className="ml-auto")
                            )], id="patent_modal5",
                            scrollable = True),
            ],
            style = {'background-color' : 'lightgrey', 'padding' : '30px', 'margin-top' : '30px'})])],

                style={'width': '100%', 'height': 500, 'margin-left' : '15px', 'margin-top' : '15px',  
                        'display' : 'flex', 'flex-direction' : 'column', 'align-items': 'center'})
        #Example : leftSpace = html.Div(Call_method_of_plotted_graph)
    #midSpace = html.Div(dcc.Graph(figure = get_world_map_epo_total())) 
    midSpace = html.Div(dcc.Graph(id = 'worldmap_patents')) 
    #rightSpace = html.Div("Rechter Space")

    bot_leftSpace = html.Div(dcc.Graph(id = 'scatter_patents_env'))
    #bot_midSpace = html.Div("Mid Space")
    bot_rightSpace = html.Div(dcc.Graph(id = 'histogram_total_env'))

    #In "content" the grid gets initialised and styled via HTML and CSS ==> If your graph doesent get displayed the right way you can adjust the styling or text Konstantin
    content = html.Div([
        dbc.Row( [
            dbc.Col(
            [leftSpace, html.Div([        
            ])], className='col-2', style ={'padding':20}),

            dbc.Col(
            [midSpace, html.Div(
            )], className='col-10',style ={'padding':20}),]),

        dbc.Row( [
            dbc.Col(
            bot_leftSpace, className='col-6', style ={'padding':20}),
            dbc.Col(
            [bot_rightSpace, html.Div(
            )], className='col-6',style ={'padding':20}),]
            )],
            style={ 'width' : 'auto',  'overflow' : 'hidden',},) # other nice color #7ED6F0

    return content



markdown_text1 = '''

More than 100 countries worldwide are covered. Geographical aggregates are provided for the EU-28, the OECD total, and the World total.
Fractional counts applied for patents with multiple inventors/applicants:
When a patent was invented by several inventors from different countries, the respective contributions of each country is taken into account. This is done in order to eliminate multiple counting of such patents.
For example, a patent co-invented by 1 French, 1 American and 2 German residents will be counted as:
1/4th of a patent for France;
1/4th for the USA;
and ½ patent for Germany.


'''

markdown_text2 = '''The dataset provides data on patents counts by technology for:
    	
- Patent **applications** to the European Patent Office (EPO)
- Patent applications to the US Patent and Trademark Office (USPTO)
- Patents filed under the Patent Co-operation Treaty (PCT), at international phase, that designate the EPO

Series are derived from EPO's Worldwide Patent Statistical database (PATSTAT Global, Spring 2020). USPTO and Triadic patent families are mainly derived from PATSTAT biblio, while EPO and PCT patent counts are based on PATSTAT's EPO Register (Spring 2020).
'''

markdown_text3 = '''**Inventors’ country:**

Counting patents according to the inventor’s country of residence is the most relevant for measuring the technological innovativeness of researchers and laboratories located in a given country.
'''

markdown_text4 = '''An inventor seeking protection files a first application (the priority) generally in his/her country of residence. Then, he/she has a 12-months legal delay for applying or not for protection of the original invention in other countries (application). The application is published at least 18 months after the priority date. And finally, it can take three to ten years for a patent to be granted.

- *Priority date*: it corresponds to the first filing worldwide and therefore closest to the invention date.
To measure inventive activity, patent should be counted according to the priority date (in the case of patent families, the priority date corresponds to the earliest priority among the set of patents)
- *Application (or filing) date*: It occurs generally 12 month after a foreign priority. Using the application date introduces a bias owing to a one-year lag between residents and foreigners.

Note that figures for the later years may be decreasing because of legal delays for publishing patent information. Therefore, EPO applications are complete up to 2016 by priority date, and 2018 by application date. EPO grants are deemed complete up to 2015 by priority date, 2017 by application date, and 2019 by date of grant. USPTO application data are almost complete up to 2016 by priority date, and 2017 by application date. USPTO grant data are almost complete up to 2016 by priority date, 2017 by application date, and 2019 by date of grant. PCT data are complete up to 2017 by priority date, and 2018 by application date.
'''

markdown_text5 = '''- Total count of patents: Provides the count of all patents by country
- Environmental-related technologies

Patent counts are also presented according to the classes of the International Patent Classification (IPC) - 1 and 3 digits. Counts are based on the list of IPC codes that are given in each patent document, and use fractional counts.
'''