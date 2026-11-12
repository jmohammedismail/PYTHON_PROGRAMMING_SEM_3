# MODULE 4 - LAB 2
# Student Data Manager Using Files
# Options: add a student, display all students, and exit.
# Each record is stored in students.txt as Roll Number, Name, Marks.

FILE_NAME = "students.txt"


def add_student():
    try:
        roll = int(input("Enter Roll Number: "))
        if roll <= 0:
            raise ValueError
    except ValueError:
        print("Invalid Roll Number! Enter a positive whole number.")
        return

    try:
        name = input("Enter Student Name: ").strip()
        if not name or not all(part.isalpha() for part in name.split()):
            raise ValueError
    except ValueError:
        print("Invalid Student Name! Use alphabets and spaces only.")
        return

    try:
        marks = float(input("Enter Marks: "))
        if not 0 <= marks <= 100:
            raise ValueError
    except ValueError:
        print("Invalid Marks! Enter a value between 0 and 100.")
        return

    try:
        with open(FILE_NAME, "a", encoding="utf-8") as file:
            file.write(f"{roll},{name},{marks:g}\n")
        print("Student added successfully!")
    except OSError as error:
        print("Error while saving student details:", error)


def display_students():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            records = file.readlines()

        if not records:
            print("No student records found.")
            return

        print("\n----- STUDENT RECORDS -----")
        for record in records:
            try:
                roll, name, marks = record.strip().split(",", 2)
                print("Roll Number:", roll)
                print("Name:", name)
                print("Marks:", marks)
                print("---------------------------")
            except ValueError:
                print("Skipping invalid student record:", record.strip())

    except FileNotFoundError:
        print("No student records found. Add a student first.")
    except OSError as error:
        print("Error while reading student records:", error)


def main():
    while True:
        print("\n===== STUDENT DATA MANAGER =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice! Enter 1, 2 or 3.")
            continue

        if choice == 1:
            add_student()
        elif choice == 2:
            display_students()
        elif choice == 3:
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Select 1, 2 or 3.")


if __name__ == "__main__":
    main()
