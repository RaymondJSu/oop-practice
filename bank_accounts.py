class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initAmount, acctName):
        self.balance = initAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' Balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\nDeposite complete.")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return 
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
            )

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interupted. {error}")

    def transfer(self, amount, account):
        try:
            print('\n********\n\nBeginning Transter')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer complete.\n\n********')
        except BalanceException as error:
            print(f'Transfer interrupted. {error}')

### Inheritance, override deposit and withdraw method

class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05) # additional 5%
        print('\nDeposit complete.')
        self.getBalance()

# there will be a $5 fee everytime withdraw money from this account
class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initAmount, acctName):
        super().__init__(initAmount, acctName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print('\nWithdraw complete.')
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')