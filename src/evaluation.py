"""Has methods to calculate"""

from frozendict import frozendict
from data_reader import DATASET_DIRS, SAMPLE_DATASETS_DIR
from dp_calculations import calculate_values
import polars as pl
import os

COL_CLASSIFICATION_PATH = "column-classifications.csv"
"""A constant string representing the file name with correct classifications."""

# Constants for column-classification.csv columns.
COL = "column"
CATEGORICAL = "categorical"


def get_correct_answers() -> frozendict:
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


def classification_accuracy(
    correct_answers: frozendict, predictions: dict
) -> (int, int):
    """Returns an accuracy score comparing the predictions to the correct answers.

    Args:
        correct_answers: A mapping of datasets to ideal column classifications.
        predictions: Mapping of dataset to predicted column classifications.

    Returns:
        total_column: The total number of columns evaluated.
        correct_answers: The total number of correct classifications.
    """

    # Both dicts have key: (dataset, column), value: "categorical" | "numerical"
    total_columns = 0
    correct_answers = 0
    for key in predictions.keys():
        total_columns += 1
        if predictions[key] == correct_answers[key]:
            correct_answers += 1

    return (total_columns, correct_answers)


# Need a method to bind classifications.threshold_calc to the same type.
def create_predictions(
    datasets: dict[str, pl.DataFrame],
    count_budget: int | float,
    per_column_budget: int | float,
    classifier: callable,
):
    """A method to calculate predictions on a dataset."""

    result = {}
    for dataset_name, dataset in datasets.items():
        get_metadata = calculate_values(dataset, count_budget, per_column_budget)
        predictions: dict[str, str] = classifier(get_metadata)
        for column, categorical in predictions.items():
            result[(dataset_name, column)] = categorical
    return result
