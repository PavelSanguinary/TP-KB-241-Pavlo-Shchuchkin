from dataclasses import dataclass

@dataclass(order=True)
class Student:
    name: str
    phone: str
    email: str
    address: str

    def update(self, phone: str, email: str, address: str) -> None:
        self.phone = phone
        self.email = email
        self.address = address
