from bank_accounts import *

Dave = BankAccount(1000, "Dave")
Jenny = BankAccount(3000, "Jenny")

Dave.getBalance()
Jenny.getBalance()

Jenny.deposit(505)

# withdraw Balance Exception for account Dave
Dave.withdraw(1001)
Dave.withdraw(200)

# transfer Balance Exception
Dave.transfer(1000, Jenny)
Dave.transfer(50, Jenny)

# Interest reward account
Jim = InterestRewardsAcct(1000, "Jim")

Jim.getBalance()
Jim.deposit(100) # 5% reward

Jim.transfer(100, Dave)

# Savings account practice
Leon = SavingsAcct(1000, "Leon")
Leon.getBalance()
Leon.deposit(100)

Leon.transfer(10000, Jenny)
Leon.transfer(1000, Jenny)