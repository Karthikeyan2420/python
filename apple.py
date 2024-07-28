
from tkinter import *
r=Tk()
r.geometry("400x400")

l1=Label(r,text="Enter the First Value")
l1.grid(row=0,column=1)
l2=Label(r,text="Enter the Second Value")
l2.grid(row=1,column=1)
l3=Label(r,text="Result")
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
    c=a+b
    e3.delete(0,50)
    e3.insert(0,c)
    
def sub():
    c=int(e1.get())
    d=int(e2.get())
    e=c-d
    e3.delete(0,50)
    e3.insert(0,e)
    
def multi():
    f=int(e1.get())
    g=int(e2.get())
    h=f*g
    e3.delete(0,50)
    e3.insert(0,h)
    
def div():
    i=int(e1.get())
    j=int(e2.get())
    k=i/j
    e3.delete(0,50)
    e3.insert(0,k)

    
b=Button(r,text="add",command=lambda:add())
c=Button(r,text="sub",command=lambda:sub())
z=Button(r,text="multi",command=lambda:multi())
x=Button(r,text="div",command=lambda:div())

b.grid(row=0,column=3) 
c.grid(row=1,column=3) 
z.grid(row=2,column=3) 
x.grid(row=3,column=3) 

r.mainloop()  




