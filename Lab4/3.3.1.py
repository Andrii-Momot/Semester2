class Figure:
    def dimention(self):
        return 2
    def perimetr(self):
        pass
    def square(self):
        pass
    def squareSurface(self):
        pass
    def volume(self):
        pass

class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def square(self):
        return self.a * self.b
    def perimetr(self):
        return 2*(self.a + self.b)
    def volume(self):
        return self.square()

class RectangularParallelepiped(Rectangle):
    def __init__(self, a, b, c):
        super().__init__(a,b)
        self.c = c
    def dimention(self):
        return 3
    def perimetr(self):
        pass
    def square(self):
        pass
    def squareSurface(self):
        return self.c*super().perimetr()
    def volume(self):
        return super().square()*self.c

if __name__ == "__main__":
    r1 = Rectangle(2,3)
    print(r1.dimention())
    print(r1.square())
    print(r1.perimetr())
    print(r1.squareSurface())
    p1=RectangularParallelepiped(1,2,3)
    print(p1.dimention())
    print(p1.square())
    print(p1.perimetr())
    print(p1.squareSurface())

    with open("input01.txt") as f:
        max_volume=0
        max_figure=Figure()
        for line in f:
            if line.split()[0] == "Rectangle":
                a, b = map(int, line.split()[1:])
                r = Rectangle(a, b)
                s = r.volume()
                if s > max_volume:
                    max_volume = s
                    max_figure=r
                print(s)
            elif line.split()[0] == "RectangularParallelepiped":
                a, b, c = map(int, line.split()[1:])
                r = RectangularParallelepiped(a, b, c)
                s = r.volume()
                if s > max_volume:
                    max_volume = s
                    max_figure = r
                print(s)
    print(max_volume)
    print(type(max_figure).__name__)