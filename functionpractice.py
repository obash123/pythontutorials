# def circle_area(radius):
#     return radius * radius * (22/7)


# def square_area(length):
#     return length * length 


# def triangle_area(base,height):
#     return 0.5 * base * height


# rad = int(input("enter the radius: "))
# sq = int(input("enter the length of the square: "))
# base = int(input("enter the base: "))
# height = int(input("enter the height "))

# print(circle_area(rad))
# print(square_area(sq))
# print(triangle_area(base,height))


# class Shape():
#     def __init__(self,radius,length):
#         self.height = height
#         self.radius = radius
#         self.base = base
#         self.length = length

#     def circle_area(self):
#         return self.radius * self.radius * (22/7)


#     def square_area(self):
#         return self.length * self.length 


#     def triangle_area(self):
#         return 0.5 * self.base * self.height


# rad = int(input("enter the radius: "))
# sq = int(input("enter the length of the square: "))
# base = int(input("enter the base: "))
# height = int(input("enter the height "))

# sol = Shape(rad)
# uti = Shape(sq)
# on =  Shape(base,height)

# print(sol.circle_area())

# Write a function that takes a list of integers as input and returns the sum of all the numbers that are divisible by both 3 and 5.


x = 5
def finder(*num):
    addition = 0
    for i in num:
        if (i % 3 == 0) and (i % 5 == 0):
            addition += i
    return addition


print(finder(5,6,7,9,15,21,30))

# Write a program that composes two functions, f(x) and g(x), to create a new function h(x) such that h(x) = f(g(x)).
# pascals 