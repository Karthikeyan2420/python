'''import tkinter
root= tkinter.Tk()
root.mainloop() 


from tkinter import *
Z = Tk()
for fm in ['red','orange','violet','purple','blue','ash','black']:
    Frame(height=100,width= 600,bg=fm).pack()                
Z.mainloop()


import tkinter
from tkinter import messagebox


def hiiamsai ():
   tkinter.messagebox.showwarning("levelup","now")

top =tkinter.Tk()
B =tkinter.Button(top,text="tapme",command=lambda:hiiamsai())
B.pack()
top.mainloop()                                  

import turtle

turtle.speed(1)

for i in range(4):
	turtle.forward(100)
	

	val = turtle.heading()
	
	turtle.write(str(val))
	turtle.backward(30)
	turtle.left(98)
'''





import tkinter
from tkinter import messagebox

def helloCallBack():

   tkinter.messagebox.showwarning( "Hello Python", " saisaran ")
def new():
   tkinter.messagebox.showwarning( "hello world ", " 9876543210 ")
def zaz():
    tkinter.messagebox.showwarning( "hello soldiers", " message")
top = tkinter.Tk()
B = tkinter.Button(top,text="name",command=lambda:helloCallBack())
s = tkinter.Button(top,text="number",command=lambda:new())
x = tkinter.Button(top,text="CONTENT",command=lambda:zaz())
B.pack()
s.pack()
x.pack()
top.mainloop() 


