import os

import argilla as rg
from dotenv import load_dotenv

load_dotenv()

client = rg.Argilla(
    api_url=os.getenv("ARGILLA_API_URL"),
    api_key=os.getenv("ARGILLA_API_KEY"),
)

workspace = client.workspaces("default")
