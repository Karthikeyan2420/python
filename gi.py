from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image

w=Tk()
w.title("welcome to python")
w.geometry("400x400")
w.configure(background="violet")


a=Label(w,text="first name:").grid(row=0,column=0)
b=Label(w,text="last name:").grid(row=1,column=0)
c=Label(w,text="email id:").grid(row=2,column=0)
d=Label(w,text="contact no:").grid(row=3,column=0)

a1=Entry(w).grid(row=0,column=1)
b1=Entry(w).grid(row=1,column=1)
c1=Entry(w).grid(row=2,column=1)
d1=Entry(w).grid(row=3,column=1)

frame=Frame(w,width=600,height=400)
frame.place(anchor="center",relx=0.5,rely=0.5)
img=ImageTk.PhotoImage(Image.open("kitkat.jpg"))
label=Label(frame,image=img)


b=ttk.Button(w,text="submit").grid(row=4,column=0)


label.pack()
w.mainloop()
