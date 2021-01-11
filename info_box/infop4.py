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

def get_infoBox(pathname):
    infobox=    dbc.Row([
                    dbc.Row([html.I( className='fas fa-info', style={'padding-right':20}), html.A("Information Box")],className='infoHead'),

                    dbc.Button("Countries", id="patent_open1", style= {'margin' : '10px', 'width' : '95%'}),
                    dbc.Modal(
                        [
                            dbc.ModalHeader("Countries"),
                            dcc.Markdown(children = markdown_text1, style = {'padding' : '15px'}),
                            dbc.ModalFooter(
                                dbc.Button("Close", id="patent_close1", className="ml-auto")
                    )],  id="patent_modal1",
                        scrollable = True),

                    dbc.Button("Prediction Models", id="patent_open2", style= {'margin' : '10px', 'width' : '95%'}),
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

                    dbc.Button("Empty", id="patent_open4", style= {'margin' : '10px', 'width' : '95%'}),
                    dbc.Modal(
                        [
                            dbc.ModalHeader("Empty"),
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

                        

