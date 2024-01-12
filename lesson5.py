class Animal:
    def __init__(self,colors):
        self.num_legs = 4
        self.colors = colors
        self.num_eyes = 2

    def make_sound(self,sound_name):
        return sound_name




class Dog(Animal):
    

    def make_sound(self,sound_name,sound_htz):
        return sound_name + " " + str(sound_htz)
    
rottweiler = Dog('pink')
print(rottweiler.make_sound("woof",4))
