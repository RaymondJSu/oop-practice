class BankAccount:
    def __init__(self, initAmount, acctName):
        self.balance = initAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance}:.2f")