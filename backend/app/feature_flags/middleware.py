from .store import FEATURE_FLAGS
from .models import FeatureFlag

def is_feature_enabled(name: str) -> bool:
    flag = FEATURE_FLAGS.get(name)
    if flag:
        return flag.enabled
    return False
