account_numbers = {
    '019234859':50,
    "019284784":100,
    "829290029":150
}

class Account:
    def __init__(self, account_number, amount):
        self.account_number = account_number
        self.amount = amount
        
    def credit_account(self):
        if self.account_number in account_numbers:
            account_numbers[self.account_number] += self.amount
            return account_numbers[self.account_number]
    
    def debit_account(self):
        if self.account_number in account_numbers:
            account_numbers[self.account_number] -= self.amount
            return account_numbers[self.account_number]
        
    def __str__(self):
        return self.account_number

acc = input("enter the account number: ")
num = int(input("entert the amount : "))
emmanuel_account = Account(acc, num)   
print ("the account balance is currently: ",emmanuel_account.credit_account())




# write a car class that accelerates, decelerates and apply brakes.
#class

# class Car:
#     def __init__(self, final_velocity):
#         self.initial_velocity = 0
#         self.final_velocity = final_velocity
#         self.velocity = 0

#     def accelerate(self):
#         self.velocity = (self.final_velocity + self.initial_velocity)
#         return "the car accelerated" + str(self.velocity) 
    
#     def deccelerate(self):
#         self.velocity -= self.final_velocity
#         return self.velocity
    
#     def brake(self):
#         self.velocity = 0
#         return self.velocity
    
# sport_car = Car(300)
# print(sport_car.accelerate())




# write a class that creates cgpa and work on the practice exam question 1


    





