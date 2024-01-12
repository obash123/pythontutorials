# Recipe Book Application:
#Create a class representing recipes with attributes for ingredients, instructions, and cooking time. Implement methods to add new recipes, search by ingredients, and display recipes.




class Recipes:
    def __init__(self,ingredients,instructions,cooking_time) :
        self.ingredients = ingredients
        self.instructions = instructions
        self.cooking_time = cooking_time

    
    def Ingredients():
        pass



bread = Recipes("flour","butter","sugar","egg","yeast","milk"),
("do......"),(" 4 ")

ham = Recipes("ham",4,22,3,4)
mayo = Recipes("mayo",12,0,0,9)
bread = Recipes("bread",2.6,6.2,28,4) 
apple = Recipes("apple",0,1,25,4) 
coke = Recipes("coke",0.1,0.3,35.2,4)



lunch = [bread, ham, mayo, bread, apple, coke]
for item in lunch:
    print(item)
