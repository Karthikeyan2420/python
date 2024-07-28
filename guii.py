from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk

win=Tk()
win.geometry("500x500")
frame=Frame(win,width=600,height=400)
frame.pack()
frame.place(relx=0.2,rely=0.01)
img=ImageTk.PhotoImage(Image.open("minions.jpg"))
label=Label(frame,image=img)
label.pack()



a=Label(win,text="first name:")
a.place(relx=0.02,rely=0.1)


win.mainloop()
