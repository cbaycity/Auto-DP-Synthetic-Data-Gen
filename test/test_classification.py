"""Tests that the classification frameworks operate as expected."""

from src.classification import threshold_calc
from src.dp_calculations import DPResult
import pytest


@pytest.mark.parametrize(
    "threshold,dataset_info,expected_result",
    [
        (
            0.05,
            DPResult(
                100,
                {
                    "A": 1,
                    "B": 6,
                    "C": 91,
                },
            ),
            {"A": "categorical", "B": "numeric", "C": "numeric"},
        ),
        (
            0.9,
            DPResult(
                100,
                {
                    "A": 1,
                    "B": 6,
                    "C": 91,
                },
            ),
            {"A": "categorical", "B": "categorical", "C": "numeric"},
        ),
    ],
)
def test_threshold_calc(
    threshold: float, dataset_info: DPResult, expected_result: dict[str, bool]
):
    """Tests that the classifications output is correct per threshold."""
    assert expected_result == threshold_calc(dataset_info, threshold)
