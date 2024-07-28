import tkinter
from tkinter import *
from PIL import ImageTk,Image
win=Tk()
win.geometry("500x500")
frame=Frame(win,width=200,height=200)
frame.pack()
frame.place(anchor="center",relx=0.5,rely=0.5)
img=ImageTk.PhotoImage(Image.open("new1.jpg"))
label=Label(frame,image = img)
label.pack()
win.mainloop()
