import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc


def get_infoBox3(pathname):
    infobox = dbc.Row([
                       
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
                    ],style={'margin':0},)

    if pathname == "/page3":
        return infobox


markdown_text1 = '''

More than 100 countries worldwide are covered.

Geographical aggregates are provided for the EU-28, the OECD total, and the World total.
Fractional counts applied for patents with multiple inventors/applicants:
When a patent was invented by several inventors from different countries, the respective contributions of each country is taken into account. This is done in order to eliminate multiple counting of such patents.
For example, a patent co-invented by 1 French, 1 American and 2 German residents will be counted as:

- 1/4th of a patent for France
- 1/4th for the USA
- and ½ patent for Germany.


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

