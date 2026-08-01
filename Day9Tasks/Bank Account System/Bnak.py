class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(amount, "deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(amount, "withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print("Account Number:", self.account_number)
        print("Current Balance:", self.balance)


account1 = BankAccount(123456, 5000)

account1.deposit(2000)
account1.withdraw(1000)
account1.display_balance()