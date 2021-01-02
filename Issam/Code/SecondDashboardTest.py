# Environment used: dash1_8_0_env
import pandas as pd     #(version 1.0.0)
import plotly           #(version 4.5.0)
import plotly.express as px

import dash             #(version 1.8.0)
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import plotly.graph_objects as go
# print(px.data.gapminder()[:15])

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

df = pd.read_csv("C:/Users/Elève/Desktop/projet Dashboard/FinaleDataAttitude.csv")
df_map = pd.read_csv("C:/Users/Elève/Desktop/test1.csv")

print(df.head(4))

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# MEN
a1 = df[df['GENDERF'] == 1.0]
b1 = a1['Q1_Consider_Living_CC'].value_counts()
# WOMEN
a2 = df[df['GENDERF'] == 2.0]
b2 = a2['Q1_Consider_Living_CC'].value_counts()

###### MEN
c1 = df[df['GENDERF'] == 1.0]
d1 = c1['Q2_Do_You_Change_Your_Behaviour'].value_counts()
###### WOMEN
c2 = df[df['GENDERF'] == 2.0]
d2 = c2['Q2_Do_You_Change_Your_Behaviour'].value_counts()

###### MEN
e1 = df[df['GENDERF'] == 1.0]
f1 = e1['Q3_How_Fight_CC'].value_counts()
###### WOMEN
e2 = df[df['GENDERF'] == 2.0]
f2 = e2['Q3_How_Fight_CC'].value_counts()

#---------------------------------------------------------------
app.layout = html.Div([

        html.Div([
        dcc.Graph(id='map')
    ]),

    html.Div([dcc.Graph(id='the_graph')],
    style={'width': '30%', 'display': 'inline-block'}),


    html.Div([dcc.Graph(id='the_graph2')],
    style={'width': '30%', 'display': 'inline-block'}),

    html.Div([dcc.Graph(id='the_graph3')],
    style={'width': '30%', 'display': 'inline-block'}),


    html.Div([
        dcc.Dropdown(id = 'mydropdown',
        options=[{'label': 'Homme', 'value': 'b1'},
                 {'label': 'Femme', 'value': 'b2'}],
        value=b1)
        ],
        style={'width': '30%', 'display': 'inline-block'}),



    html.Div([
        dcc.Dropdown(id = 'mydropdown2',
        options=[{'label': 'Homme', 'value': 'd1'},
                 {'label': 'Femme', 'value': 'd2'}],
        value=b1)
        ],
        style={'width': '30%', 'display': 'inline-block'}),



    html.Div([
        dcc.Dropdown(id = 'mydropdown3',
        options=[{'label': 'Homme', 'value': 'f1'},
                 {'label': 'Femme', 'value': 'f2'}],
        value=b1)
        ],
        style={'width': '30%', 'display': 'inline-block'}),


    html.Div([
        dcc.Graph(id='hist1')
    ],
        style={'width': '30%', 'display': 'inline-block'}),

    html.Div([
        dcc.Graph(id='hist2')
    ],
        style={'width': '30%', 'display': 'inline-block'}),

    
    html.Div([
        dcc.Graph(id='hist3')
    ],
        style={'width': '30%', 'display': 'inline-block'})

])



#---------------------------------------------------------------
@app.callback(
    Output(component_id='map', component_property='figure'),
    Output(component_id='the_graph', component_property='figure'),
    Output(component_id='the_graph2', component_property='figure'),
    Output(component_id='the_graph3', component_property='figure'),
    Output(component_id='hist1', component_property='figure'),
    Output(component_id='hist2', component_property='figure'),
    Output(component_id='hist3', component_property='figure'),




    [Input(component_id='mydropdown', component_property='value')],
    [Input(component_id='mydropdown2', component_property='value')],
    [Input(component_id='mydropdown3', component_property='value')]
)

def update_output(mydropdown, mydropdown2, mydropdown3):

    figA = px.histogram(df, x = "COUNTRYR", y = "Q1_Consider_Living_CC", histfunc='avg',
                    labels={
                     "COUNTRYR": "",
                     "Q1_Consider_Living_CC": "living climate change quesion"
                     })
    figA.add_shape(type="line",
    x0=-0.5, y0=1, x1=29.5, y1=1,
    line=dict(
        color="lime",
        width=2,
        dash="dashdot")
    )
    figA.update_layout(yaxis_range=[0,5])

    figB = px.histogram(df, x = "COUNTRYR", y = "Q2_Do_You_Change_Your_Behaviour", histfunc='avg',
                    labels={
                     "COUNTRYR": "",
                     "Q2_Do_You_Change_Your_Behaviour": "behaviour changment"
                     })
    figB.add_shape(type="line",
    x0=-0.5, y0=2, x1=29.5, y1=2,
    line=dict(
        color="lime",
        width=2,
        dash="dashdot")
    )
    figB.update_layout(yaxis_range=[0,5])

    figC = px.histogram(df, x = "COUNTRYR", y = "Q3_How_Fight_CC", histfunc='avg',
                    labels={
                     "COUNTRYR": "",
                     "Q3_How_Fight_CC": "how fight CC"
                     })
    figC.add_shape(type="line",
    x0=-0.5, y0=2, x1=29.5, y1=2,
    line=dict(
        color="lime",
        width=2,
        dash="dashdot"))
    figC.update_layout(yaxis_range=[0,4])

    map = px.choropleth(df_map, locations="ISO",
    color="PUBLI_RATE",
    hover_name="COUNTRY",
    title='Public Opinion Worldwide',
    color_continuous_scale=px.colors.sequential.Cividis
    )
    
    colors1 = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen','red']

    if (mydropdown == 'b2'):
        fig1 = go.Figure(data=[go.Pie(labels=['Yes, of course','Yes, a little','Not really','Not at all','Dont know'],
                             values = b2)])
        fig1.update_traces(hoverinfo='label+percent', textinfo='label',
                  marker=dict(colors=colors1, line=dict(color='#000000', width=0.5)))
        fig1.update_layout(title = "Do you consider we are living a Climate Change ?", title_font_size = 15, showlegend=False)
    else:
        fig1 = go.Figure(data=[go.Pie(labels=['Yes, of course','Yes, a little','Not really','Not at all','Dont know'],
                             values = b1)])
        fig1.update_traces(hoverinfo='label+percent', textinfo='label',
                  marker=dict(colors=colors1, line=dict(color='#000000', width=0.5)))
        fig1.update_layout(title = "Do you consider we are living a Climate Change ? ",title_font_size = 15, showlegend=False)

    if (mydropdown2 == 'd2'):
        fig2 = go.Figure(data=[go.Pie(labels=['Yes, of course','Yes, a little','Not really','Not at all','Dont know'],
                             values = d2)])
        fig2.update_traces(hoverinfo='label+percent', textinfo='label',
                  marker=dict(colors=colors1, line=dict(color='#000000', width=0.5)))
        fig2.update_layout(title = "Did you change your habits to improve <br> climate situation ?", title_x = 0.5, title_font_size = 15, showlegend=False)
    else:
        fig2 = go.Figure(data=[go.Pie(labels=['Yes, of course','Yes, a little','Not really','Not at all','Dont know'],
                             values = d1)])
        fig2.update_traces(hoverinfo='label+percent', textinfo='label',
                  marker=dict(colors=colors1, line=dict(color='#000000', width=0.5)))
        fig2.update_layout(title = "Did you change your habits to improve <br> climate situation ? ", title_x = 0.5, title_font_size = 15, showlegend=False)

    if (mydropdown3 == 'f2'):
        fig3 = go.Figure(data=[go.Pie(labels=['Yes, of course','Yes, a little','Not really','Not at all','Dont know'],
                             values = f2)])
        fig3.update_traces(hoverinfo='label+percent', textinfo='label',
                  marker=dict(colors=colors1, line=dict(color='#000000', width=0.5)))
        fig3.update_layout(title = "Who must fight in priority global warming ?",  title_font_size = 15, showlegend=False)
    else:
        fig3 = go.Figure(data=[go.Pie(labels=['Yes, of course','Yes, a little','Not really','Not at all','Dont know'],
                             values = f1)])
        fig3.update_traces(hoverinfo='label+percent', textinfo='label',
                  marker=dict(colors=colors1, line=dict(color='#000000', width=0.5)))
        fig3.update_layout(title = "Who must fight in priority global warming ?", title_font_size = 15, showlegend=False)

    return map, fig1, fig2, fig3, figA, figB, figC

if __name__ == '__main__':
    app.run_server(debug=True)