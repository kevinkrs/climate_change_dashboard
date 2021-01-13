import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

markdown_text1 = '''

Our collective CO2 emissions can be expressed as a product of four factors and their relationship with each other : 
population size, economic growth, energy intensity and emissions per energy unit produced.
Here we focus on energy intensity and emissions per energy unit produced, because this factors explain how we can stop that.

On the graph we can see the evolution over time for the main economic actor
So we can see the high carbon energy production, and the part of the renewable energy in the total production.
The world map shows us the inequality of consequences with the numbers of deaths from air pollution, and the impact on ozone for each country. 

'''

markdown_text2 = '''

On these part, data come from OCDE data base, BP statistical review and Nasa Ozone since nineteen sixty-five to December twenty-nineteen.

'''




def get_infoBox1(pathname):
    infobox=    dbc.Row([
                    dbc.Row([html.I( className='fas fa-info', style={'padding-right':20}), html.A("Information Box")],className='infoHead'),

                    dbc.Button("Object", id="patent_open1", style= {'margin' : '10px', 'width' : '95%'}),
                    dbc.Modal(
                        [
                            dbc.ModalHeader("Object"),
                            dcc.Markdown(children = markdown_text1, style = {'padding' : '15px'}),
                            dbc.ModalFooter(
                            dbc.Button("Close", id="patent_close1", className="ml-auto")
                    )],  id="patent_modal1",
                        scrollable = True),

                    dbc.Button("Data Source", id="patent_open2", style= {'margin' : '10px', 'width' : '95%'}),
                    dbc.Modal(
                        [
                            dbc.ModalHeader("Data Source"),
                            dcc.Markdown(children = markdown_text2, style = {'padding' : '15px'}),
                            dbc.ModalFooter(
                            dbc.Button("Close", id="patent_close2", className="ml-auto")
                    )], id="patent_modal2",
                        scrollable = True),

                ],style={'margin':0},)
    if pathname == "/page1":
        return infobox

                        

