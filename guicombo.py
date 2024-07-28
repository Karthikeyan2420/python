from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Combobox Example")
root.geometry('300x300')
combo = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"])
combo.pack()
combo1 = ttk.Combobox(root)
combo1.pack()

def option_selected(event):
   selected_option = combo.get()
   print("You selected:", selected_option)
   if selected_option=="Option 1":
      combo1.config(values=["kh","kjlj"])
   
combo.bind("<<ComboboxSelected>>", option_selected)
root.mainloop()

