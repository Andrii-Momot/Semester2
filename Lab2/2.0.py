from turtle import *

class Segment:
    def __init__(self, x, y):
        self.end=(x,y)
        self.beg=(0,0)
    def draw(self):
        up()
        goto(self.beg)
        down()
        goto(self.end[0]+self.beg[0], self.end[1]+self.beg[1])
        up()
    def set_begin(self,x,y):
        self.beg=(x,y)

class Triangle:
    def __init__(self, x1, y1, x2, y2,color="black"):
        self.color=color
        self.Seg1=Segment(x1,y1)
        self.Seg2=Segment(x2-x1,y2-y1)
        self.Seg2.set_begin(x1,y1)
        self.Seg3=Segment(-x2,-y2)
        self.Seg3.set_begin(x2,y2)
    def draw(self):
        pencolor(self.color)
        self.Seg1.draw()
        self.Seg2.draw()
        self.Seg3.draw()
    def set_begin(self,x,y):
        self.Seg1.set_begin(x, y)
        self.Seg2.beg = (self.Seg2.beg[0] + x, self.Seg2.beg[1] + y)
        self.Seg3.beg = (self.Seg3.beg[0] + x, self.Seg3.beg[1] + y)

if __name__ == '__main__':
    #s1 = Segment(100, 100)
    #s1.draw()
    #s2 = Segment(-100, 50)
    #s2.set_begin(20,20)
    #s2.draw()
    t1 = Triangle(100,0, 100,100,"red")
    t1.draw()
    t2 = Triangle(0, 100, -100, 100)
    t2.draw()
    t2.set_begin(50,50)
    t2.draw()
    mainloop()
