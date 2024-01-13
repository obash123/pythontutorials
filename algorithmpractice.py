# write a  fibonacci to specific number of terms 
# write  a program to find the sum of all even fibonnaci numbers 
# enhance the recursvie fib function w memory 

class fibonacci():
    def __init__(self,number):
        self.number = number
        self.home = []

    def fib(self,number):
        if number <= 1:
            return 1
        else:
            return (self.fib(number - 1) + self.fib(number - 2))

    def get_fib(self):
        for i in range(self.number):
            self.home.append(self.fib(i))

    def even(self):
        sum = 0 
        for i in self.home:
            if i % 2 == 0:
                sum += i
        return sum

value = int(input("enter your value: "))
solution = fibonacci(value)

print(solution.fib(value))
solution.get_fib()
print(solution.even())

# def fib_dy(n):
#     if n == 1 or n == 2:
#         return 1
#     up_down = [0] * (n + 1)
#     up_down[1] = 1
#     up_down[2] = 2
#     for i in range(3 , n + 1):
#         up_down[i] = up_down[i - 1] + up_down[i - 2]
#     return up_down[n]
    
# print(fib_dy(100))