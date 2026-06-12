# n=int(input("enter the number:"))
# for i in range(1,11):
# #  print( n*i, end=" ")

# class and object
class House:
    def __init__(self,color, rooms,):
        self.color=color
        self.rooms=rooms
        
    def describe(self):
        return f"A {self.color} House"   
      
# The Object (Instance)
# OBJECT — An Instance
my_house = House("blue", 3)
your_house = House("red", 5)

# Each object is unique!
print(my_house.color)    # blue
print(your_house.rooms)
        
        # constructor and self
class Dog:
    def __init__(self, name, breed):
        # 'self' = reference to this object
        self.name = name    # instance attr
        self.breed = breed  # instance attr

    def bark(self):
        return f"{self.name}: Woof!"

rex = Dog("Rex", "Husky")
buddy = Dog("Buddy", "Lab")
print(rex.bark())    
print(buddy.bark())

# Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private

    def get_balance(self):       # getter
        return self.__balance

    def deposit(self, amount):   # setter
        if amount > 0:
            self.__balance += amount

acct = BankAccount(1000)
print(acct.get_balance())  # 1000
acct.deposit(500)
print(acct.get_balance())

# inheritance
class vehicle:
    def __init__(self,brand):
        self.brand= brand
    def move(self):
        return f"{self.brand} moves"    
Toyota = vehicle ("Toyota")
print(Toyota.move())

class car(vehicle):
    def __init__(self,brand,doors):
        super().__init__(brand)
        self.doors = doors
car =car("Toyota", 4)
print(car.move())
print(car.doors)        

# polymorphism
class Animal:
    def sound(self):
        return "..."

class Dog(Animal):
    def sound(self):      # Override
        return "Woof!"

class Cat(Animal):
    def sound(self):      # Override
        return "Meow!"

# One interface — many behaviours
for animal in [Dog(), Cat()]:
    print(animal.sound())
    
#    abstraction
    from abc import ABC, abstractmethod

class Shape(ABC):          # Abstract class
    @abstractmethod
    def area(self):       # Contract
        pass              # Must implement!

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r ** 2

c = Circle(5)
print(c.area())           # 78.5

# class and object
class House:
    def __init__(self,color, rooms,):
        self.color=color
        self.rooms=rooms
        
    def describe(self):
        return f"A {self.color} House"   
      
class House:
    def __init__(self, color, rooms):
        self.color = color
        self.rooms = rooms

    def describe(self):
        return f"A {self.color} house"
# The Object (Instance)
# OBJECT — An Instance
my_house = House("blue", 3)
your_house = House("red", 5)

# Each object is unique!
print(my_house.color)    # blue
print(your_house.rooms)
        
        # constructor and self
class Dog:
    def __init__(self, name, breed):
        # 'self' = reference to this object
        self.name = name    # instance attr
        self.breed = breed  # instance attr

    def bark(self):
        return f"{self.name}: Woof!"

rex = Dog("Rex", "Husky")
buddy = Dog("Buddy", "Lab")
print(rex.bark())    
print(buddy.bark())

# Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private

    def get_balance(self):       # getter
        return self.__balance

    def deposit(self, amount):   # setter
        if amount > 0:
            self.__balance += amount

acct = BankAccount(1000)
print(acct.get_balance())  # 1000
acct.deposit(500)
print(acct.get_balance())

# inheritance
class vehicle:
    def __init__(self,brand):
        self.brand= brand
    def move(self):
        return f"{self.brand} moves"    
Toyota = vehicle ("Toyota")
print(Toyota.move())

class car(vehicle):
    def __init__(self,brand,doors):
        super().__init__(brand)
        self.doors = doors
car =car("Toyota", 4)
print(car.move())
print(car.doors)        

# polymorphism
class Animal:
    def sound(self):
        return "..."

class Dog(Animal):
    def sound(self):      # Override
        return "Woof!"

class Cat(Animal):
    def sound(self):      # Override
        return "Meow!"

# One interface — many behaviours
for animal in Dog(), Cat():
    print(animal.sound())
#    abstraction
    from abc import ABC, abstractmethod

class Shape(ABC):         # Abstract class
    @abstractmethod
    def area(self):       # Contract
        pass              # Must implement!

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r ** 2

c = Circle(5)
print(c.area())  

class myclass:
    def say
    

