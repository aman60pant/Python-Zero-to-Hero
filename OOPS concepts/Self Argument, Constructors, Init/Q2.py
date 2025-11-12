# Create a class Account with attributes owner and balance.
# Add methods:
# deposit(amount)               # withdraw(amount)               # display()
# Use self correctly to modify and access instance variables.

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"After Deposit, Now the updated balance is: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        print(f"After Withdrawl, Now the updated balance is: {self.balance}")

    def display(self):
        print(f"Owner: {self.owner} with ammount {self.balance}")


obj = Account("Aman", 3000)
obj.deposit(50)
obj.withdraw(20)
obj.display()