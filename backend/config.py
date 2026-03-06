import os, json
# Load FEATURE_FLAGS from env var as JSON; fallback to empty dict
FEATURE_FLAGS = {}
if os.getenv('FEATURE_FLAGS'):
    try:
        FEATURE_FLAGS = json.loads(os.getenv('FEATURE_FLAGS'))
    except json.JSONDecodeError:
        FEATURE_FLAGS = {}
