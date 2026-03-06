import json
from .models import FeatureFlag
from ..config import Config

FEATURE_FLAGS = {}

def load_feature_flags():
    data = json.loads(Config.FEATURE_FLAGS_JSON or '{}')
    for name, attrs in data.items():
        enabled = bool(attrs.get('enabled', False))
        description = attrs.get('description', '')
        FEATURE_FLAGS[name] = FeatureFlag(name, enabled, description)
