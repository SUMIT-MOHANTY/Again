from typing import List, Dict, Any

class MockPostgres:
    def __init__(self):
        self._data: List[Dict[str, Any]] = []

    def fetch_one(self, query: str, *params) -> Dict[str, Any]:
        return self._data[0] if self._data else {}

    def fetch_all(self, query: str, *params) -> List[Dict[str, Any]]:
        return self._data.copy()

    def execute(self, query: str, *params) -> None:
        # Very simple simulation: store params as a dict
        entry = {f"param{i}": p for i, p in enumerate(params)}
        self._data.append(entry)
