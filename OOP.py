class A:
    def __init__(self, height):
        self.height = height
    
class B(A):
    def __init__(self, length, breadth, height):
        self.length = length
        self.breadth = breadth
        super().__init__(height)