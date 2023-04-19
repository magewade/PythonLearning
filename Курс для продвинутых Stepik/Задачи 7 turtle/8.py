from turtle import *
from random import  *
colormode(255)
bgcolor("black")
speed(0)
hideturtle()
penup()

for i in range(randrange(500)):
        tracer(1000)
        fillcolor(randrange(255), randrange(255), randrange(255))
        goto(randrange(-300, 300), randrange(-300, 300))
        left(randrange(180))
        begin_fill()
        r = randrange(5, 30)
        for i in range(5):
                right(144)
                forward(r)
        end_fill()
done()