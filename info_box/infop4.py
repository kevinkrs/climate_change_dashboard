import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

markdown_text1 = '''

All countries are handled seperately or in a conglomerate of regions classified by the OECD.
The OECD regions consist of:

- OECD Europe
- OECD America
- OECD Pacific
- Latin America
- Rest of Europe and Asia 
- Middle East and North Africa
- South and South-East-Asia
- Sub-Saharan Africa
'''

markdown_text2 = '''For the historic and future data and the trend calculation a variety of assumptions and modelling have been made:
    	
- Impact of the climate change on individual GDPs : ENV-Linkages model by OECD 
- The Climate Risk Index is calculated by German Watch with the worldwide data collection and analysis provided by Munich Re’s NatCatSERVICE which is the world’s leading re-insurance
    company. The main indicators are : weather-related events – storms, floods as well as temperature extremes and mass movements (heat and cold waves etc.)

- The trend calculation have been calculated trough a OLS(Ordinary Least Squares) Regression by using the historic and future data.
'''

markdown_text3 = '''**GDP and EUR:**

The gross domestic product is a reliable measure to determine the development of a country's economy and to classify the damage caused. Sometimes absolute numbers like Euros can also be used to reflect a scenario
'''

markdown_text4 = '''The Global Climate Risk Index indicates a level of exposure and vulnerability to extreme weather events, which countries should understand as warnings in order to be prepared for more frequent and/or more severe events in the future.

CRI score goes from 0 until 120. The lower the score is, the higher the vulnerability and exposure to extreme weather events is.
'''

markdown_text5 = '''Climate related ecents are parted into 4 groups.

- Meterological events
- Hydrological events
- Climatological events
- Geophysical events
'''

def get_infoBox4(pathname):
    infobox =   dbc.Row([
                    html.P("Information Box",className="lead", style={'width':'100%'}),

                    dbc.Button("Countries", id="patent_open1", style= {'margin' : '10px', 'width' : '95%'}),
                    dbc.Modal(
                        [
                            dbc.ModalHeader("Countries"),
                            dcc.Markdown(children = markdown_text1, style = {'padding' : '15px'}),
                            dbc.ModalFooter(
                                dbc.Button("Close", id="patent_close1", className="ml-auto")
                    )],  id="patent_modal1",
                        scrollable = True),

                    dbc.Button("Data Models", id="patent_open2", style= {'margin' : '10px', 'width' : '95%'}),
                    dbc.Modal(
                        [
                            dbc.ModalHeader("Prediction Models"),
                            dcc.Markdown(children = markdown_text2, style = {'padding' : '15px'}),
                            dbc.ModalFooter(
                            dbc.Button("Close", id="patent_close2", className="ml-auto")
                    )], id="patent_modal2",
                        scrollable = True),

                    dbc.Button("Reference Data", id="patent_open3", style= {'margin' : '10px', 'width' : '95%'}),
                    dbc.Modal(
                        [
                            dbc.ModalHeader("Reference Data"),
                            dcc.Markdown(children = markdown_text3, style = {'padding' : '15px'}),
                            dbc.ModalFooter(
                                dbc.Button("Close", id="patent_close3", className="ml-auto", style= {'margin' : '10px'})
                            )], id="patent_modal3",
                        scrollable = True),

                    dbc.Button("Climate Risk Index", id="patent_open4", style= {'margin' : '10px', 'width' : '95%'}),
                    dbc.Modal(
                        [
                            dbc.ModalHeader("Climate Risk Index"),
                            dcc.Markdown(children = markdown_text4, style = {'padding' : '15px'}),
                            dbc.ModalFooter(
                                dbc.Button("Close", id="patent_close4", className="ml-auto")
                            )], id="patent_modal4",
                        scrollable = True),

                    dbc.Button("Climate related events", id="patent_open5", style= {'margin' : '10px', 'width' : '95%'}),
                    dbc.Modal(
                        [
                            dbc.ModalHeader("Climate related events"),
                            dcc.Markdown(children = markdown_text5, style = {'padding' : '15px'}),
                            dbc.ModalFooter(
                                dbc.Button("Close", id="patent_close5", className="ml-auto")
                            )], id="patent_modal5",
                            scrollable = True),
                ],style={'margin':0},)

    if pathname == "/page4":
        return infobox

                        

