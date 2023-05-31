import turtle
import math
import random

player = turtle.Turtle()
player.shape("turtle")
screen = player.getscreen()
screen.bgcolor("black")
screen.setup(800, 600)
player.color("yellow")

player.penup()
player.goto(-300, 0)
player.pendown()

velocity = 70
player.left(45)

def turnleft(): # 키보드 화살표 왼쪽 
    player.left(5)

def turnright(): # 키보드 화살표 오른쪽
    player.right(5)

def turnup(): # 속도를 10만큼 올린다, 키보드 화살표 위쪽
    global velocity
    velocity = velocity + 10

def turndown(): # 속도를 10만큼 줄인다, 키보드 화살표 아래쪽
    global velocity
    velocity = velocity - 10

def fire():
    x = -300
    y = 0
    player.color(random.random(), random.random(), random.random())
    player.penup()
    player.goto(x,y)
    player.pendown()
    angle = player.heading()
    vx = velocity * math.cos(angle*3.14/180)
    vy = velocity * math.sin(angle*3.14/180)
    while player.ycor() >= 0:
        vx = vx
        vy = vy - 10
        x = x + vx
        y = y + vy
        player.goto(x,y)
        # player.stamp()
        
screen.onkeypress(turnleft, "Left")
screen.onkeypress(turnright, "Right")
screen.onkeypress(turnup, "Up")
screen.onkeypress(turndown, "Down")
screen.onkeypress(fire, "space")

screen.listen()
turtle.mainloop()
