import turtle
from numpy import arange

def curve(angle, max_len):
    for i in arange(0, max_len, 1):
        turtle.left(angle)
        turtle.forward(i)
        turtle.dot(4)
    turtle.goto(0, 0)


turtle.penup()
turtle.hideturtle()
turtle.tracer(0, 0)
for angle in arange(222, 270, .05):
    turtle.clear()
    curve(angle, 600)
    turtle.update()
turtle.mainloop()