import json
import os

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.data_file = "Data_customers.json"
        self.load_data()

    def load_data(self):
        # Load existing data if the file exists
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as file:
                data = json.load(file)
        else:
            data = {}

        # If the customer exists, load their balance
        if self.name in data:
            self.balance = data[self.name]["balance"]

    def save_data(self):
        # Load existing data
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as file:
                data = json.load(file)
        else:
            data = {}

        # Update or add the customer's data
        data[self.name] = {
            "name": self.name,
            "balance": self.balance
        }

        # Write updated data back to the file
        with open(self.data_file, "w") as file:
            json.dump(data, file, indent=4)

    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        self.balance += amount
        print(f'Deposited {amount}. New balance: {self.balance}')
        self.save_data()

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if amount > self.balance:
            print('Insufficient funds')
        else:
            self.balance -= amount
            print(f'Withdrew {amount}. New balance: {self.balance}')
            self.save_data()

    def check_balance(self):
        print(f'Current balance for {self.name}: {self.balance}')


print("Welcome To My BanckAccount")
name = input("Enter customer name: ")
initial_balance = float(input("Enter your balance: "))
account = BankAccount(name, initial_balance)

while True:
    action = input("Choose an action: deposit, withdraw, check, or exit: ").strip().lower()
    if action == 'deposit':
        account.deposit()
    elif action == 'withdraw':
        account.withdraw()
    elif action == 'check':
        account.check_balance()
    elif action == 'exit':
        print("Good Bye!")
        break
    else:
        print("Invalid action. Please choose deposit, withdraw, check, or exit.")
