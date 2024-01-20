# class Bank_account():
#     def __init__(self,deposit,withdraw,balance):
#         self.deposit = deposit
#         self.withdraw = withdraw
#         self.balance = balance


account_numbers = {
    '019234859':50,
    "019284784":100,
    "829290029":150
}

class Account:
    def __init__(self, account_number, amount): # this is a constructor . the things inside are parameters or arguments
        self.account_number = account_number
        self.amount = amount


    def credit_account(self,account_number, amount):
        if account_number in account_numbers:
            account_numbers[account_number] += amount
            return account_numbers[account_number]
    
    def debit_account(self,account_number, amount):
        if account_number in account_numbers:
            account_numbers[account_number] -= amount
            return account_numbers[account_number]
        
    def get_account_balance(self,account_number):
        return account_numbers[account_number]
    

bai = Account("account_number","amount")

print(bai.credit_account("019234859",400))

print(bai.debit_account("829290029",100))

print(bai.get_account_balance(input("Enter your account number: ")))


# print("My total balance for credit account is: ", str(credit))
# print("My total balance for debit account is: ", str(debit))
# print("The account balance is ", str(a_balance))