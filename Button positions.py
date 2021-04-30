import tkinter
from tkinter import *
m=Tk()
redBtn=Button(m,text="Red",fg="red")
redBtn.pack(side=TOP)

orangebtn=Button(m,text="Orange",fg="orange")
orangebtn.pack(side=BOTTOM)

blueBtn=Button(m,text="Blue",fg="blue")
blueBtn.pack(side=LEFT)

blackBtn=Button(m,text="Black",fg="black")
blackBtn.pack(side=RIGHT)
m.mainloop()