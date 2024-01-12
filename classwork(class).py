from homework2 import Account

class Savings(Account):
    def __init__(self, account_number, amount,interest_rate):
        super().__init__(account_number, amount)
        self.interest_rate = interest_rate

    def add_interest(self):
        return self.get_account_balance(self.account_number) * self.interest_rate 
    

class Checking(Account):
    def __init__(self, account_number, amount):
        super().__init__(account_number, amount)

    def account_balance(self):
        return self.get_account_balance(self.account_number)
    

save = Savings("019284784",500,0.5)
print(save.add_interest())

check = Checking("019284784",150)
print(check.account_balance())