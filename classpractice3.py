# class Recipe:
#     def __init__(self,ingredients,instructions,cooking_time):
#         self.ingredients = ingredients
#         self.instructions = instructions
#         self.cooking_time = cooking_time
#         self.recipe_details = [] 

#     def ANR(self):
#         meal = {
#             'ingredient': self.ingredients, 
#             'cooking_instructions': self.instructions, 
#             'time': self.cooking_time   
#         }

#         self.recipe_details.append(meal) 
#         return meal

# ing = input("what are the ingredients of the meal(enter done to stop): ")
# while ing != "done":
#     ing = input("what are the ingredients of the meal(enter done to stop): ")

# c_i = input("enter the cooking instructions(enter finish to stop): ")
# while c_i != "finish":
#     c_i = input("enter the cooking instructions(enter finish to stop): ")

# t = input("how long does it take to cook: ")

# food = Recipe(ing,c_i,t)
# print(food.ANR())

class Recipe:
    def __init__(self):
        self.ingredients = []
        self.instructions = []
        self.cooking_time = 0

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def add_instruction(self, instruction):
        self.instructions.append(instruction)

    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time

    def get_recipe_details(self):
        return {
            'ingredients': self.ingredients,
            'cooking_instructions': self.instructions,
            'cooking_time': self.cooking_time
        }


food = Recipe()

ing = input("Enter the ingredients of the meal (enter 'done' to stop): ")
while ing != "done":
    food.add_ingredient(ing)
    ing = input("Enter the ingredients of the meal (enter 'done' to stop): ")


c_i = input("Enter the cooking instructions (enter 'finish' to stop): ")
while c_i != "finish":
    food.add_instruction(c_i)
    c_i = input("Enter the cooking instructions (enter 'finish' to stop): ")


t = input("How long does it take to cook: ")
food.set_cooking_time(t)

print(food.get_recipe_details())
