import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

markdown_text1 = '''

A survey was conducted among 2000 peoples over 29 worldwide countries.
3 majors question were asked to determine the attention of the population for each country about climate change and global warming.

'''

markdown_text2 = '''The 3 questions reflecting worldwide attitude about climate change and global warming attention:

Question 1:  Do you consider that climate change impacts your life?
- Yes, of course
- Yes, a little
- Not really
- Not at all
- I don't know

Question 2: Do you change your behavior in order to improve the global situation?
- Yes, of course
- Yes, a little
- Not really
- Not at all
- I don't know


Question 3: Who should we fight global warming?
- Scientist, technical progress
- Ourselves, our habits and behaviours
- It is too late to stop global warming
- I don't know
'''




def get_infoBox5(pathname):
    infobox=    dbc.Row([
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

                    dbc.Button("Survey", id="patent_open2", style= {'margin' : '10px', 'width' : '95%'}),
                    dbc.Modal(
                        [
                            dbc.ModalHeader("Survey"),
                            dcc.Markdown(children = markdown_text2, style = {'padding' : '15px'}),
                            dbc.ModalFooter(
                            dbc.Button("Close", id="patent_close2", className="ml-auto")
                    )], id="patent_modal2",
                        scrollable = True),

                ],style={'margin':0},)
    if pathname == "/page5":
        return infobox

                        

