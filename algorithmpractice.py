# def factorial(num):
#     if num == 1:
#         return 1
#     else:
#         return(num * factorial(num - 1))

# print(factorial(10))

# def factorial_calc(num):
#     result = 1    
#     for i in range(1, num + 1):
#         result *= i
#     return result

# print(factorial_calc(1000))

# def fib(n):
#     if n <= 1:
#         return 1
#     else:
#         return(fib(n -1)+ fib(n - 2))

# n = int(input("enter your number: "))
# print("fibonacci sequence: ")
# for i in range(n):
#     print(fib(i), end = " ")

def fib_dy(num):
    if num == 1 or num == 2:
        return 1
    ans = [0] * (num + 1)
    ans[1] = 1
    ans[2] = 0
    for i in range(3, num + 1):
        ans[i] =  ans[i - 1] + ans[i - 2]
    return ans[num]
print(fib_dy(1000))


