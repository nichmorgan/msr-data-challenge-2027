import polars as pl

artifacts = pl.scan_parquet("./dataset/artifacts/*.parquet")
artifact_siblings = pl.scan_parquet("./dataset/artifact_siblings/*.parquet")
repos = pl.scan_parquet("./dataset/repos/part-00000.parquet")
mining_runs = pl.scan_parquet("./dataset/mining_runs/part-00000.parquet")
