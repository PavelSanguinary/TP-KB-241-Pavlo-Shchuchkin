import locale

students = [
    {"name": "Іван", "grade": 10},
    {"name": "Оля", "grade": 6},
    {"name": "Андрій", "grade": 8},
    {"name": "Микола", "grade": 12},
]
print("Початковий список:")
print(students)
locale.setlocale(locale.LC_COLLATE, "uk_UA.UTF-8")
sorted_name = sorted(students, key=lambda x: locale.strxfrm(x["name"]))
sorted_grade = sorted(students, key=lambda x: x["grade"])
print("\nВідсортовано за ім’ям:")
print(sorted_name)
print("\nВідсортовано за оцінкою:")
print(sorted_grade)