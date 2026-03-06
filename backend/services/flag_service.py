from typing import List
from ..models.feature_flag import FeatureFlag

class FlagService:
    def __init__(self, store: dict):
        self.store = store

    def list_flags(self) -> List[FeatureFlag]:
        return [FeatureFlag(name=k, enabled=v.get('enabled', False), description=v.get('description'))
                for k, v in self.store.items()]

    def get_flag(self, name: str) -> FeatureFlag:
        if name not in self.store:
            raise KeyError(name)
        data = self.store[name]
        return FeatureFlag(name=name, enabled=data.get('enabled', False), description=data.get('description'))

    def set_flag(self, name: str, enabled: bool, description: str = None) -> FeatureFlag:
        self.store[name] = {'enabled': enabled, 'description': description}
        return FeatureFlag(name=name, enabled=enabled, description=description)
