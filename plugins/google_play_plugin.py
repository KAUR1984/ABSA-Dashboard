from workflow_manager.plugin import Plugin
from plugins.scraper_plugin import ScraperPlugin
import pandas as pd
import numpy as np
import google_play_scraper

class GooglePlayPlugin(ScraperPlugin):
    """
        A plugin that crawls for Google Play Store review data.
        Credit to Gagandeep Kundi for code for transforming data, available at https://www.linkedin.com/pulse/how-scrape-google-play-reviews-4-simple-steps-using-python-kundi

    """

    def scrape(self):
        reviews, _ = google_play_scraper.reviews('com.facebook.katana')
        revDf = pd.DataFrame(np.array(reviews), columns=['review'])
        revDf = revDf.join(pd.DataFrame(revDf.pop('review').tolist()))
        return revDf[['at', 'content', 'score', 'userName']].to_dict(orient='list')