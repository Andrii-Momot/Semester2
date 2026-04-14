from math import gcd

class Rational:
    def __init__(self, n, d=1):
        if isinstance(n, str):
            r=n.split('/')
            if len(r)==1:
                self._n = int(n)
                self._d = d
            else:
                self._n = int(r[0])
                self._d = int(r[1])
        else:
            self._n = n
            self._d = d
        g=gcd(self._n,self._d)
        self._n = self._n//g
        self._d = self._d//g

    def __str__(self):
        return f"{self._n}/{self._d}"
    def __mul__(self, other):
        return Rational(self._n * other._n, self._d * other._d)
    def __add__(self, other):
        return Rational(self._n*other._d + self._d*other._n , self._d * other._d)
    def __sub__(self, other):
        return Rational(self._n * other._d - self._d * other._n, self._d * other._d)
if __name__ == '__main__':
    r1=Rational(5)
    r2=Rational('5')
    r3=Rational(3,4)
    r4=Rational('3/4')
    print(r1)
    print(r2)
    print(r3)
    print(r4)
    print(r1*r2)
    print(r1+r2)
    s="4 - 92 - 79 * 59 * 90/16 * 75 - 55 * 82/41 * 19"
    print(eval(s))
    l=s.split()
    res=[]
    for el in l:
        #print(el)
        if el in "*+-":
            res.append(el)
        else:
            res.append(f"Rational('{el}')")
    print(res)
    res2=" ".join(res)
    print(res2)
    res3=eval(res2)
    print(res3)

