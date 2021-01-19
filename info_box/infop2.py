import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc




def get_infoBox2(pathname):
    infobox=    dbc.Row([
                    html.P("Information Box",className="lead", style={'width':'100%'}),

                    dbc.Button("In Policy Document", id="patent_open1", style= {'margin' : '10px', 'width' : '95%'}),
                    dbc.Modal(
                        [
                            dbc.ModalHeader("In Policy Document"),
                            dcc.Markdown(children = markdown_text1, style = {'padding' : '15px'}),
                            dbc.ModalFooter(
                            dbc.Button("Close", id="patent_close1", className="ml-auto")
                    )],  id="patent_modal1",
                        scrollable = True),

                    dbc.Button("In Law", id="patent_open2", style= {'margin' : '10px', 'width' : '95%'}),
                    dbc.Modal(
                        [
                            dbc.ModalHeader("In Law"),
                            dcc.Markdown(children = markdown_text2, style = {'padding' : '15px'}),
                            dbc.ModalFooter(
                            dbc.Button("Close", id="patent_close2", className="ml-auto")
                    )], id="patent_modal2",
                        scrollable = True),

                ],style={'margin':0},)
    if pathname == "/page2":
        return infobox

                        


markdown_text1 = '''



'''

markdown_text2 = '''



'''