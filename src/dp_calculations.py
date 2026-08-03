"""Contains methods for DP preprocessing functionality."""

import polars as pl

from typing import NamedTuple
import opendp.prelude as dp

dp.enable_features("contrib")


class DPResult(NamedTuple):
    total_count: int
    column_counts: dict[str, int]


def calculate_values(
    dataset: pl.DataFrame,
    count_budget: int | float,
    per_column_budget: int | float,
) -> DPResult:
    """
    Calculates dp versions of the datasets metadata.


    Returns a total dataset record count and a distinct values count for each column.

    Args:
        dataset: The input dataset to evaluate.
        count_budget: The budget to use for the total values count.
        per_column_budget: The budget to use in each columns distinct value count.
    """

    context = dp.Context.compositor(
        data=dataset.lazy(),
        privacy_unit=dp.unit_of(contributions=1),
        privacy_loss=dp.loss_of(
            epsilon=(count_budget + per_column_budget * len(dataset.columns))
        ),
    )

    count_result = (
        context.query(epsilon=count_budget).select(dp.len()).release().collect()
    )

    result = DPResult(count_result[0, 0], {})

    for column in dataset.columns:
        distinct_query = (
            context.query(epsilon=per_column_budget)
            .select(pl.col(column).dp.n_unique())
            .release()
            .collect()[0, 0]
        )
        result.column_counts[column] = distinct_query

    return result
