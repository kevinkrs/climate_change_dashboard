#Setup for Dash and needed components
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input
from dash.dependencies import Output
from dash.dependencies import State
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px
#Setup for Redis Queu ==> Handling long term processes
from redis import Redis
from rq import Worker, Queue, Connection
from rq.job import Job
from flask_caching import Cache