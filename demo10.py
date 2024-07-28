""" import tkinter
top = tkinter.Tk()
top.mainloop() """

""" from tkinter import*
abi = Tk()
frame = Frame(abi,bg="blue",width=500,height=500)
frame.pack()
abi.mainloop() """

""" import tkinter
a = tkinter.Tk()
b = tkinter.Button(a,text="hello world",activebackground="pink",bg="blue")
b.pack()
a.mainloop()
 """

""" 
from tkinter import*
from tkinter import Tk
root =Tk()
text = Text(root,height=2,width=30)
text.insert(INSERT,"Hello world ....")
text.insert(END,"bye bye .....")
text.pack()
b= Button(root,text="submit")
b.pack()
text.tag_add("here","1.0","1.4")
text.tag_add("start", "1.8", "1.13")
text.tag_config("here", background="orange", foreground="blue")
text.tag_config("start", background="black", foreground="green")
root.mainloop() """

import tkinter
from tkinter import *
from tkinter  import ttk
from  tkinter import messagebox
from PIL import ImageTk,Image

root =Tk()
root.geometry("500x500")
frame = Frame(root, width= 100 ,height=100)
frame.pack()
frame.place(anchor="n",relx=0.5,rely=0)
img =ImageTk.PhotoImage(Image.open("dairy.jpg"))
label = Label(frame,image=img)
label.pack()
a=Label(root,text="first Name")
a.place(relx=0.05,rely=0.5)
a1=Label(root,text="last Name")
a1.place(relx=0.05,rely=0.6)
a2=Label(root,text="email id")
a2.place(relx=0.05,rely=0.7)
a3=Label(root,text="contact no")
a3.place(relx=0.05,rely=0.8)
b1=Entry(root)
b1.place(relx=0.2,rely=0.5)
b2=Entry(root)
b2.place(relx=0.2,rely=0.6)
b3=Entry(root)
b3.place(relx=0.2,rely=0.7)
b=Entry(root)
b.place(relx=0.2,rely=0.8)
r =Label(root,text="gender")
r.place(relx=0.7,rely=0.5)
combo 
root.mainloop()



