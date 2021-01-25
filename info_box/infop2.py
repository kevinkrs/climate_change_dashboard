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

                    dbc.Button("Funding", id="patent_open2", style= {'margin' : '10px', 'width' : '95%'}),
                    dbc.Modal(
                        [
                            dbc.ModalHeader("Funding"),
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

The data for Net-Zero Tracker was provided by climatewatch.org and gives information about countries with Net-Zero target and the aimed year to achieve the goal. 
Unfortunately there's not many countries with such a goal already set, hence we're only able to display the given dataset with Net-Zero.

'''

markdown_text2 = '''
**Multilateral**
...

**Multi Donor National**
...

**Multi Donor Regional**
...

'''