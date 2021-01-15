import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output
from info_box.infop5 import get_infoBox5


#==> import external method from .py file from folder /data,  wwhich is plotting the graph

def p5_updateLayout():

    #Defining Spaces ==> Insert your plot into the spaces
    #Example : leftSpace = html.Div(Call_method_of_plotted_graph)
    

    up_leftSpace = html.Div(dcc.Graph(figure=maps), style={'height':600 })
    up_rightSpace = html.Div(dcc.Graph(figure=heatmap))


    bot_leftSpace = html.Div(dcc.Graph(id = 'p5pie'))
    bot_rightSpace = html.Div(dcc.Graph(figure=histogram))
    drop = html.Div(dcc.Dropdown(id = 'p5pie_dm',
        options=[{'label': 'Men', 'value': 0},
                 {'label': 'Women', 'value': 1}],
        value=0))

    #In "content" the grid gets initialised and styled via HTML and CSS ==> If your graph doesent get displayed the right way you can adjust the styling or text Konstantin
    content = html.Div(
        [dbc.Row( [           
            dbc.Col(html.Div(
            up_leftSpace, className="row justify-content-center"),className='col-12', style ={'padding':20}),
            ]),
            dbc.Row([dbc.Col(drop, className = 'col-4', style = {"display": "block",
            "margin-left": "auto",
            "margin-right": "auto"})]),
            dbc.Row( [            
            dbc.Col(html.Div(
            up_rightSpace, className="row justify-content-center"), className='col-4',style ={'padding':20}),
            dbc.Col(
            bot_leftSpace,className='col-4',style ={'padding':20}),
            dbc.Col(
            bot_rightSpace, className='col-4',style ={'padding':20}),],
            )],
            style={ 'width' : 'auto', 'padding' : 30, 'overflow' : 'hidden'},)
    
    return content



import plotly.express as px
import pandas as pd
import plotly.graph_objs as go

df1 = pd.read_csv("data/worldwideattitude/data.csv")
df2 = pd.read_csv("data/worldwideattitude/test1.csv")

df3=  pd.merge(df1, df2, on="ISO")



histogram = px.histogram(df3, x = "COUNTRYR", y = "Q2_Do_You_Change_Your_Behaviour", histfunc='avg',
                        color_discrete_sequence=["limegreen"],
                        animation_frame="GENDERF",
                            labels={
                            "COUNTRYR": "",
                            "Q2_Do_You_Change_Your_Behaviour": "behaviour changement"
                            })
histogram.add_shape(type="line",
            x0=-0.5, y0=2, x1=29.5, y1=2,
            line=dict(
                color="forestgreen",
                width=2,
                dash="dashdot")
            )
histogram.update_layout(yaxis_title="Behaviour Changement",
                            yaxis = dict(
                            tickmode = 'array',
                            tickvals = [1, 2, 3, 4],
                            ticktext = ['Yes', 'A little', 'Not really', 'Not']),)
histogram.update_layout(title = "Worldwide consideration of"+'<br>'+"behaviour changement by gender",
                        sliders = [dict(currentvalue={"prefix": "Gender : "})],
                        title_x = 0.5, title_font_size = 15, showlegend=False)
histogram['layout']['updatemenus'][0]['pad']=dict(r= 10, t= 100)
histogram['layout']['sliders'][0]['pad']=dict(r= 10, t= 100,)



colors1 = ['forestgreen', 'limegreen', 'yellowgreen','aliceblue']

piechart = go.Figure(data=[go.Pie( labels=['Scientists'+'<br>'+'Technical progress','Ourselves'+'<br>'+'habits, behaviour','Its too late','Dont know'],
                                values = df1['Q3_How_Fight_CC'].value_counts())])
piechart.update_traces(hoverinfo='label+percent', textinfo='label',
                    marker=dict(colors=colors1, line=dict(color='#000000', width=0.5)))
piechart.update_layout(title = "Worldwide consideration of who"+'<br>'+"must fight global warming", title_x = 0.5, title_font_size = 15, showlegend=False)



maps = px.choropleth(df2, locations="ISO",
                            color="PUBLI_RATE",
                            hover_name="COUNTRY",
                            color_continuous_scale=px.colors.sequential.YlGn,
                            )
maps.update_layout(title={
                        'text': "Nation public opinion about climate situation",
                        'y':0.85,
                        'x':0.5,
                        'xanchor': 'center',
                        'yanchor': 'top'},
                   title_x = 0.5, title_font_size = 15, coloraxis_showscale=False,
                    autosize=False,
                    paper_bgcolor="white",
                    width=1000,
                    height=800,)
maps.add_annotation(text="World map displays the national level of attention to the environnement. Greenest countries pay more attention.",
                    showarrow=False,
                    x = 0.5,
                    y = 0.88)


heatmap = px.density_heatmap(df1,x ="Q2_Do_You_Change_Your_Behaviour", y = "Q1_Consider_Living_CC", animation_frame="COUNTRYR",
                            color_continuous_scale=px.colors.sequential.YlGn,

                             )
heatmap.update_layout(title = "Correlation between"+'<br>'+"behaviour and consideration",
                      title_x = 0.5, title_font_size = 15, coloraxis_showscale=False,
                      xaxis_title="Behaviour Changements",
                      yaxis_title="Climate Change Consideration",
                      xaxis = dict(
                            tickmode = 'array',
                            tickvals = [1, 2, 3, 4, 5],
                            ticktext = ['Yes', 'A little', 'Not really', 'Not', 'Dont know']),
                      yaxis = dict(
                            tickmode = 'array',
                            tickvals = [1, 2, 3, 4, 5],
                            ticktext = ['Yes', 'A little', 'Not really', 'Not', 'Dont know']),
                      autosize=False,
                      width=400,
                      height=400,
                      paper_bgcolor="white",
                      sliders = [dict(currentvalue={"prefix": "Country : "})])

heatmap.update_traces(hovertemplate = ' Behaviour changements : %{x} <br> Climate change consideration: %{y}<br> Number of person : %{z}')
heatmap['layout']['updatemenus'][0]['pad']=dict(r= 10, t= 100)
heatmap['layout']['sliders'][0]['pad']=dict(r= 10, t= 100,)


def pie1():
    
    colors1 = ['forestgreen', 'limegreen', 'yellowgreen', 'white']
    
    # MEN
    a1 = df1[df1['GENDERF'] == 1.0]
    b1 = a1['Q3_How_Fight_CC'].value_counts()

    fig1 = go.Figure(data=[go.Pie(labels=['Scientists','Ourselves','Too late','Dont know'],
                             values = b1)])
    fig1.update_traces(hoverinfo='label+percent', textinfo='label',
                  marker=dict(colors=colors1, line=dict(color='#000000', width=0.5)))
    fig1.update_layout(title = "Who must fight global warming ?", title_font_size = 15, showlegend=False)

    return fig1

def pie2():
    colors1 = ['forestgreen', 'limegreen', 'yellowgreen', 'white']


                # WOMEN
    a2 = df1[df1['GENDERF'] == 2.0]
    b2 = a2['Q3_How_Fight_CC'].value_counts()

    fig2 = go.Figure(data=[go.Pie(labels=['Scientists','Ourselves','Too late','Dont know'],
                             values = b2)])
    fig2.update_traces(hoverinfo='label+percent', textinfo='label',
                  marker=dict(colors=colors1, line=dict(color='#000000', width=0.5)))
    fig2.update_layout(title = "Who must fight global warming ?",title_font_size = 15, showlegend=False)



    return fig2

def get_pie():
    return [pie1(), pie2()]

