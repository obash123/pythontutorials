# # sentence = "I want to eat a fat rat"
# # print(sentence)
# # words = sentence.split()
# # print(words)

# # len(words) >= 2

# # secondWord = words[1]
# # print(secondWord)


# # print(format(54.437958070572730,"10.2f"))

# # x = 345.3546
# # print(format(x, "10.3f"))


# '''
# Use the variables k and total to write a while loop that computes the 
# sum of the squares of the first 50 counting numbers and associates that value with total. 
# Thus your code should associate 1*1 + 2*2 + 3*3 +... + 49*49 + 50*50 with total.
# Use no variables other than k and total.
# '''
# # k = 0
# # total = 0 
# # while k < 51:
# #     total += k ** 2
# #     k += 1
# # print(total)

# # k1 = 0
# # total1 = 0 
# # while k1 < 50:
# #     k1 += 1
# #     total1 += k1 ** 2
# # print(total1)

# # i = 1
# # while i < 6:
# #   print(i)
# #   if i == 3:
# #     break
# #   i += 1


# # n = int(input("enter a number: "))
# # k = 0
# # total = 0 
# # while k < n+1:
# #     total += k ** 3
# #     k += 1
# # print(total)

# '''
# Write a Python program that takes an integer n as input and prints a pyramid pattern of '' characters.
# The pattern should have n rows, and each row should have '' characters in an increasing order.
# '''

# # def pyramid(n):
# #   for i in range (1,n+1):
# # #    for j in range(1,i+1):
# #       print("*",end= " ")
# #   print()

# # print(pyramid(4))

# # def print_pyramid(n):
# #     for i in range(n):
# #         print(" " * (n - i - 1) + "*" * (2 * i + 1))

# # print(print_pyramid(5))

# # def print_pyramid(n):
# #     for i in range(1, n + 1):
# #         # Print leading spaces
# #         print(" " * (n - i), end="")

# #         # Print '*' characters
# #         print("*" * (2 * i - 1))

      
# # '''
# # Write a Python program that takes a positive integer n as input and calculates the factorial of n. 
# # The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
# # '''

# # n = int(input("enter a number: "))
# # factorial = 1
# # while n > 0:
# #     factorial *= n
# #     n -= 1

# # print(factorial)

# # def calculate_factorial(n):
# #     if n < 0:
# #         return "Factorial is not defined for negative numbers."
# #     elif n == 0 or n == 1:
# #         return 1
# #     else:
# #         factorial_result = 1
# #         for i in range(2, n + 1):
# #             factorial_result *= i
# #         return factorial_result
    

# # '''
# # Write a Python program that takes two positive integers, 
# # start and end, as input and prints all prime numbers within that range (inclusive).
# # '''

# # a = int(input("enter a number: "))
# # b = int(input("enter a number: "))

# # def is_prime(num):
# #     if num < 2:
# #         return False
# #     for i in range(2, int(num**0.5) + 1):
# #         if num % i == 0:
# #             return False
# #     return True


# # for i in range(a,b+1):
# #   if is_prime(i):
# #       print(i)

        
# '''
# A magic square is a square matrix (2D list) 
# where the sums of the numbers in each row, each column, and both main diagonals are the same.
# Write a Python program to generate a magic square of order n (where n is an odd positive integer).
# '''


# start = 1
# matrix = []

# for i in range(3):
#     row = []
#     for j in range(3):
#         row.append(start)
#         start += 1
#     matrix.append(row)


# print(matrix)

# TRY AND EXCEPTION

# try:
#     a = 5/0
#     print(a)
# except ZeroDivisionError as error:
#     print(f"An exception occured {error}")



import math

print(math.sqrt(9))
print(math.pow(5,3))


list1 = [1,2,3,4,5,6,7,8,9]
list1 = set(list1)
list1.pop()
list1.remove(9)
list1.discard(9)
list1.discard(8)
list1.remove(7)
list1.pop()
list1.discard(6)
list1.remove(5)
list1.pop() 
list1.discard(5)

print(list1)