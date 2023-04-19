import turtle as t
from random import choice

def rhomb(side):
    colors = ['green', 'red', 'blue', 'orange', 'black', 'cyan', 'purple', 'magenta', 'yellow', 'brown']
    t.color(choice(colors))
    for i in [60, 120] * 2:
        t.backward(side)
        t.left(i)
def snowflake(side, count = 10):
    for _ in range(count):
        rhomb(side)
        t.right(360 / count)
t.pensize(2)
# rhomb(150)
snowflake(50) # вторым параметром можно передать количество
t.done()