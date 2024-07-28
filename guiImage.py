from tkinter import *
from PIL import  Image
from PIL.ImageTk import PhotoImage

win = Tk()

win.geometry("700x500")



img = PhotoImage(Image.open("kitkat.jpg"))
label = Button(win, image = img)
label.pack()

win.mainloop()


