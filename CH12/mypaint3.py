from tkinter import *

mycolor = 'blue'

def paint(event):
    r = 4
    x1, y1 = (event.x - r), (event.y - r)
    x2, y2 = (event.x + r), (event.y + r)
    canvas.create_oval(x1, y1, x2, y2, fill=mycolor, outline=mycolor)

def change_red():
    global mycolor
    mycolor = 'red'

def change_blue():
    global mycolor
    mycolor = 'blue'

def change_yellow():
    global mycolor
    mycolor = 'yellow'

def change_green():
    global mycolor
    mycolor = 'green'

window = Tk()
canvas = Canvas(window)
canvas.pack()
canvas.bind("<B1-Motion>", paint)

button = Button(window, text="빨강색", command=change_red)
button.pack(side='left')

button = Button(window, text="파란색", command=change_blue)
button.pack(side='left')

button = Button(window, text="노란색", command=change_yellow)
button.pack(side='left')

button = Button(window, text="초록색", command=change_green)
button.pack(side='left')

window.mainloop()



