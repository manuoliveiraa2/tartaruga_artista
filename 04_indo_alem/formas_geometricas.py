from tracemalloc import start
import turtle
from turtle import onscreenclick, mainloop, shape, width, onkey, listen


turtle = turtle.Turtle()

def square(start, end):
    turtle.penup()
    turtle.goto(start[0], start[1])
    turtle.pendown()

    diff_x = abs (start[0] - end[0])
    diff_y = abs(start[1] - end[1])
    width = max(diff_x, diff_y) 


    for _ in range(4):
        turtle.forward(width)
        turtle.left(90)

def to_square():
    global shape
    shape = square

def to_retangle():
    global shape
    shape = retangle

start = None
shape = square

def tap(x, y):
    global start
    if start is None:
        start = x, y
        
    
    else:
        end = x, y
        shape(start, end)

        start = None

def triangle(start, end):
    turtle.penup()
    turtle.goto(start[0], start[1])
    turtle.pendown()

    diff_x = abs (start[0] - end[0])
    diff_y = abs(start[1] - end[1])
    width = max(diff_x, diff_y) 

    for _ in range(3):
        turtle.forward(width)
        turtle.left(120)
    

def retangle(start, end):
    turtle.penup()
    turtle.goto(start[0], start[1])
    turtle.pendown()

    diff_x = abs (start[0] - end[0])
    diff_y = abs(start[1] - end[1])
    width = max(diff_x, diff_y)

    for _ in range(4):
        turtle.forward(width)
        turtle.left(90)


def line():
    turtle.forward(100)

turtle.color('blue')

def star():
    for _ in range(20):
        turtle.left(90)
        turtle.forward(100)
        turtle.left(10)
        turtle.backward(100)
        turtle.left(10)
       
def shape_square():
    global shape
    shape = square

def shape_triangle():
    global shape
    shape = triangle

def change_shape(next_shape):
    global shape
    shape = next_shape

onscreenclick(tap)
onkey(lambda: change_shape(square), 's')
onkey(lambda: change_shape(triangle), 'c')
listen()
mainloop()