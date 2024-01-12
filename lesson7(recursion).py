def factorial(num):
    if num == 1: # o(1)
        return 1 # o(1)
    else:       
        return (num * factorial(num - 1)) # o(n)

#print(factorial(100))

def factorial_calc(num):
    result = 1 # o(1)
    for i in range(1,num + 1): # o(n)
        result *= i # o(1)
    return result # o(1)

#print(factorial_calc(100))


# when doing recursion have  a base condition (if else statement)
# recursion is similar to for loops

# ITERATIVE
# def walk(steps):
#     for step in range(1, steps+1): # o(n)
#         print(f"You take step #{step}") # o(1)

# RECURSIVE
def walk(steps):
    if steps == 0: # o(1)
        return 1
    walk(steps - 1)
    print(f"You take step #{steps}")

walk(100)

# recursion = a function that calls itself from within
#                      helps to visualize a complex problem into basic steps
#                      problems can be solved more easily iteratively or recursively
#                      iterative = faster, complex
#                      recursive = slower, simpler

# recursion uses stack (first in last out, last in first out)
# queue (first in first out, last in last out )


def Fib(n):
   if n <= 1:
       return n
   else:
       return (Fib(n - 1) + Fib(n - 2))  # function calling itself(recursion)


n = int(input("Enter the Value of n: "))  # take input from the user
print("Fibonacci series :")
for i in range(n):
   print(Fib(i),end = " ")


fib_series = [0, 1] # 0 and 1 are the initial default values
def fib(n):
    if n<= len(fib_series):
       return fib_series[n-1]

    else:
       next_number = fib(n-1)+fib(n-2)
       fib_series.append(next_number)
       print((next_number),end=' ')
       return next_number

n = int(input("Enter the value of n: "))
print(0, 1, end=" ") #initial default values
fib(3)


# dynamic programming stores frequently used computations during computation
