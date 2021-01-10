import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output


#==> import external method from .py file from folder /data,  wwhich is plotting the graph

def p5_updateLayout():

    #Defining Spaces ==> Insert your plot into the spaces
    #Example : leftSpace = html.Div(Call_method_of_plotted_graph)
    leftSpace = html.Div([
            dbc.Col([
                dbc.Row([
                    html.H4('', style = { 'margin' : '10px'}),                    
                    dbc.Button("Information Box", id="open"),
                    dbc.Modal(
                        [
                            dbc.ModalHeader("Major infos"),
                            dbc.ModalBody([html.Div("For each countries : 3 questions were asked to 2 thousands people."),
                                        html.Div("Question 1 : Do you consider we are living a climate change ?"),
                                        html.Div("            1 : Yes, of course"),
                                        html.Div("            2 : Yes, a little bit"),
                                        html.Div("            3 : Not really"),
                                        html.Div("            4 : Not at all"),
                                        html.Div("            5 : I don't know"),
                                        html.Div("Question 2 : Did you change your habits in order to improve climate situation ?"),
                                        html.Div("            1 : Yes, of course"),
                                        html.Div("            2 : Yes, a little bit"),
                                        html.Div("            3 : Not really"),
                                        html.Div("            4 : Not at all"),
                                        html.Div("            5 : I don't know"),
                                        html.Div("Question 3 : Who must fight in priority global warming"),
                                        html.Div("            1 : Scientists and technical progress"),
                                        html.Div("            2 : Ourselves, our behaviour and our habits"),
                                        html.Div("            3 : It is too late to stop global warming"),
                                        html.Div("            4 : I don't know")]
                            ),
                            dbc.ModalFooter(
                                dbc.Button("Close", id="close", className="ml-auto")
                    ),
            ],
            id="modal",
            scrollable = True
        ),],style = {'background-color' : 'lightgrey', 'padding' : '30px', 'margin-top' : '30px'})])],

                style={'width': '100%', 'height': 500, 'margin-left' : '15px', 'margin-top' : '15px',  
                        'display' : 'flex', 'flex-direction' : 'column', 'align-items': 'center'})
    up_leftSpace = html.Div(dcc.Graph(figure=maps), style={'height':600 })
    up_rightSpace = html.Div(dcc.Graph(figure=heatmap))


    bot_leftSpace = html.Div(dcc.Graph(figure=piechart))
    bot_rightSpace = html.Div(dcc.Graph(figure=histogram))

    #In "content" the grid gets initialised and styled via HTML and CSS ==> If your graph doesent get displayed the right way you can adjust the styling or text Konstantin
    content = html.Div(
        [dbc.Row( [
            dbc.Col(html.Div(
            leftSpace, className="row justify-content-center"),className='col-2', style ={'padding':20}),            
            dbc.Col(html.Div(
            up_leftSpace, className="row justify-content-center"),className='col-10', style ={'padding':20}),
            ]),
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

df1 = pd.read_csv("data/worldwideattitude/FinaleDataAttitude.csv")
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
histogram.update_layout(yaxis_range=[0,5])
histogram.update_layout(title = "Worldwide consideration of"+'<br>'+"behaviour changement by gender",
                        sliders = [dict(currentvalue={"prefix": "Gender : "})],
                        title_x = 0.5, title_font_size = 15, showlegend=False)


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
                    width=700,
                    height=670)
maps.add_annotation(text="World map displays the national level"+'<br>'+" of attention to the environnement."+'<br>'+" Greenest countries pay more attention.",
                    showarrow=False,
                    x = 0,
                    y = 0)


heatmap = px.density_heatmap(df1,x ="Q2_Do_You_Change_Your_Behaviour", y = "Q1_Consider_Living_CC", animation_frame="COUNTRYR",
                            color_continuous_scale=px.colors.sequential.YlGn,

                             )
heatmap.update_layout(title = "Correlation between"+'<br>'+"behaviour and consideration",
                      title_x = 0.5, title_font_size = 15, coloraxis_showscale=False,
                      xaxis = {"title" : 'behaviour changement'},
                      yaxis = {"title" : 'climate change consideration'},
                      autosize=False,
                      width=400,
                      height=400,
                      paper_bgcolor="white",
                      sliders = [dict(currentvalue={"prefix": "Country : "})])
heatmap.update_traces(hovertemplate = ' Behaviour changement : %{x} <br> Climate change consideration: %{y}<br> Number of person : %{z}')

