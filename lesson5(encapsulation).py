class Base:
    def __init__(self):
        self.a = 3
        self.__c = 5

class Derived(Base):
    def __init__(self):


        Base.__init__(self)
        print(self.a)
        #print(self.__c)

pl = Base()
#print(pl.c)
print(pl.a)
qt = Derived()