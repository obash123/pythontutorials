# # 2D List
# matrix_2d = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# # print(matrix_2d[0][0])


# # 3D List
# matrix_3d = [
#     [
#         [1, 2, 3],
#         [4, 5, 6]
#     ],
#     [
#         [7, 8, 9],
#         [10, 11, 12]
#     ]
# ]


# matrix_3d[1][1][1] = 13
# # print(matrix_3d)


# matrix1_2d = [
#     [1, 5, 9],
#     [2, 4, 9],
#     [1, 1, 2]
# ]



# for i in matrix1_2d:
#     print(i)

# for row in matrix1_2d:
#     for element in row:
#         print(element, end=' ')
#     print()  


# multlist = [[1,5,9], [2, 4, 9,], [1,1, 2]]
# for i in range(len(multlist)) :
#    for j in range(len(multlist[i])) :
#       print(multlist[i][j], end=" ")
#    print()

#assignment no 1
#check how this works 


def function(n):
    for i in range(n+1):
        for j in range(i+1):
            print(i,j, end = " ")
        print()

print(function(3))

# Create a Python program or function that grades a multiple-choice test.
# The test consists of questions, and each question may have multiple correct choices.
# The student's answers are compared with the correct answers, 
# and a score is calculated based on the correctness of the responses.

# assignment 2
# practice list methods

# def multiple(n):
#     return (n * 2)

# set1 = (2,3,4,5,6)
# solution = map(multiple,set1)
# print(list(solution))


right_answer = ['a','b','d','d','a','b','c','c','e','e']
student_answer_to_compare = []

student_response = input("enter your input: ")

n = 5
 
for i in range(1, n+1):
    for j in range(0, n-i+1):
        print(' ', end='')
 
    # first element is always 1
    C = 1
    for j in range(1, i+1):
 
        # first value in a line is always 1
        print(' ', C, sep='', end='')
 
        # using Binomial Coefficient
        C = C * (i - j) // j
    print()

from math import factorial
 
# input n
n = 5
for i in range(n):
    for j in range(n-i+1):
 
        # for left spacing
        print(end=" ")
 
    for j in range(i+1):
 
        # nCr = n!/((n-r)!*r!)
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
 
    # for new line
    print()