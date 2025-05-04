class BankAccount:
    def __init__(self, name, initial_balance = 0):
        self.name = name
        self.balance = initial_balance
    
    def get_menu(self):
        return """
        1 Deposit
        2 Withdraw
        """
    
    def get_name(self):
        return self.name

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return self.balance