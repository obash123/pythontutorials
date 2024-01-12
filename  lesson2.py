# # I have a restuarant and there are lists of food items all having their prices
# # write a program to be able to give me the price of each of the food items I select 


# restaurant = {
#     "soup":"afang",
#     "drink":"caprisonne",
#     "starters":"yam",
#     "main":"egusi",
#     "dessert":"dodo"

# }

# print(restaurant)

# food = input("what would you like to get: ")

# if food not in restaurant:
#     print("it's not available")
# else:
#     print(restaurant[food])

# # Challenge 2: Iterate through every number in a list to separate out even and odd numbers. 
# # Identify possible outlier values as well.


# list1 = ["dog", "cat", "hat", 2,6,7,3,88,90,55,77,65,80]

# for i in list1:
#     if type(i) is int:

#         if i % 2 == 0:
#             print("even number: ",i)
#         elif i % 2 !=0:
#             print("odd number: ",i)
#     else:
#         print("the outliers are",i)

# challenge 3 functions
        
account_numbers = {
    '019234859':50,
    "019284784":100,
    "829290029":150
}


def credit_account(account_number, amount):
    if account_number in account_numbers:
        account_numbers[account_number] += amount
        return account_numbers[account_number]
    
def debit_account(account_number, amount):
    if account_number in account_numbers:
        account_numbers[account_number] -= amount
        return account_numbers[account_number]
    
def get_account_balance(account_number):
    return account_numbers[account_number]
    

credit = (credit_account("019234859", 400))
debit = (debit_account("829290029",100))
a_balance = (get_account_balance(input("Enter your account number: ")))

print("My total balance is ", str(credit))
print("My total balance is ", str(debit))
print("The account balance is ", str(a_balance))