from tkinter import *

window = Tk()

def process():
    temperature = float(e1.get())
    mytemp = (temperature - 32)*5/9
    e2.insert(0, str(round(mytemp,2)))

def c2f():
    c_temp = float(e2.get())
    f_temp = c_temp*9/5+32
    e1.insert(0, str(round(f_temp)))

l1 = Label(window, text="화씨", font='helvetica 16 italic')
l2 = Label(window, text="섭씨", font='helvetica 16 italic')
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)

e1 = Entry(window, bg='yellow', fg='black')
e2 = Entry(window, bg='yellow', fg='black')
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b1 = Button(window, text="화씨->섭씨", command=process)
b2 = Button(window, text="섭씨->화씨", command=c2f)
b1.grid(row=2, column=0)
b2.grid(row=2, column=1)

window.mainloop()


