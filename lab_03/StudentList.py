from __future__ import annotations
from typing import List, Optional
from Student import Student

class StudentList:
    def __init__(self, students: Optional[List[Student]] = None):
        self._students: List[Student] = sorted(students or [], key=lambda s: s.name.lower())

    def all(self) -> List[Student]:
        return list(self._students)

    def add(self, student: Student) -> None:
        self._students.append(student)
        self._students.sort(key=lambda s: s.name.lower())

    def find_by_name(self, name: str) -> Optional[Student]:
        name_l = name.strip().lower()
        for s in self._students:
            if s.name.lower() == name_l:
                return s
        return None

    def delete_by_name(self, name: str) -> bool:
        name_l = name.strip().lower()
        for i, s in enumerate(self._students):
            if s.name.lower() == name_l:
                del self._students[i]
                return True
        return False

    def update_by_name(self, name: str, phone: str, email: str, address: str) -> bool:
        s = self.find_by_name(name)
        if not s:
            return False
        s.update(phone=phone, email=email, address=address)
        return True

    def __len__(self) -> int:
        return len(self._students)
