class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. Balance: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return f"Withdrew {amount}. Balance: {self.balance}"

account = BankAccount("Nikhil", 1000)
print(account.deposit(500))
print(account.withdraw(200))
print(account.withdraw(2000))
