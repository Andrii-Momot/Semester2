class Equation:
    def __init__(self, b, c):
        self.b = b
        self.c = c
    def show(self):
        print(f"{self.b}x + {self.c} = 0")
    def solve(self):
        if self.b!=0:
            return (-self.c/self.b,)
        else:
            if self.c==0:
                return ("Inf",)
            else:
                return ()

class QuadraticEquation(Equation):
    def __init__(self, a, b, c):
        self.a = a
        super().__init__(b,c)
    def show(self):
        print(f"{self.a}x^2 + {self.b}x + {self.c} = 0")
    def solve(self):
        if self.a==0:
            return Equation(self.b, self.c).solve()
        else:
            d=self.b**2-4*self.a*self.c
            if d==0:
                return (-self.b/2/self.a,)
            if d<0:
                return ()
            x1=(-self.b+d**0.5)/2/self.a
            x2 = (-self.b - d ** 0.5) / 2 / self.a
            return (x1,x2)



if __name__ == "__main__":
    # eq1 = QuadraticEquation(1, 2,1)
    # eq1.show()
    # print(eq1.solve())

    equations = []
    with open("input01.txt") as f:
        for line in f:
            l=list(map(int,line.split()))
            #print(l)
            if len(l)==2:
                equations.append(Equation(l[0], l[1]))
            if len(l)==3:
                equations.append(QuadraticEquation(l[0], l[1], l[2]))

    # for eq in equations:
    #     eq.show()
    #     print(eq.solve())

    print("Рівняння, які не мають розв'язків:")
    for eq in equations:
        sols = eq.solve()
        if len(sols)==0:
            eq.show()
            print(sols)

    print("Рівняння, які мають один розв'язок:")
    for eq in equations:
        sols = eq.solve()
        if len(sols)==1:
            eq.show()
            print(sols)

