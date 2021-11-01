from abc import ABC, abstractmethod
from workflow_manager.plugin import Plugin


class ScraperPlugin(ABC, Plugin):
    """
        An abstract class that represents a plugin that scrapes reviews from a web source.

    """

    @abstractmethod
    def scrape(self):
        pass
