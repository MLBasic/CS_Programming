import turtle
import random

screen = turtle.Screen()
image1 = "rabbit.gif"
image2 = "turtle.gif"
screen.addshape(image1)
screen.addshape(image2)

t1 = turtle.Turtle()
t1.shape(image1)
t1.pensize(5)
t1.penup()
t1.goto(-300, 0)
t1.pendown()

t2 = turtle.Turtle()
t2.shape(image2)
t2.pensize(5)
t2.penup()
t2.goto(-300,-100)
t2.pendown()

for i in range(100):
    d1 = random.randint(1,60)
    t1.forward(d1)
    d2 = random.randint(1,60)
    t2.forward(d2)
