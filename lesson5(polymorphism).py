class Dog:
    def __init__(self):
        pass
    def animal_sound(self,animal):
        return animal
    
class Lion:
    def __init__(self):
        pass
    def animal_sound(self,animal):
        return animal
dog = Dog()
lion = Lion()



animals = [dog.animal_sound("Husky"), lion.animal_sound("African Lion")]

for animal in animals:
    print(animal)