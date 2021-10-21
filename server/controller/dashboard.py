# -*- coding: utf-8 -*-
from dash import Dash
import dash_html_components as html
from flask import Flask
import dash_core_components as dcc
from plotly.graph_objs import *

"""
    Contains commands to build dashboard visualisations

"""

server = Flask(__name__)
ranking = Dash(__name__, server=server, url_base_pathname='/ranking/')
ranking.layout = html.Div()
timeplot = Dash(__name__, server=server, url_base_pathname='/timeplot/')
timeplot.layout = html.Div()


def create_timeplot():
    trace1 = Bar(
        x=["Emoji A", "Emoji B", "Emoji C", "Emoji D", "Emoji E", "Emoji F", "Emoji G", "Emoji H", "Emoji I",
           "Emoji J"],
        y=[150, 100, 94, 56, 43, 31, 22, 15, 10, 2],
        marker={
            "color": "rgb(204, 255, 204)",
            "line": {
                "color": "rgb(102, 153, 153)",
                "width": 1.5
            }
        },
        opacity=0.6,
        text=["Emoji A", "Emoji B", "Emoji C", "Emoji D", "Emoji E", "Emoji F", "Emoji G", "Emoji H", "Emoji I",
              "Emoji J"],
    )

    data = [trace1]
    layout = {"title": "Top 10 Emojis Clusters"}
    fig = Figure(data=data, layout=layout)

    histogram1.layout = html.Div(children=[
        dcc.Graph(
            id='example-graph',
            figure=fig
        )
    ])


def create_ranking():

    histogram2.layout = html.Div([
        html.Table([
            html.Tr([html.Td(['Feature1']), html.Td(['0.8'])]),
            html.Tr([html.Td(['Feature2']), html.Td(['0.4'])]),
            html.Tr([html.Td(['Feature3']), html.Td(['0'])]),
            html.Tr([html.Td(['Feature4']), html.Td(['-0.4'])]),
            html.Tr([html.Td(['Feature5']), html.Td(['-0.8'])]),
        ])
    ])

