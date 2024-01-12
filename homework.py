class FoodItem:
    def __init__(self,foodName,gramsFat,gramsCarbs,gramsProtein,gramsCalories):
         self.foodName = foodName
         self.gramsFat = gramsFat
         self.gramsCarbs = gramsCarbs
         self.gramsProtein = gramsProtein
         self.gramsCalories = gramsCalories

    # def __str__(self):
    #    # return self.foodName
    #     return f"{self.foodName} - carbohydrates: {self.gramsCarbs}g"
    
    def __lt__(self,other):
        #return self.gramsCarbs.sort()
        #return self.gramsCarbs < other.gramsCarbs
        return self.gramsCalories < other.gramsCalories
        
    
cheese = FoodItem("cheese",5,3,2,9)
ham = FoodItem("ham",4,22,3,4)
mayo = FoodItem("mayo",12,0,0,9)
bread = FoodItem("bread",2.6,6.2,28,4) 
apple = FoodItem("apple",0,1,25,4) 
coke = FoodItem("coke",0.1,0.3,35.2,4)


sort_foodItems = [
    cheese,
    ham,
    mayo,
    bread,
    apple,
    coke
]

# f_calories = [
#     FoodItem(gramsProtein = 4, gramsCarbs = 4, gramsFat = 9),
#     cheese,ham,mayo,bread,apple,coke    
# ]

# lunch = [cheese, ham, mayo, bread, apple, coke]

# sorted_lunch = sorted(lunch)

# for item in lunch:
#     print(item)
    
for sorted_items in sorted(sort_foodItems):
    print (sorted_items.foodName)





