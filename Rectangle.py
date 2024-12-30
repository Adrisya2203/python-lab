class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return (self.length*self.breadth)
    def perimeter(self):
        return 2*(self.length+self.breadth)
r1=Rectangle(5,3)
r2=Rectangle(8,5)
r1.area()
r1.perimeter()
print("area and perimeter:",r1.area,r1.perimeter)
r2.area()
r2.perimeter()
print("area and perimeter:",r2.area,r2.perimeter)


