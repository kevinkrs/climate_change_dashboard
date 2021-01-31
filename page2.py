from lib.lib import *
from data.Economic_Impact.graphs import get_iGreenBondData
from data.Governmental_efforts.graphs import get_fundingGraph, get_fundingGraph, get_pledgedGraph, get_NetZeroTargetWM

#==> import external method from .py file from folder /data,  wwhich is plotting the graph

def p2_updateLayout():
    #Defining Spaces ==> Insert your plot into the spaces
   #leftSpace = html.Div([
    #    html.H4('Indicators', style = {'color' : 'white'}),
     #       dcc.Dropdown(id = 'dropdown_po', 
      #              options =[{'label' : 'EPO', 'value' : '0' },
       #                     {'label' : 'USPTO', 'value' : '1'},
        #                    {'label' : 'PCT', 'value' : '2'}], 
         #                   value = '0',
          #                  placeholder = 'Select patent office',  style = {'margin-bottom' : 10})],
           #             style = {'margin-top' : 200, 'padding' : 10, 'margin-left' : 10, 'background-color' : 'lightgreen', 'border-radius' : 5})
        #Example : leftSpace = html.Div(Call_method_of_plotted_graph)

    midSpace = html.Div(dcc.Graph(figure=get_NetZeroTargetWM()))
    botSpace = html.Div(dcc.Graph(figure=get_fundingGraph()))

    #In "content" the grid gets initialised and styled via HTML and CSS ==> If your graph doesent get displayed the right way you can adjust the styling or text Konstantin
    content = html.Div(
        [dbc.Row( [
            #dbc.Col(
            #leftSpace,className='col-2', style ={'padding':20}),
            dbc.Col(
            midSpace, className='col-12',style ={'padding':20}),],
            ),
        dbc.Row( 
            dbc.Col(
            botSpace, className='col-6', style ={'padding':20}),
            ),],
            style={ 'width' : 'auto', 'padding' : 30, 'overflow' : 'hidden'},)
    
    return content