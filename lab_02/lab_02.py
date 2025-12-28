import csv
students_list = [
    {"name": "Bob", "phone": "0631234567", "email": "bob@example.com", "address": "Street 123"},
    {"name": "Emma", "phone": "0631234567", "email": "emma@example.com", "address": "Street 456"},
    {"name": "Jon", "phone": "0631234567", "email": "jon@example.com", "address": "Street 789"},
    {"name": "Zak", "phone": "0631234567", "email": "zak@example.com", "address": "Street 101"}
]

CSV_FILE = "students.csv"

def loadcsv(filename, students):
    try:
        with open(filename, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            loaded = []
            for row in reader:
                name = (row.get("name") or row.get("Name") or "").strip()
                phone = (row.get("phone") or row.get("Phone") or "").strip()
                email = (row.get("email") or row.get("Email") or "").strip()
                address = (row.get("address") or row.get("Address") or "").strip()
                loaded.append({"name": name, "phone": phone, "email": email, "address": address})

        loaded.sort(key=lambda s: s["name"].lower())
        students.clear()
        students.extend(loaded)
        print(f"Load {filename}: {len(students)}")
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"Error in {filename}: {e}")

def savecsv(filename, students):
    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["name", "phone", "email", "address"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for s in students:
                writer.writerow({
                    "name": s.get("name", ""),
                    "phone": s.get("phone", ""),
                    "email": s.get("email", ""),
                    "address": s.get("address", "")
                })
        print(f"Count save: {filename}: {len(students)}")
    except Exception as e:
        print(f"Error save {filename}: {e}")

def printAllList():
    if not students_list:
        print("List clear.\n")
        return
    for student in students_list:
        print(
            f"Name: {student['name']}, "
            f"Phone: {student['phone']}, "
            f"Email: {student['email']}, "
            f"Address: {student['address']}"
        )
    print()

def addNewElement():
    name = input("Enter student name: ").strip()
    phone = input("Enter student phone: ").strip()
    email = input("Enter student email: ").strip()
    address = input("Enter student address: ").strip()

    new_student = {"name": name, "phone": phone, "email": email, "address": address}

    insert_position = 0
    for student in students_list:
        if name.lower() > student["name"].lower():
            insert_position += 1
        else:
            break

    students_list.insert(insert_position, new_student)
    print("New student has been added.")
    savecsv(CSV_FILE, students_list)
    printAllList()

def deleteElement():
    name = input("Enter name to delete: ").strip()
    delete_position = -1

    for i, student in enumerate(students_list):
        if student["name"].lower() == name.lower():
            delete_position = i
            break

    if delete_position == -1:
        print("Student not found.")
    else:
        deleted_name = students_list[delete_position]["name"]
        del students_list[delete_position]
        print(f"Student {deleted_name} has been deleted.")
        savecsv(CSV_FILE, students_list)

    printAllList()

def updateElement():
    name = input("Enter name to update: ").strip()
    student_found = False

    for student in students_list:
        if student["name"].lower() == name.lower():
            student_found = True
            student["phone"] = input(f"Enter new phone for {student['name']}: ").strip()
            student["email"] = input(f"Enter new email for {student['name']}: ").strip()
            student["address"] = input(f"Enter new address for {student['name']}: ").strip()
            break
    if not student_found:
        print("Student not found.")
    else:
        print(f"Student {name}'s data has been updated.")
        savecsv(CSV_FILE, students_list)

    printAllList()

def main():
    loadcsv(CSV_FILE, students_list)

    while True:
        try:
            choice = input("Please specify the action [C create, U update, D delete, P print, S save, X exit]: ").strip().lower()
        except EOFError:
            print("Exiting...")
            savecsv(CSV_FILE, students_list)
            break

        if choice == "c":
            addNewElement()
        elif choice == "u":
            updateElement()
        elif choice == "d":
            deleteElement()
        elif choice == "p":
            printAllList()
        elif choice == "s":
            savecsv(CSV_FILE, students_list)
        elif choice == "x":
            print("Exiting...")
            savecsv(CSV_FILE, students_list)
            break
        else:
            print("Wrong choice, please try again.")

main()
