from turtle import *
from math import *

reset() # Ініціалізуємо режим малювання
#for i in range(5,100,5):
#    circle(i)

r=[i*0.1 for i in range(64)]
print(r)
up()
setpos(100, 0)
down()
for t in r:
    x=100*cos(t)
    y=50*sin(2*t)
    goto(x,y)


mainloop()