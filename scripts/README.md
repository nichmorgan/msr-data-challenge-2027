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

# Argilla

Manual validation uses Argilla. You need a running Argilla server, an API key, the parquet tables under `./dataset`, and the `scripts/` uv env (`uv sync`).

Copy the secret templates, then fill them in. Do not commit either file.

```bash
cp .env.example .env
cp argilla_users.example.json argilla_users.json
```

`.env` holds `ARGILLA_API_URL`, `ARGILLA_API_KEY`, `HF_TOKEN`, and `HF_DATASET_ID`. `argilla_users.json` holds annotator accounts. Secrets in `.env` are gitignored.

# Hugging Face (processed outputs)

Public derivative dataset: [`nichmorgan/gitskills-msr27`](https://huggingface.co/datasets/nichmorgan/gitskills-msr27) (not the official raw [`mvaccargiu/gitskills`](https://huggingface.co/datasets/mvaccargiu/gitskills) dump).

Push or update that Hub dataset from Argilla, not with a local `hf upload`. Paste `HF_TOKEN` and `HF_DATASET_ID` from `.env` into Argilla’s Hub fields. Keep a write-capable token at https://huggingface.co/settings/tokens if you need to rotate one.

Run the notebooks from `scripts/` so `tool_extraction` and `./dataset` resolve:

1. `argilla_users.ipynb` — create users from `argilla_users.json` and add them to workspace `default`
2. `argilla_dataset.ipynb` — delete dataset `skills` if it exists, recreate it, and log a 5000-row sample (`SEED` from `tool_extraction.py`)

`argilla_client.py` loads the env vars and connects to workspace `default`.

Schema on dataset `skills`:

- `included` — `yes`, `not_plain_text`, `not_english`, `not_skill`, or `not_tool`
- `mentions` — spans on `content` with labels `tool`, `publisher`, or `repository`
- `manual_details` — one line per marked tool still missing a publisher or repository: `tool | publisher | repository`. Omit the tool name to bind by mark order. Leave a field empty when it is already marked. Repository is a full https project URL, or `none`. Leave the answer blank when every value is marked, or when included is not yes.

Changing settings or the sample requires re-running `argilla_dataset.ipynb`. That notebook deletes `skills` before recreating it.
