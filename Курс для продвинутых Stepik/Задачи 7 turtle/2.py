import turtle
def hexagon(side):
    turtle.speed(10)
    turtle.pensize(7)
    turtle.shape('circle')
    col = ['#f5250a', '#f59b0a', '#f5e90a',
           '#08cf0c', '#081ccf', '#8908cf']
    for a in range(12):
        for i in range(6):
            turtle.color(col[i])
            turtle.forward(side)
            turtle.left(60)
        turtle.left(30)

n = int(input("Введите длину стороны: "))
hexagon(n)

turtle.exitonclick()
