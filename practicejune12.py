# Q1. 
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

student1 = Student("Lucky", 101)

print("Name:", student1.name, student1.roll_no)

# Q2
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)

car1 = Car("Toyota", "Fortuner")
car1.display()

# Q3
class Employee:
    def __init__(self):
        self.__salary = 30000   # private variable

    def show_salary(self):
        print("Salary =", self.__salary)

    def increase_salary(self, amount):
        self.__salary += amount

emp = Employee()
emp.show_salary()
emp.increase_salary(5000)
emp.show_salary()


from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")

p = CreditCard()
p.pay(1000)

# Q4
from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def work(self):
        pass

class Programmer(Employee):
    def work(self):
        print("Writing code")

class Designer(Employee):
    def work(self):
        print("Designing UI")

p = Programmer()
d = Designer()

p.work()
d.work()

# Q5

from abc import ABC, abstractmethod

class Appliance(ABC):

    @abstractmethod
    def turn_on(self):
        pass

class Fan(Appliance):

    def turn_on(self):
        print("Fan is ON")

f = Fan()
f.turn_on()