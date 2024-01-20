import random

p = random.randint(0,100)
print(p)
guess = int(input(" guess the value: "))
while guess != p:
    print("you're wrong, try again")
    guess = int(input(" guess the value: "))
    if guess < p:
        print(" it's a higher value")
    elif guess > p:
        print("it's a lower value")
else:
    print("you're correct")


# value = 90

# guess = int(input(" guess the value: "))
# while guess != value:
#     print("you're wrong, try again")
#     guess = int(input(" guess the value: "))
# else:
#     print("you're correct")

# calculation
# # 1
#   1 2
#   1 2  3
#   1 2  3  4

# # 1
#   1 2
#   1 2  3
#   1 2  3  4
#   1 2  3
#   1 2
#   1

# palindrom checker 


# for loop iterates over a sequence 

# write a nested loop that gives a matrix 

# for i in range(2):
#     for j in range(2):
#         print (i,j)

# for i in range(5):
#     print()
#     for j in range(i + 1):
#         print ("*",end = " ")
# #    print("\n\n")

# num = 0       
# for i in range(4):
#     for j in range (i + 1):
#         print (num, end = " ")
#         num += 1
#     print()


# for i in range(5,0,-1):
#     for j in range(1, i + 1):
#         print(j, end = " ")
#     print()




