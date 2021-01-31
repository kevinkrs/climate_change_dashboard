import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc




def get_infoBox2(pathname):
    infobox =    dbc.Row([
                    html.P("Information Box",className="lead", style={'width':'100%'}),

                    dbc.Button("Net-Zero Tracker", id="patent_open1", style= {'margin' : '10px', 'width' : '95%'}),
                    dbc.Modal(
                        [
                            dbc.ModalHeader("Net-Zero Tracker"),
                            dcc.Markdown(children = markdown_text1, style = {'padding' : '15px'}),
                            dbc.ModalFooter(
                            dbc.Button("Close", id="patent_close1", className="ml-auto")
                    )],  id="patent_modal1",
                        scrollable = True),

                    dbc.Button("Funding by Countries", id="patent_open2", style= {'margin' : '10px', 'width' : '95%'}),
                    dbc.Modal(
                        [
                            dbc.ModalHeader("Funding by Countries"),
                            dcc.Markdown(children = markdown_text2, style = {'padding' : '15px'}),
                            dbc.ModalFooter(
                            dbc.Button("Close", id="patent_close2", className="ml-auto")
                    )], id="patent_modal2",
                        scrollable = True),

                ],style={'margin':0},)
    if pathname == "/page2":
        return infobox

                        


markdown_text1 = '''
**Net-Zero Energy** is a goal to saturate a countries energy consumption only with renewable energy sources.

**Pledged** refers to money that has been pledged as a donation to a specific fund but has not yet necessarily arrived at the fund. A transaction of the complete promised amount is not necessarily safe.
**Deposited** refers to money which has been donated by a contributor and is now owned by a fund.

'''

markdown_text2 = '''
**Climate Funds update** is an organisation supported by the Heinrich Böll Stiftung and provides a managed database for institutes and organisations to submit information about the funding of climate funds which basically support the mititgation of climate change related events.

The data, for most funds, is up to date as of February 2020.


'''