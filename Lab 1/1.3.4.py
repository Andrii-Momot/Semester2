class Rectangle:
    def __init__(self,a=1,b=1): #параметри по замовчуванню
        self.a=a
        self.b=b
    def area(self):
        return self.a * self.b
    def perimeter(self):
        return (self.a + self.b) * 2

r1=Rectangle(4,5)
print(r1.area())
print(r1.perimeter())

r2=Rectangle(4)
print(r2.area())

r1.a=2
r1.b=3
print(r1.area())
print(r1.perimeter())

