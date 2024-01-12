class Circle:
    def __init__(self,radius):
        self.radius = radius


    def area(self):
        return self.radius * self.radius * (22/7)

# value = int(input("Enter the value of the radius: "))
# ans = Circle(value)
# print("the area is: ",ans.area())

class Triangle:
    def __init__(self,height,base):
        self.height = height
        self.base = base

    def Area(self):
        return self.base * self.height * 1/2
    
# var = int(input("Enter the value of base: "))
# var2 = int(input("Enter the value of the height: "))

# Ans = Triangle(var,var2)
# print("the area is: ", Ans.Area())

class Square:
    def __init__(self,length):
        self.length = length

    def AREA(self):
        return self.length * self.length
    

# var3 = int(input("enter the length of the side: "))
# ANS = Square(var3)
# print("The area of the square is: ",ANS.AREA())

intro = input("What shape's area would you like to calculate: ")
if intro == "Circle":
    value = int(input("Enter the value of the radius: "))
    ans = Circle(value)
    print("the area is: ",ans.area())

elif intro == "Square":
    var3 = int(input("enter the length of the side: "))
    ANS = Square(var3)
    print("The area of the square is: ",ANS.AREA())

elif intro == "Triangle":
    var = int(input("Enter the value of base: "))
    var2 = int(input("Enter the value of the height: "))
    Ans = Triangle(var,var2)
    print("the area is: ", Ans.Area())