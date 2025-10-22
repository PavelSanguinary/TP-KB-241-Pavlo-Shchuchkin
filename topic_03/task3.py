person = {"Ім'я": "Максим", "Вік": 25}
print("Без змін", person)
person.update({"Вік": 26, "Місто": "Київ"})
print("Update: ", person)

print(person.keys())
print(person.values())
print(person.items())
del person["Вік"]
print("del: ", person)
person.clear()
print("clear:", person)