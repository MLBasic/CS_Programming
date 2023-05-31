from tkinter import *

window = Tk()
window.geometry("800x300")

btn1 = Button(window, text="버튼1", font='맑은고딕 16', width="8", height="2")
btn1.place(x=40,y=20)

btn2 = Button(window, text="버튼2", font='맑은고딕 16', width="8", height="2")
btn2.place(x=240,y=20)

btn3 = Button(window, text="버튼3", font='맑은고딕 16', width="8", height="2")
btn3.place(x=440,y=20)

w = Label(window, text="박스 1", bg="red", fg="white", font='맑은고딕 16', width="60")
w.place(x=40,y=100)

w = Label(window, text="박스 2", bg="green", fg="black", font='맑은고딕 16', width="60")
w.place(x=40,y=140)

w = Label(window, text="박스 3", bg="blue", fg="white", font='맑은고딕 16', width="60")
w.place(x=40,y=180)



window.mainloop()
