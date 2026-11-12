# MODULE 4 - LAB 3
# CSV-Based Payroll Management System
# Stores employee details and calculated net salary in payroll.csv.

import csv

FILE_NAME = "payroll.csv"
FIELDS = [
    "Employee ID",
    "Name",
    "Basic Salary",
    "Allowance",
    "Deduction",
    "Net Salary",
]


def add_employees():
    try:
        number = int(input("Enter number of employees: "))
        if number <= 0:
            raise ValueError
    except ValueError:
        print("Invalid number! Enter a positive whole number.")
        return

    for index in range(number):
        print(f"\nEmployee {index + 1}")

        try:
            employee_id = int(input("Enter Employee ID: "))
            if employee_id <= 0:
                raise ValueError
        except ValueError:
            print("Invalid Employee ID! This employee was skipped.")
            continue

        try:
            name = input("Enter Employee Name: ").strip()
            if not name or not all(part.isalpha() for part in name.split()):
                raise ValueError
        except ValueError:
            print("Invalid Employee Name! This employee was skipped.")
            continue

        try:
            basic_salary = float(input("Enter Basic Salary: "))
            allowance = float(input("Enter Allowance: "))
            deduction = float(input("Enter Deduction: "))

            if min(basic_salary, allowance, deduction) < 0:
                raise ValueError
        except ValueError:
            print("Invalid salary details! Use non-negative numbers. Employee skipped.")
            continue

        net_salary = basic_salary + allowance - deduction

        try:
            # Write the heading only when the CSV file is new or empty.
            try:
                with open(FILE_NAME, "r", newline="", encoding="utf-8") as check_file:
                    has_content = check_file.read(1) != ""
            except FileNotFoundError:
                has_content = False

            with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=FIELDS)
                if not has_content:
                    writer.writeheader()

                writer.writerow({
                    "Employee ID": employee_id,
                    "Name": name,
                    "Basic Salary": basic_salary,
                    "Allowance": allowance,
                    "Deduction": deduction,
                    "Net Salary": net_salary,
                })

            print("Employee added successfully!")
            print(f"Net Salary: {net_salary:.2f}")

        except OSError as error:
            print("Error while saving payroll details:", error)


def display_payroll():
    try:
        with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            if not reader.fieldnames:
                print("No payroll records found.")
                return

            print("\n----- EMPLOYEE PAYROLL RECORDS -----")
            found_record = False

            for row in reader:
                found_record = True
                try:
                    print("\nEmployee ID:", row["Employee ID"])
                    print("Name:", row["Name"])
                    print("Basic Salary:", row["Basic Salary"])
                    print("Allowance:", row["Allowance"])
                    print("Deduction:", row["Deduction"])
                    print("Net Salary:", row["Net Salary"])
                    print("------------------------------------")
                except (KeyError, TypeError):
                    print("Invalid employee record found.")

            if not found_record:
                print("No employee records found.")

    except FileNotFoundError:
        print("Payroll file does not exist. Add an employee first.")
    except (OSError, csv.Error) as error:
        print("Error while reading payroll file:", error)


def main():
    while True:
        print("\n===== PAYROLL MANAGEMENT SYSTEM =====")
        print("1. Add Employee")
        print("2. Display Payroll Records")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice! Enter 1, 2 or 3.")
            continue

        if choice == 1:
            add_employees()
        elif choice == 2:
            display_payroll()
        elif choice == 3:
            print("Exiting Payroll Management System...")
            break
        else:
            print("Invalid choice! Select 1, 2 or 3.")


if __name__ == "__main__":
    main()
