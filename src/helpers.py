import os
import json

def load_config(path="config.json"):
    with open(path) as f:
        return json.load(f)

def get_env(key, default=None):
    return os.environ.get(key, default)
