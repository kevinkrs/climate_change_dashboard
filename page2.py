from lib.lib import *
from data.Governmental_efforts.graphs import get_fundingGraph, get_fundingGraph, get_NetZeroTargetWM

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

    midSpace = html.Div(dcc.Loading(dcc.Graph(figure=get_NetZeroTargetWM()),color='#45bf55', type='graph', className='pv6'),style={'padding':30, 'background-color':'#f8f7f7', 'border-radius': 10})
    botSpace = html.Div(dcc.Loading(dcc.Graph(figure=get_fundingGraph()),color='#45bf55', type='graph', className='pv6'),style={'padding':30, 'background-color':'#FFFFFF', 'border-radius': 5})

    #In "content" the grid gets initialised and styled via HTML and CSS ==> If your graph doesent get displayed the right way you can adjust the styling or text Konstantin
    content = html.Div(
        [dbc.Row( [
            #dbc.Col(
            #leftSpace,className='col-2', style ={'padding':20}),
            dbc.Col(
            midSpace, className='col-12',style ={'padding':35}),],
            ),
        dbc.Row( 
            dbc.Col(
            botSpace, className='col-12', style ={'padding':20}),
            style={'background-color':'#FFFFFF' }
            ),],
            style={ 'width' : 'auto', 'padding' : 30, 'overflow' : 'hidden'},)
    
    return content