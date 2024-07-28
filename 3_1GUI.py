
# Python provides the standard library Tkinter for creating the graphical user interface
# for desktop based applications.


# import tkinter
# root= tkinter.Tk()
# root.mainloop() 


# from tkinter import *
# root=Tk()
# root.geometry("200x200")
# frame=Frame(root,width=200,height=200)
# frame.pack()
# root.mainloop()

# from tkinter import *
# root=Tk()
# frame=Frame(root,bg="skyblue",width=500,height=500)
# frame.pack()
# root.mainloop()
 


"""import tkinter
from tkinter import messagebox

def helloCallBack():
    tkinter.messagebox.showwarning( "Hello Python", "Hello World")

top = tkinter.Tk()
B = tkinter.Button(top,text="new",command=lambda:helloCallBack())
B.pack() 
top.mainloop()""" 


"""import tkinter
t=tkinter.Tk()
frame=tkinter. Frame(t, bg="skyblue", width=500, height=500)
B = tkinter.Button(t, text ="Hello",activebackground="red")
B.pack()
frame.pack()
t.mainloop()"""  



""" from tkinter import *
root = Tk()
for fm in ['orange','white','green','blue','white','black']:
    Frame(height = 20,width = 640,bg = fm).pack()
root.mainloop()   """

#

from tkinter import *
r=Tk()
r.geometry("400x400")

l1=Label(r,text="Enter the First Value")
l1.grid(row=0,column=1)
l2=Label(r,text="Enter the Second Value")
l2.grid(row=1,column=1)
l3=Label(r,text="result")
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
    c=a-b
    e3.delete(0,50)
    e3.insert(0,c)
b=Button(r,text="Add",command=lambda:add())
b.grid(row=3,column=3) 

r.mainloop()  


