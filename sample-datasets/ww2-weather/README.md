Dataset Source - Kaggle: https://www.kaggle.com/datasets/smid80/weatherww2

Why use this dataset:
The `Summary of Weather.csv` file in the Weather Conditions in World War Two Kaggle Dataset has hundreds of thousands of records. It is a large dataset and has nine integer or float columns which need to be classified as categorical or numeric. Ideally there is good performance on this dataset.

# Columns to evaluate:
| Column | Classification |
| ------ | -------------- |
| STA | "categorical"|
| YR | "categorical"|
| MO | "categorical"|
| DA | "categorical"|
| TSHDSBRSGF | "categorical"|
| Precip | "numeric"|
| MaxTemp | "numeric"|
| MinTemp | "numeric"|
| MeanTemp | "numeric"|
| Snowfall | "numeric"|
| PRCP | "numeric"|
| MAX | "numeric"|
| MIN | "numeric"|
| MEA | "numeric"|
| SNF | "numeric"|
| SND | "numeric" |

### Modifications:
There are a number of columns with null values or are a repeat of another column in the dataset, these have been removed and are listed below.
Columns Removed: ["PoorWeather", "DR", "SPD", "FT", "FB", "FTI", "ITH", "PGT", "SD3", "RHX", "RHN", "RVG", "WTE"]
