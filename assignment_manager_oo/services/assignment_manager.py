
from typing import List, Dict, Optional
import uuid

class AssignmentManager:
    def __init__(self) ->None:
        self.assignment = initial_assignments

    def all(self) -> list[dict]:
        return list(self.assignment)
       

    def add(self, title:str, description:str,
            points:int, assignment_type:str):
        pass
        if not title.strip():
            raise ValueError("Title is required")
        
        allowed_types = ["Homework", "Lab"]
        
        if assignment_type.lower() not in allowed_types:
            raise ValueError("assignment type is invalid")
        
        new_assignment = {
            "id:": str(uuid.uuid4()),
            "title": title,
            "description": description,
            "points": points,
            "assignment_type": assignment_type
        }

        self.assignment.append(new_assignment)
        return new_assignment

    def delete(self, assignment_id:str):
        pass