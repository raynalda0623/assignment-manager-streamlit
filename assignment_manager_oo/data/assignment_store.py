import json
from pathlib import Path

from typing import List, Dict, Optional

class AssignmentStore:
    def __init__(self, json_path: Path) -> None:
        self.json_path = json_path

    def load(self) -> list[dict]:
        if self.json_path.exists():
            with open(self.json_path, "r") as f:
                return json.load(f) 
        else:
            return [] 

    def save(self, assignments: list[dict]):
        with open(self.json_path, "w") as f:
            json.dump(assignments, f)