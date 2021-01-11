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
        pass

    # Removes amount from balance
    def withdraw(self, amount):
        pass


if __name__ == '__main__':
    pass