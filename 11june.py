class BankAccount:
    def __init__(self, account_number, balance):
        self.__balance = balance
        self.account_number= account_number

    def get_balance(self,amount ):
     if amount>0:
      self._balance+=amount


    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

account = BankAccount(1000)

print(account.get_balance())

account.deposit(500)

print(account.get_balance())


