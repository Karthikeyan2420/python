import tkinter
from tkinter import *
from PIL import ImageTk,Image
win=Tk()
win.geometry("500x500")
frame=Frame(win,width=200,height=200)
frame.pack()
frame.place(anchor="center",relx=0.5,rely=0.5)
img=ImageTk.PhotoImage(Image.open("dairy.jpg"))
label=Label(frame,image = img)
label.pack()
win.mainloop()


a=Label(win,text="first name:")
a.place(relx=0.01,rely=0.4)
b=Label(win,text="last name:")
b.place(relx=0.01,rely=0.5)
c=Label(win,text="email id:")
c.place(relx=0.01,rely=0.6)
d=Label(win,text="contact no:")
d.place(relx=0.01,rely=0.7)

a1=Entry(win)
a1.place(relx=0.02,rely=0.41)
b1=Entry(win)
a.place(relx=0.02,rely=0.51)
c1=Entry(win)
a.place(relx=0.02,rely=0.6)
d1=Entry(win)
a.place(relx=0.02,rely=0.7)
