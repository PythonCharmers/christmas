# Christmas Tree Challenge - see www.101computing.net/christmas-tree/

import time
import turtle as t
from random import randint

def draw_circle(turtle, color, x, y, radius):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


def draw_star(turtle, color, x, y, size):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.right(144)
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)
        turtle.forward(size)
    turtle.end_fill()
    turtle.setheading(0)


myPen = t.Turtle()
myPen.shape("turtle")
myPen.speed(20)

window = t.Screen()
window.bgcolor("#072752")

y = -100
width = 240

myPen.penup()
myPen.color("red")
myPen.goto(0, 260)
myPen.write("Merry Christmas and happy 2016", move=False, align="center", font=("Arial", 24, "bold"))

#let's draw the moon
draw_circle(myPen, "white", 130, 100, 30)
draw_circle(myPen, "#072752", 115, 100, 30)

#Now the stars
for i in range(1, 16):
    x = randint(-180, 180)
    y = randint(-150, 180)
    size = randint(5, 15)
    draw_star(myPen, "yellow", x, y, size)

myPen.penup()
myPen.goto(0, 230)
myPen.color("green")
myPen.write("from Python Charmers", align="center", font=("Arial", 24, "bold"))
myPen.hideturtle()

time.sleep(30)
