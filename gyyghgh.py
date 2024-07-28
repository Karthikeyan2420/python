import tkinter
from tkinter import *
from tkinter import messagebox
r=Tk()
r.geometry("400x400")

l1=Label(r,text="transport charge")
l1.grid(row=0,column=1)
l2=Label(r,text="delivery charge")
l2.grid(row=1,column=1)
l3=Label(r,text="salary of person")
l3.grid(row=2,column=1)

e1=Entry(r)
e1.grid(row=0,column=2)
e2=Entry(r)
e2.grid(row=1,column=2)
e3=Entry(r)
e3.grid(row=2,column=2)

def add():
    a=int(e1.get())
    b=int(e2.get())
    d=int(e3.get())
    c=d-(a+b)
    messagebox.showwarning( "Hello Python", c)





b=Button(r,text="submit",command=lambda:add())
b.grid(row=3,column=3) 

r.mainloop()  

