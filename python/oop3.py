class Circle:    

 
    
    def __init__(self,radius):
        self.r = radius

    def calculateArea(self):
        self.A = 3.14 * self.r * self.r
        return self.A


c = Circle(25)
print(c.calculateArea())