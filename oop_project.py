from bank_accounts import *

Dave = BankAccount(1000, "Dave")
Jenny = BankAccount(3000, "Jenny")

Dave.getBalance()
Jenny.getBalance()

Jenny.deposit(505)

Dave.withdraw(1001)
Dave.withdraw(200)