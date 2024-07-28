Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: D:\karthikeyan\karthikeyan\after class\3_1GUI.py
>>> 
... from tkinter import *
... r=Tk()
... r.geometry("400x400")
... 
... l1=Label(r,text="Enter the First Value")
... l1.grid(row=0,column=1)
... l2=Label(r,text="Enter the Second Value")
... l2.grid(row=1,column=1)
... l3=Label(r,text="Result")
... l3.grid(row=2,column=1)
... 
... e1=Entry(r)
... e1.grid(row=0,column=2)
... e2=Entry(r)
... e2.grid(row=1,column=2)
... e3=Entry(r)
... e3.grid(row=2,column=2)
... 
... def add():
...     a=int(e1.get())
...     b=int(e2.get())
...     c=a+b
...     e3.delete(0,50)
...     e3.insert(0,c)
... b=Button(r,text="Add",command=lambda:add())
... b.grid(row=3,column=3) 
... 
... r.mainloop()  
... 
