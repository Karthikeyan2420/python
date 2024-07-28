from tkinter import *

root=Tk()
f=Frame(root,bg="Blue",height=50,width=1400)
l1=Label(f,text="Header",bg="Blue",font=("Times New Roman",25))
l1.place(relx=0.43,rely=0.2)
f.place(relx=0.001,rely=0.001)



f1=Frame(root,bg="Blue",height=50,width=1400)
l1=Label(f1,text="Footer",bg="Blue",font=("Times New Roman",25))
l1.place(relx=0.43,rely=0.2)
f1.place(relx=0.001,rely=0.93)

root.mainloop()