import os

class Config:
    FEATURE_FLAGS_JSON = os.getenv('FEATURE_FLAGS_JSON', '{}')
