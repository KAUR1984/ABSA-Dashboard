from workflow_manager.plugin import Plugin
import pandas as pd
from models.AspectBasedSentimentAnalysis.training.train_top_classifier import prediction_for_pipe

class AbsaPlugin(Plugin):
    def predict(self):
        data = prediction_for_pipe()
        return data.to_dict(orient='list')
        # return pd.read_csv('../models/AspectBasedSentimentAnalysis/prediction_step_rows.csv').to_dict(orient='list')