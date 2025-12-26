import locale
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Student(name: {self.name}, age: {self.age})"
students = [
    Student("Вася", 19),
    Student("Ігор", 20),
    Student("Вітя", 17),
    Student("Андрій", 18),
    Student("Сергій", 17)
]
sorted_name = sorted(students, key=lambda student: student.name.lower())
print("Відсортовано за ім'ям:")
for student in sorted_name:
    print(student)
sorted_age = sorted(students, key=lambda student: student.age)
print("\nВідсортовано за віком:")
for student in sorted_age:
    print(student)
