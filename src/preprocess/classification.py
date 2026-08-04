"""Methods to classify if a column is categorical or continuous."""

from preprocess.dp_calculations import DPResult


def threshold_calc(dataset_info: DPResult, threshold: float = 0.05) -> dict[str, str]:
    """Calculates if a variable is categorical based on thresholding.

    Args:
        dataset_info: The target dataset with columns to evaluate.
        threshold: The percent of the data that if it is unique it counts as categorical.
    """
    result = {}
    for column, count in dataset_info.column_counts.items():
        result[column] = (
            "categorical" if threshold * dataset_info.total_count > count else "numeric"
        )
    return result
