import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

markdown_text1 = '''

Here is the first page of this dashboard. The objective is to give an overview of the situation and thanks to historical data also understand the trajectory.

Our collective CO2 emissions can be expressed as a product of four factors and their relationship with each other :
Population size, economics growth, energy intensity and emissions per energy unit produced.
Here we focus on the last two, because this factors explain how we can stop that.

Our data takes into account all countries and uses aggregation to summarize the situation.

'''

markdown_text2 = '''

On these part, data come from OCDE data base, BP statistical review and Nasa Ozone.
And all of our data are relative.

'''




def get_infoBox1(pathname):
    infobox=    dbc.Row([
                    dbc.Row([html.I( className='fas fa-info', style={'padding-right':20}), html.A("Information Box")],className='infoHead'),

                    dbc.Button("object", id="patent_open1", style= {'margin' : '10px', 'width' : '95%'}),
                    dbc.Modal(
                        [
                            dbc.ModalHeader("object"),
                            dcc.Markdown(children = markdown_text1, style = {'padding' : '15px'}),
                            dbc.ModalFooter(
                            dbc.Button("Close", id="patent_close1", className="ml-auto")
                    )],  id="patent_modal1",
                        scrollable = True),

                    dbc.Button("data", id="patent_open2", style= {'margin' : '10px', 'width' : '95%'}),
                    dbc.Modal(
                        [
                            dbc.ModalHeader("data"),
                            dcc.Markdown(children = markdown_text2, style = {'padding' : '15px'}),
                            dbc.ModalFooter(
                            dbc.Button("Close", id="patent_close2", className="ml-auto")
                    )], id="patent_modal2",
                        scrollable = True),

                ],style={'margin':0},)
    if pathname == "/page1":
        return infobox

                        

