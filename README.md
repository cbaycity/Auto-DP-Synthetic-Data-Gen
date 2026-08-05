This is the development doc for the project.

https://github.com/cbaycity/Auto-DP-Synthetic-Data-Gen


# Overview:
This repository exists to help create a differentially private (DP) library that can categorize columns as categorical or numeric for use in DP synthetic data generation. The current approach assumes that schemas are public knowledge, and the issue is to determine if a variable should be discretized and have cuts (bins) created before synthetic data generation - or if it should be treated as categorical and have its keys inferred with an ApproxDP query. This workload is similar to an AutoML's feature type inference challenge.

# Dataset Overview:
The sample datasets were selected from their inclusion in the Towards Feature Type Inference Benchmarking study and subsquent AutoML benchmark [library](https://github.com/vraj-ucsd/ML-Data-Prep-Zoo/blob/master/MLFeatureTypeInference/Benchmark-Labeled-Data/Metadata/meta_data.csv).