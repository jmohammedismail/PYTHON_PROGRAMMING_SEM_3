"""Bank Account Management System using Object-Oriented Programming."""

class BankAccount:
    def __init__(self, account_holder, account_number, opening_balance=0.0):
        if opening_balance < 0:
            raise ValueError("Opening balance cannot be negative.")
        self.account_holder = account_holder
        self.account_number = account_number
        self.__balance = float(opening_balance)

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return
        self.__balance += amount
        print(f"Successfully deposited Rs. {amount:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"Successfully withdrawn Rs. {amount:.2f}")

    def display_details(self):
        print("\n----- ACCOUNT DETAILS -----")
        print(f"Account Holder : {self.account_holder}")
        print(f"Account Number : {self.account_number}")
        print(f"Available Balance : Rs. {self.__balance:.2f}")


def main():
    print("===== BANK ACCOUNT MANAGEMENT SYSTEM =====")
    name = input("Enter account holder name: ").strip()
    number = input("Enter account number: ").strip()
    account = BankAccount(name, number)

    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Display Account\n4. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            try:
                account.deposit(float(input("Enter deposit amount: Rs. ")))
            except ValueError:
                print("Please enter a valid amount.")
        elif choice == "2":
            try:
                account.withdraw(float(input("Enter withdrawal amount: Rs. ")))
            except ValueError:
                print("Please enter a valid amount.")
        elif choice == "3":
            account.display_details()
        elif choice == "4":
            print("Thank you for using our banking system.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
