from tkinter import *
from tkinter import ttk

 
root=Tk()
text=Text(root,height=2,width=30)
text.pack()

var = IntVar()
R1 = Radiobutton(root, text="Option 1", variable=var, value=1)
R1.pack(anchor=W)
R2 = Radiobutton(root, text="Option 2", variable=var, value=2)
R2.pack(anchor=W)

combo = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"])
combo.pack()


Checkbutton(root,text="new").pack()
Checkbutton(root,text="new1").pack()
root.mainloop()
