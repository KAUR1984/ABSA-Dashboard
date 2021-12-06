import logging
from flask import redirect, Blueprint, render_template
from server.controller import visualization
from smm_workflow import workflow_most_common_emojis
import numpy as np
import pandas as pd
from workflow_manager.job_creator import JobCreator
from plugins.enum.plugins_enum import PluginsEnum

import dash
import dash_html_components as html
import plotly.graph_objects as go
import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output


"""
    Routes for outputs for front-end are set in this module
"""


bp = Blueprint('pages', __name__)
logger = logging.getLogger()


@bp.route('/')
def view_base():
    return "Home"

@bp.route('/app_store')
def render_app_store():
    conf = {'method_name': 'scrape', 'args': []}
    app_store_plugin = JobCreator(plugin=PluginsEnum.GooglePlayPlugin)
    job = app_store_plugin.create_job(conf)

    # conf = {'method_name': 'predict', 'args': []}
    # ABSA_plugin = JobCreator(plugin=PluginsEnum.AbsaPlugin)
    # job = ABSA_plugin.create_job(conf)

    data = job.delay().get()
    return render_template('app_store_data.html',  tables=data)


df = pd.DataFrame({
    "Feature": ["Feature1", "Feature2", "Feature3", "Feature4", "Feature5", "Feature6"],
    "Amount": [0.34, -0.53, 0.67, 0.84, -0.25, 0.44]
})

@bp.route('/dash_test')
def dash_test():
    layout = html.Div(children=[
        html.H1(children='Hello Dash'),

        dcc.Graph(
            id='example-graph',
            figure=fig
        )
    ])
    return layout 

