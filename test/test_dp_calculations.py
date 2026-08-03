"""Tests that the dp calculations works as expected."""

import polars as pl
import numpy as np
import pytest
from src.dp_calculations import calculate_values


LARGE_EPSILON = 1_000
SMALL_EPSILON = 1e-10
DUMMY_DATASET_SIZE = 10_000
DUMMY_DATASET = pl.DataFrame(
    {
        "A": np.random.randint(low=0, high=1, size=DUMMY_DATASET_SIZE),
        "B": np.random.randint(low=-10, high=10, size=DUMMY_DATASET_SIZE),
        "C": np.random.uniform(low=-10, high=10, size=DUMMY_DATASET_SIZE),
        "D": np.random.laplace(loc=0.0, scale=10, size=DUMMY_DATASET_SIZE),
    }
)
"""A dataset with completely fake and mock records for testing."""


def test_large_epsilon():
    """Tests that with a large epsilon the dp results are very accurate."""
    result = calculate_values(DUMMY_DATASET, LARGE_EPSILON, LARGE_EPSILON)
    assert result.total_count == pytest.approx(DUMMY_DATASET_SIZE, abs=5), (
        "True Count, {DUMMY_DATASET_SIZE}, was not close to estimated count, {result.total_count}."
    )

    for column in result.column_counts.keys():
        true_count = DUMMY_DATASET[column].n_unique()
        assert result.column_counts[column] == pytest.approx(true_count, abs=5), (
            "Col, {column}, had far apart distinct counts and estimates: n_unique-{true_count}, estimated-{result.column_counts[column]}"
        )
