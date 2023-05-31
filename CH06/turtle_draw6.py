import turtle
t = turtle.Turtle()

#1. 60도씩 360/60 == 6개 의 원을 그린다면 ?

#theta = 60
#for i in range(360/theta):
#    t.circle(100)
#    t.left(theta)

count = 60
for i in range(count):
    t.circle(100)
    t.left(360/count)

turtle.done()
