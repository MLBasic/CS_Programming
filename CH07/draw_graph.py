import turtle

# 함수 만들기  막대그래프 하나를 그리는 함수
def drawBar(height, width=40):
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write(str(height), font=('Times New Roman', 16, 'bold'))
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()

    
data = [120, 56, 309, 220, 156, 23, 98]

t = turtle.Turtle()
t.color("blue")
t.fillcolor("red")
t.pensize(3)

for d in data:
    drawBar(d, 20)

turtle.done()



    
    
