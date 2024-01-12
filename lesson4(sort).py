class FoodItem:
    def __init__(self, foodName, calories):
        self.foodName = foodName
        self.calories = calories
        
    def __lt__(self, other):
        return self.calories < other.calories

item1 = FoodItem("Protein", 9)
item2 = FoodItem("Carbohydrate", 4)
item3 = FoodItem("Fat", 18)

sort_foodItems = [
    item1,
    item2,
    item3
]

for sorted_items in sorted(sort_foodItems):
    print (sorted_items.foodName)