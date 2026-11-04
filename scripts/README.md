# Dataset

From the `scripts/` directory, download the GitSkills parquet tables into `./dataset`.

```bash
hf download mvaccargiu/gitskills --repo-type dataset \
  --include "data/artifacts/**" \
  --include "data/artifact_siblings/**" \
  --include "data/repos/**" \
  --include "data/mining_runs/**" \
  --local-dir ./dataset
```

The Hub nests those tables under `data/`, so the command writes `./dataset/data/{artifacts,artifact_siblings,repos,mining_runs}/`. Flatten once so the paths in `tool_extraction.py` match.

```bash
mv ./dataset/data/* ./dataset/ && rmdir ./dataset/data
```

Those paths are `./dataset/artifacts/*.parquet`, `./dataset/artifact_siblings/*.parquet`, `./dataset/repos/part-00000.parquet`, and `./dataset/mining_runs/part-00000.parquet`.

Leave `./dataset/.gitkeep` in place. Parquet under `scripts/dataset/` is gitignored. Notebooks in this folder are run from `scripts/` so those relative paths resolve.
