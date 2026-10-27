import polars as pl

artifact_siblings = pl.read_parquet("hf://datasets/mvaccargiu/gitskills/data/artifact_siblings/*.parquet")
artifacts = pl.read_parquet("hf://datasets/mvaccargiu/gitskills/data/artifacts/*.parquet")

test_artifact = pl.read_parquet("hf://datasets/mvaccargiu/gitskills/data/artifacts/part-00000.parquet")
print(test_artifact)
