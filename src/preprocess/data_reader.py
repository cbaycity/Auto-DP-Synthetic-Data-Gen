"""Helper function to read the datasets into dataframes."""

import polars as pl
import os

SAMPLE_DATASETS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "sample-datasets"
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
        result[dataset] = pl.read_csv(
            os.path.join(SAMPLE_DATASETS_DIR, dataset, "data.csv"),
            infer_schema_length=100_000
        )
    return result
