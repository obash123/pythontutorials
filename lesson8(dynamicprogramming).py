# dynamic programming stores frequently used computations during computation

def fibonacci_n(n): 
    if n <= 1:
        return n
    return fibonacci_n(n - 1) + fibonacci_n(n - 2)

print(fibonacci_n(35))  # Calculate the 10th Fibonacci number

"""
While the recursive approach works, it recalculates the Fibonacci sequence for smaller values repeatedly, 
leading to an exponential increase in redundant calculations. This inefficiency can be addressed using DP.
"""


f_n = {0:0, 1:1}
def fibonacci(n):
    if n in f_n.keys():
        return f_n[n]
    else:
        f_n[n] = fibonacci(n-1) + fibonacci(n-2) # 2n + 1, at most the function is called 2 times
        return f_n[n]
    
print(fibonacci(10))

#bottom up approach
def fib_bottom_up(n):
    if n==1 or n==2:
        return 1
    bottom_up = [0] * (n+1) # defining your stack range
    bottom_up[1] = 1
    bottom_up[2] = 2
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2] # here you are not calling it recursively
    return bottom_up[n]

print(fib_bottom_up(100))
    
"""The bottom-up approach in the Fibonacci example fills up"""

"""The bottom-up approach in the Fibonacci example fills up the fib array iteratively, 
avoiding redundant function calls. It directly computes and stores solutions for smaller subproblems, 
leading to a more efficient use of resources and improved time complexity compared to a recursive or memorization-based approach."""


"""
The Euclidean algorithm is a method for finding the greatest common divisor (GCD) of two numbers. It's based on the principle that the GCD of two numbers remains the same"""
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage:
num1 = 48
num2 = 18

result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is: {result}")

def recursive_gcd(a, b):
    if b == 0:
        return a
    else:
        return recursive_gcd(b, a % b)

# Example usage:
num1 = 48
num2 = 18

result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is: {result}")

"""
The Euclidean algorithm is a method for finding the greatest common divisor (GCD) of two numbers. It's based on the principle that the GCD of two numbers remains the same if the larger number is replaced by the difference between the two numbers.

Euclidean Algorithm for GCD:
Step 1: Take two numbers, a and b, where a is greater than or equal to b.
Step 2: Divide a by b and get the remainder (a % b).
Step 3: Replace a with b and b with the remainder obtained in the previous step.
Step 4: Repeat steps 2 and 3 until the remainder becomes 0. The GCD is the non-zero remainder obtained in the previous step."""

# step 1 
a = 6
b = 4

# step 2
c = a % b 

# step 3
d = b % c

def GCD(a,b):
    if b == 0:
        return a
    else:
        c = a % b 
        return GCD(b,c)
    
print(GCD(6,4))



# m = qn + r ,r = remainder, q = quotient
# learn to write recursive and bottom up 
# time complexity, space complexity of recursion, bottom up, dynamic programming 

# learn all the algorithms
