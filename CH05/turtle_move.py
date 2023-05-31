import turtle

t = turtle.Turtle()
t.shape("turtle")

t.width(3)
t.shapesize(3,3)

while True:
    command = input("명령을 입력하세요(l,r,q) : ")
    if command == 'l':
        t.left(90)
        t.forward(100)
    if command == 'r':
        t.right(90)
        t.forward(100)
    if command == 'q':
        turtle.done()
