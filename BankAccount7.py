class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.name = name  # Protected attribute

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} into account {self.account_number}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.account_number}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return f"{self.balance} Baht"
    
    def transfer(self, recipient_account, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            recipient_account.deposit(amount)
            print(f"Transferred {amount} from account {self.account_number} to account {recipient_account.account_number}")
        else:
            print("Transfer failed: invalid amount")


class SavingsAccount(Account):
    def __init__(self, account_number, balance=0, name="", account_type="", interest_rate=0.01):
        super().__init__(account_number, balance)
        self.name = name
        self.account_type = account_type
        self.interest_rate = interest_rate

    def add_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.deposit(interest_amount)


class FixedDeposit(Account):
    def __init__(self, account_number, balance=0, name="", account_type="", interest_rate=0.05, term=12):
        super().__init__(account_number, balance)
        self.name = name
        self.account_type = account_type
        self.interest_rate = interest_rate
        self.term = term

    def add_interest(self):
        interest_amount = self.balance * self.interest_rate * (self.term / 12)
        self.deposit(interest_amount)


# Example usage:
if __name__ == "__main__":
    # Creating savings account
    savings_acc = SavingsAccount("Elon Musk", name="Elon Musk", account_type="savings", balance=1000)
    savings_acc.deposit(5000000) 
    print("Savings account balance:", savings_acc.get_balance())
    savings_acc.add_interest()
    print("After interest, savings account balance:", savings_acc.get_balance())

    # Creating fixed deposit account
    fixed_acc = FixedDeposit("Mr.BooK", name="Mr.BooK", account_type="fixed deposit", balance=2000)
    fixed_acc.deposit(2000)
    print("Fixed deposit account balance:", fixed_acc.get_balance())
    fixed_acc.add_interest()
    print("After interest, fixed deposit account balance:", fixed_acc.get_balance())

    # Transferring funds from savings account to fixed deposit account
    savings_acc.transfer(fixed_acc, 500000)
    print("Savings account balance after transfer:", savings_acc.get_balance())
    print("Fixed deposit account balance after transfer:", fixed_acc.get_balance())