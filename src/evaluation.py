"""Has methods to calculate"""

from frozendict import frozendict
from data_reader import DATASET_DIRS, SAMPLE_DATASETS_DIR
import polars as pl
import os

COL_CLASSIFICATION_PATH = "column-classifications.csv"
"""A constant string representing the file name with correct classifications."""

# Constants for column-classification.csv columns.
COL = "column"
CATEGORICAL = "categorical"


def get_correct_answer() -> frozendict:
    """Returns a dictionary mapping datasets and columns to their correct classification."""

    correct_answers = {}
    """A dictionary of correct dataset, col mappings to categorical classification."""

    # Update correct_answers for export.
    for dataset in DATASET_DIRS:
        classifications_path = os.path.join(
            SAMPLE_DATASETS_DIR, dataset, COL_CLASSIFICATION_PATH
        )
        print(classifications_path)
        classifications = pl.read_csv(classifications_path)
        for i in range(len(classifications)):
            correct_answers[(dataset, classifications[i, COL])] = classifications[
                i, CATEGORICAL
            ]

    return frozendict(correct_answers)


print(get_correct_answer())
