import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output


#==> import external method from .py file from folder /data,  wwhich is plotting the graph

def p5_updateLayout():

    #Defining Spaces ==> Insert your plot into the spaces
    #Example : leftSpace = html.Div(Call_method_of_plotted_graph)
    up_leftSpace = html.Div(dcc.Graph(figure=maps), style={'height':400})
    up_rightSpace = html.Div(dcc.Graph(figure=heatmap), style={'height':400})


    bot_leftSpace = html.Div(dcc.Graph(figure=piechart))
    bot_rightSpace = html.Div(dcc.Graph(figure=histogram))

    #In "content" the grid gets initialised and styled via HTML and CSS ==> If your graph doesent get displayed the right way you can adjust the styling or text Konstantin
    content = html.Div(
        [dbc.Row( [
            dbc.Col(
            up_leftSpace,className='col-6',style ={'padding':0}),
            dbc.Col(
            up_rightSpace, className='col-6',style ={'padding':0}),]),
            dbc.Row( [
            dbc.Col(
            bot_leftSpace,className='col-6',style ={'padding':20}),
            dbc.Col(
            bot_rightSpace, className='col-6',style ={'padding':20}),],
            )],
            style={ 'width' : 'auto', 'padding' : 30, 'overflow' : 'hidden'},)
    
    return content



import plotly.express as px
import pandas as pd
import plotly.graph_objs as go

df1 = pd.read_csv("data2/worldwideattitude/FinaleDataAttitude.csv")
df2 = pd.read_csv("data2/worldwideattitude/test1.csv")

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
histogram.update_layout(yaxis_range=[0,5])
histogram.update_layout(title = "Worldwide consideration of"+'<br>'+"behaviour changement by gender", title_x = 0.5, title_font_size = 15, showlegend=False)



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
maps.update_layout(title = "Nation public opininon about"+'<br>'+"climate situation",
                   title_x = 0.5, title_font_size = 15, coloraxis_showscale=False,
                    autosize=False,
                    paper_bgcolor="white",
                    width=620,
                    height=500)
maps.add_annotation(text="World map displays the national level"+'<br>'+" of attention to the environnement."+'<br>'+" Greenest countries pay more attention.",
                    showarrow=False,
                    x = 0,
                    y = 0)


heatmap = px.density_heatmap(df1,x ="Q2_Do_You_Change_Your_Behaviour", y = "Q3_How_Fight_CC", animation_frame="COUNTRYR",
                            color_continuous_scale=px.colors.sequential.YlGn,
                             )
heatmap.update_layout(title = "Correlation between"+'<br>'+"behaviour and responsabilities",
                      title_x = 0.5, title_font_size = 15, coloraxis_showscale=False,
                      autosize=False,
                      width=400,
                      height=400,
                      paper_bgcolor="white")
