import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import csv

def prepare_daily_report():

    df_country_code = pd.read_csv('../Data/data_situation2.csv')
    
    return(df_country_code)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'Covid19-Dash'
app.layout = html.Div([html.Div([html.H1("Global Warning")],
                                style={'textAlign': "center", "padding-bottom": "30"}
                               ),
                       html.Div([html.Span("Metric to display : ", className="six columns",
                                           style={"text-align": "right", "width": "40%", "padding-top": 10}),
                                 dcc.Dropdown(id="value-selected", value='CO2_emissions',
                                              options=[{'label': "CO2_emissions ", 'value': 'CO2_emissions'},
                                                       {'label': "Death_from_air_pollution ", 'value': 'Death_from_air_pollution'},
                                                       {'label': "Ozone_concentration ", 'value': 'Ozone_concentration'},
                                                       {'label': "GDP_BILLIONS ", 'value': 'GDP_BILLIONS'}],
                                              style={"display": "block", "margin-left": "auto", "margin-right": "auto",
                                                     "width": "70%"},
                                              className="six columns")], className="row"),
                       dcc.Graph(id="my-graph")
                       ], className="container")

@app.callback(
    dash.dependencies.Output("my-graph", "figure"),
    [dash.dependencies.Input("value-selected", "value")]
)
def update_figure(selected):
    #dff = prepare_confirmed_data()

    dff = prepare_daily_report()
    dff['hover_text'] = dff["Country_Region"] + ": " + dff[selected].apply(str)

    trace = go.Choropleth(locations=dff['CODE'],z=np.log(dff[selected]),
                          text=dff['hover_text'],
                          hoverinfo="text",
                          marker_line_color='white',
                          autocolorscale=False,
                          reversescale=True,
                          colorscale="RdBu",marker={'line': {'color': 'rgb(180,180,180)','width': 0.5}},
                          colorbar={"thickness": 10,"len": 0.3,"x": 0.9,"y": 0.7,
                                    'title': {"text": 'persons', "side": "bottom"},
                                    'tickvals': [ 2, 10],
                                    'ticktext': ['100', '100,000']})   
    return {"data": [trace],
            "layout": go.Layout(height=800,geo={'showframe': False,'showcoastlines': False,
                                                                      'projection': {'type': "miller"}})}

if __name__ == '__main__':
    app.run_server(debug=True)
    
    
    
