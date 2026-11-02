import os

# cuBLAS reads this when CUDA initializes, so it must be set before any GPU work.
os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG", ":4096:8")

import random

import numpy as np
import polars as pl
import torch

SEED = 42


def set_seed(seed: int) -> None:
    pl.set_random_seed(seed)
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.use_deterministic_algorithms(True, warn_only=True)


set_seed(SEED)

artifacts = pl.scan_parquet("./dataset/artifacts/*.parquet")
artifact_siblings = pl.scan_parquet("./dataset/artifact_siblings/*.parquet")
repos = pl.scan_parquet("./dataset/repos/part-00000.parquet")
mining_runs = pl.scan_parquet("./dataset/mining_runs/part-00000.parquet")
