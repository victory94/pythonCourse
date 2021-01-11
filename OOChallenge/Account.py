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

    def deposit(self):
        pass

    def withdraw(self):
        pass


if __name__ == '__main__':
    pass