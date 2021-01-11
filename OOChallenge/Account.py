#For this challenge, create a bank account class that has two attributes:
#    owner
#   balance
#and two methods:
#   deposit
#   withdraw
#As an added requirement, withdrawals may not exceed the available balance.

#Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.


class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    # Adds amount to balance
    def deposit(self, amount):
        self.balance = self.balance + amount
        return "Deposit Accepted"

    # Removes amount from balance
    # if overdrawn return error message
    def withdraw(self, amount):
        if self.balance - amount < 0:
            return "Funds Unavailable!"

        self.balance = self.balance - amount
        return "Withdrawal Accepted"

    def __str__(self):
        return f"Account Owner:   {self.owner} \nAccount balance: ${self.balance}"


if __name__ == '__main__':
    # 1. Instantiate the class
    acct1 = Account('Jose', 100)
    # 2. Print the object
    print(acct1)
    # 3. Show the account owner attribute
    print(acct1.owner)
    # 4. Show the account balance attribute
    print(acct1.balance)
    # 5. Make a series of deposits and withdrawals
    print(acct1.deposit(50))
    print(acct1.withdraw(75))
    # 6. Make a withdrawal that exceeds the available balance
    print(acct1.withdraw(500))
