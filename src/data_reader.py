"""Helper function to read the datasets into dataframes."""

import polars as pl
import os

SAMPLE_DATASETS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "sample-datasets"
)
DATASET_DIRS = [
    d
    for d in os.listdir(SAMPLE_DATASETS_DIR)
    if os.path.isdir(os.path.join(SAMPLE_DATASETS_DIR, d))
]


def collect_datasets() -> dict[str, pl.DataFrame]:
    """Reads the sample datasets into a dict of Polars Dataframes."""
    result = {}
    for dataset in DATASET_DIRS:
        print(f"Dataset: {os.path.join(SAMPLE_DATASETS_DIR, dataset, 'data.csv')}")
        result[dataset] = pl.read_csv(
            os.path.join(SAMPLE_DATASETS_DIR, dataset, "data.csv")
        )
    return result


# collect_datasets()
# for dataset, df in collect_datasets().items():
#    print(f"Dataset: {dataset}, df: {df}")
