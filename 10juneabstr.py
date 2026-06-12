from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    def stop_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self,carname):
        self.carname=carname
        return "Car engine started"
    
    
class Bike(Vehicle):
    def start_engine(self):
        return "Bike engine started"
    
toyota = Car()
print(toyota.start_engine("toyota"),toyota.carname)  # Car engine started
honda = Bike()
print(honda.start_engine()) 
# Bike engine started

class BankAccount:
    def __init__(self, account_number, balance):
        self.__balance = balance
        self.account_number= account_number

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

account = BankAccount(1000)

print(account.get_balance())

account.deposit(500)

print(account.get_balance())
