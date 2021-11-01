# -*- coding: utf-8 -*-
import logging
import os

import luigi
import pandas as pd

from models.AspectBasedSentimentAnalysis.dataset.read_dataset import read_json_formatted
from models.AspectBasedSentimentAnalysis.training.helpers import format_dataset
from models.AspectBasedSentimentAnalysis.training.helpers import makedirs_with_mode

logger = logging.getLogger(__name__)

BASE_PROCESSED_DIR = os.path.expanduser('~/processed')


class BaseTask(luigi.Task):
    @property
    def outfilename(self):
        return 'processed_{}.{}'.format(self.__class__.__name__.lower(),
                                        self.output_file_extension)

    @property
    def output_file_extension(self):
        return 'csv'

    @property
    def base_folder_path(self):
        return BASE_PROCESSED_DIR

    def output(self):
        if not os.path.isdir(self.base_folder_path):
            logger.debug('Creating non-existent path: %s',
                         self.base_folder_path)
            makedirs_with_mode(self.base_folder_path)
        filepath = os.path.join(self.base_folder_path, self.outfilename)
        return luigi.LocalTarget(filepath)


class AcquireDataset(BaseTask):
    dataset_filename = luigi.Parameter()

    def run(self):
        annotated_dataset = self.read_dataset()
        dataset = format_dataset(annotated_dataset)
        pd.to_pickle(dataset, self.output().path)

    def read_dataset(self):
        return read_json_formatted(self.dataset_filename)


def get_dataset(dataset_filename=None):
    """

    :param data-set_filename:
    :return:
    """
    annoted_data = read_json_formatted(dataset_filename)
    dataset = []
    for row in annoted_data:
        sources = [s.lower() for s in row['target']]
        targets = [s.lower() for s in row['polarity']]
        sentence_meta = {}
        sentence = row['sentence']
        for source, target in zip(sources, targets):
            sentence_meta[source] = target
        dataset.append({'sentence': sentence, 'meta': sentence_meta})
    return dataset


if __name__ == '__main__':
    luigi.run()
