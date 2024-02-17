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
