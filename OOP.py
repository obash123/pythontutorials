# class TemperatureConverter:
#     KEVIN = 'K',
#     FAHRENHEIT = 'F'
#     CELSIUS = 'C'

#     @staticmethod
#     def celsius_to_fahrenheit(c):
#         return 9*c/5 + 32

#     @staticmethod
#     def fahrenheit_to_celsius(f):
#         return 5*(f-32)/9

#     @staticmethod
#     def celsius_to_kelvin(c):
#         return c + 273.15

#     @staticmethod
#     def kelvin_to_celsius(k):
#         return k - 273.15

#     @staticmethod
#     def fahrenheit_to_kelvin(f):
#         return 5*(f+459.67)/9

#     @staticmethod
#     def kelvin_to_fahrenheit(k):
#         return 9*k/5 - 459.67

#     @staticmethod
#     def format(value, unit):
#         symbol = ''
#         if unit == TemperatureConverter.FAHRENHEIT:
#             symbol = '°F'
#         elif unit == TemperatureConverter.CELSIUS:
#             symbol = '°C'
#         elif unit == TemperatureConverter.KEVIN:
#             symbol = '°K'

#         return f'{value}{symbol}'

# f = TemperatureConverter.fahrenheit_to_celsius(100)
# # print(TemperatureConverter.format(f, TemperatureConverter.CELSIUS))

# '''
# Use static methods to define utility methods or group a logically 
# related functions into a class.
# '''




# # To define an abstract method, you use the @abstractmethod decorator:
# from abc import ABC, abstractmethod


# class AbstractClassName(ABC):
#     @abstractmethod
#     def abstract_method_name(self):
#         pass

# # The following defines the Employee abstract class:
# from abc import ABC, abstractmethod


# class Employee(ABC):
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name

#     @property
#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"

#     @abstractmethod
#     def get_salary(self):
#         pass

# # emp = Employee("Gbemileke", "Osinaike")
# # emp.full_name

# # The following illustrates the FulltimeEmployee class:
# class FulltimeEmployee(Employee):
#     def __init__(self, first_name, last_name, salary):
#         super().__init__(first_name, last_name)
#         self.salary = salary

#     def get_salary(self):
#         return self.salary

# # The following shows the HourlyEmployee class:
# class HourlyEmployee(Employee):
#     def __init__(self, first_name, last_name, worked_hours, rate):
#         super().__init__(first_name, last_name)
#         self.worked_hours = worked_hours
#         self.rate = rate

#     def get_salary(self):
#         return self.worked_hours * self.rate

# '''
# Since fulltime and hourly employees share the same interfaces
# (full_name property and get_salary() method). 
# Therefore, the Payroll class doesn’t need to distinguish them.'''

# class Payroll:
#     def __init__(self):
#         self.employee_list = []

#     def add(self, employee):
#         self.employee_list.append(employee)

#     def print(self):
#         for e in self.employee_list:
#             print(f"{e.full_name} \t ${e.get_salary()}")

# '''
# The following app.py uses the FulltimeEmployee,
# HourlyEmployee, and Payroll classes to print 
# out the payroll of five employees.
# '''

# # from fulltimeemployee import FulltimeEmployee
# # from hourlyemployee import HourlyEmployee
# # from payroll import Payroll

# payroll = Payroll()

# payroll.add(FulltimeEmployee('John', 'Doe', 6000))
# payroll.add(FulltimeEmployee('Jane', 'Doe', 6500))
# payroll.add(HourlyEmployee('Jenifer', 'Smith', 200, 50))
# payroll.add(HourlyEmployee('David', 'Wilson', 150, 100))
# payroll.add(HourlyEmployee('Kevin', 'Miller', 100, 150))

# # payroll.print()

# # When to use abstract classes
# # In practice, you use abstract classes to share the code 
# # among several closely related classes. 
# # In the payroll program, all subclasses of the Employee class 
# # share the same full_name property.

# # Abstract classes are classes that you cannot create instances from.

# class Counter:
#     def __init__(self):
#         self.__current = 0

#     def increment(self):
#         self.__current += 1

#     def value(self):
#         return self.__current

#     def reset(self):
#         self.__current = 0

# counter = Counter()
# counter.__current = 5
# print(counter.value())

# class Counter:
#     def __init__(self):
#         self.__current = 0

#     def increment(self):
#         self.__current += 1

#     def value(self):
#         return self.__current

#     def reset(self):
#         self.__current = 0


# counter = Counter()
# counter.__current = 5
# # print(counter.__current)
# print(counter.value())


# # Encapsulation
# class BankAccount:
#     def __init__(self, balance=0):
#         self._balance = balance

#     @property
#     def balance(self):
#         return self._balance

#     # @balance.setter
#     def set_balance(self, value):
#         if value < 0:
#             raise ValueError("Balance cannot be negative")
#         self._balance = value

#     def deposit(self, amount):
#         self._balance += amount

#     def withdraw(self, amount):
#         if amount > self._balance:
#             raise ValueError("Insufficient balance")
#         self._balance -= amount

# my_account = BankAccount(100)
# print(my_account.balance)
# my_account.deposit(50)
# print(my_account.balance)
# my_account.withdraw(30)
# my_account.set_balance(30)
# my_account.balance
# print(my_account.balance)


# # Encapsulation

# class Payment:
#     def __init__(self, price):
#         self.__final_price = price + (price * 0.05)
        
#     @property
#     def final_price(self):
#         return self.__final_price
    
#     def set_final_price(self, discount):
#         if __name__ == '__main__':
#             self.__final_price -= self.__calculate_discount(discount)
        
#     def __calculate_discount(self, discount):
#         return self.__final_price * (discount/100)
    
# book = Payment(100)
# print(book.final_price)
# book.set_final_price(5)
# print(book.final_price)
# # book.__final_price


# # Polymorphism
# # the ability of objects of different classes to be treated as if they were of the same class
# class French:
#     def say_hello(self):
#         print ('Bonjour')
        
# class Yoruba:
#     def say_hello(self):
#         print ("Bawo ni")
        
# def intro(language):
#     return language.say_hello()

# leke = Yoruba()
# Obasola = French()

# intro(leke)
# intro(Obasola)


# # Decorator

# def operation(opt_type):
#     def add(n1, n2):
#         return n1 + n2
    
#     def sub(n1, n2):
#         return n1 - n2
    
#     if opt_type == 'add':
#         return add
    
#     if opt_type == 'sub':
#         return sub
    
# subtract = operation('sub')
# addition = operation('add')
# print(subtract(5,3))
# print(addition(5,3))


# class A:
#     def __init__(self, height):
#         self.height = height
    
# class B(A):
#     def __init__(self, length, breadth, height):
#         self.length = length
#         self.breadth = breadth
#         super().__init__(height)
        
        
# class Apple(ABC):
#     @abstractmethod
#     def security(self):
#         pass
    
#     @abstractmethod
#     def speed(self):
#         pass
    
# class IPhone(Apple):
#     def __init__(self) -> None:
#         super().__init__()
    
#     def speed(self):
#         print("Iphone speed is more faster.")
        
#     def security(self):
#         print("Iphone security is efficient.")
        
# class Ipod(Apple):
#     def __init__(self):
#         super().__init__()
    
#     def speed(self):
#         print("Ipod speed is more faster.")
        
#     def security(self):
#         print("Ipod security is efficient.")
        
# phone = IPhone()
# media_device = Ipod()

# class Bank:
#     def __init__(self):
#         self.__balance = 0
        
#     def credit_balance(self, amount):
#         self.__balance += amount
        
#     def get_balance(self):
#         return self.__balance
    
# bank = Bank()
# bank.__balance = 10000
# print (bank.get_balance())
# bank.credit_balance(200)
# print(bank.get_balance())



# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Drive!")

# class Boat:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Sail!")

# class Plane:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Fly!")

# car1 = Car("Ford", "Mustang")       #Create a Car class
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
# plane1 = Plane("Boeing", "747")     #Create a Plane class

# for x in (car1, boat1, plane1):
#   x.move()

'''
Problem Statement:

Design a class called BankAccount that represents a bank account.
The class should have the following properties:

Account holder's name (private)
Account number (private)
Balance (private)
The class should have the following methods:

_init_: Initialize the account holder's name, account number, and balance
deposit: Adds the given amount to the balance
withdraw: Subtracts the given amount from the balance, if sufficient balance is available. 
If not, it should print an error message.
get_balance: Returns the current balance
get_account_number: Returns the account number
set_account_number: Sets the account number
get_account_holder_name: Returns the account holder's name

set_account_holder_name: Sets the account holder's name

Additionally, the class should implement abstraction and encapsulation so that the user cannot directly access the 
private properties and can only access them through the methods.
'''


# Encapsulation
class BankAccount:
    def __init__(self, name, account_num, balance=0):
        self.__balance = balance
        self.__name = name 
        self.__account_num = account_num

    @property
    def balance(self):
        return self.__balance

    # @balance.setter
    def set_balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = value

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient balance")
        self.__balance -= amount

    @property
    def get_balance(self):
        return self.__balance 

    @property
    def get_account_number(self):
        return self.__account_num
    
    def set_account_number(self,acc_num):
        if acc_num < 0 or len(str(acc_num)) != 10:
            raise ValueError("enter a valid account number")
        self.__account_num = acc_num

    @property
    def get_account_holder_name(self):
        return self.__name
    
    def set_account_holder_name(self,holder_name):
        self.__name = holder_name    


my_account = BankAccount("james Obaloluwa",10393845058,100)
print(my_account.balance)
my_account.deposit(50)
print(my_account.balance)
my_account.withdraw(30)
my_account.set_balance(30)
my_account.balance
print(my_account.balance)
print(my_account.get_balance)
print(my_account.get_account_number)
my_account.set_account_number(9749576956)
print(my_account.get_account_number)
print(my_account.get_account_holder_name)
my_account.set_account_holder_name("obasola")
print(my_account.get_account_holder_name)
