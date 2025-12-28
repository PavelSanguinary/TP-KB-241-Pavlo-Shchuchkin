import csv
from typing import List
from Student import Student
from StudentList import StudentList

class FileManager:
    def __init__(self, filename: str):
        self.filename = filename

    def load(self) -> StudentList:
        try:
            with open(self.filename, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                students: List[Student] = []
                for row in reader:
                    name = (row.get("name") or row.get("Name") or "").strip()
                    phone = (row.get("phone") or row.get("Phone") or "").strip()
                    email = (row.get("email") or row.get("Email") or "").strip()
                    address = (row.get("address") or row.get("Address") or "").strip()
                    if name or phone or email or address:
                        students.append(Student(name=name, phone=phone, email=email, address=address))
                return StudentList(students)
        except FileNotFoundError:
            return StudentList()

    def save(self, student_list: StudentList) -> None:
        with open(self.filename, "w", newline="", encoding="utf-8") as f:
            fieldnames = ["name", "phone", "email", "address"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for s in student_list.all():
                writer.writerow({
                    "name": s.name,
                    "phone": s.phone,
                    "email": s.email,
                    "address": s.address
                })
