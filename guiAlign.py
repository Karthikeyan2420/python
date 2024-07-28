import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image

win=Tk()
win.geometry("500x500")

frame=Frame(win,width=100,height=100)
frame.pack()
frame.place(anchor="n",relx=0.5)

img=ImageTk.PhotoImage(Image.open("kitkat.jpg"))
label=Label(frame,image = img)
label.pack()

a=Label(win,text="First Name:")
a.place(relx=0.05,rely=0.5)
b=Label(win,text="Last Name:")
b.place(relx=0.05,rely=0.6)
c=Label(win,text="Email-ID:")
c.place(relx=0.05,rely=0.7)
d=Label(win,text="Contact No:")
d.place(relx=0.05,rely=0.8)

a1=Entry(win)
a1.place(relx=0.2,rely=0.5)
b1=Entry(win)
b1.place(relx=0.2,rely=0.6)
c1=Entry(win)
c1.place(relx=0.2,rely=0.7)
d1=Entry(win)
d1.place(relx=0.2,rely=0.8)


R=Label(win,text="Gender :")
R.place(relx=0.5,rely=0.5)
var = IntVar()
R1 = Radiobutton(win, text="Male", variable=var, value=1)
R1.place(relx=0.6,rely=0.5)
R2 = Radiobutton(win, text="Female", variable=var, value=2)
R2.place(relx=0.7,rely=0.5)

combo1=Label(win,text="Country :")
combo1.place(relx=0.5,rely=0.6)
combo = ttk.Combobox(win, values=["India", "America", "Africa", "Green Land"])
combo.place(relx=0.6,rely=0.6)

text1=Label(win,text="Message : ")
text1.place(relx=0.5,rely=0.7)
text2 = Text(win,height=2, width=18)
text2.place(relx=0.6,rely=0.7)

def senthil(name):
    messagebox.showwarning("Excellent work",name)
B1=Button(win,text="Done",command=lambda:senthil(a1.get()))
B1.place(relx=0.7,rely=0.9)
win.mainloop()
