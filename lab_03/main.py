from Student import Student
from StudentList import StudentList
from FileManager import FileManager

CSV_FILE = "students.csv"

def print_all(student_list: StudentList) -> None:
    students = student_list.all()
    if not students:
        print("List clear.\n")
        return
    for s in students:
        print(f"Name: {s.name}, Phone: {s.phone}, Email: {s.email}, Address: {s.address}")
    print()

def main():
    fm = FileManager(CSV_FILE)
    student_list = fm.load()
    print(f"Load {CSV_FILE}: {len(student_list)}")
    while True:
        try:
            choice = input("Please specify the action [C create, U update, D delete, P print, S save, X exit]: ").strip().lower()
        except EOFError:
            print("Exiting...")
            fm.save(student_list)
            break
        if choice == "c":
            name = input("Enter student name: ").strip()
            phone = input("Enter student phone: ").strip()
            email = input("Enter student email: ").strip()
            address = input("Enter student address: ").strip()
            student_list.add(Student(name=name, phone=phone, email=email, address=address))
            print("New student has been added.")
            fm.save(student_list)
        elif choice == "u":
            name = input("Enter name to update: ").strip()
            phone = input("Enter new phone: ").strip()
            email = input("Enter new email: ").strip()
            address = input("Enter new address: ").strip()
            if student_list.update_by_name(name, phone, email, address):
                print("Student data has been updated.")
                fm.save(student_list)
            else:
                print("Student not found.")
        elif choice == "d":
            name = input("Enter name to delete: ").strip()
            if student_list.delete_by_name(name):
                print("Student has been deleted.")
                fm.save(student_list)
            else:
                print("Student not found.")
        elif choice == "p":
            print_all(student_list)
        elif choice == "s":
            fm.save(student_list)
            print(f"Count save: {CSV_FILE}: {len(student_list)}")
        elif choice == "x":
            print("Exiting...")
            fm.save(student_list)
            break
        else:
            print("Wrong choice, please try again.")

if __name__ == "__main__":
    main()
