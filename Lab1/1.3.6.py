class Rectangle:
    def __init__(self,a=1,b=1): #параметри по замовчуванню
        self.a=a
        self.b=b
    def area(self):
        return self.a * self.b
    def perimeter(self):
        return (self.a + self.b) * 2
    def shaw(self):
        print(f"a={self.a},b={self.b}")


with open("input.txt") as f:
    max_area=0
    rmax=Rectangle(0,0)
    for line in f:
        a,b=map(int,line.split())
        r=Rectangle(a,b)
        s = r.area()
        print(s)
        if s > max_area:
            max_area = s
            rmax=r

print(max_area)
rmax.shaw()



