from tkinter import *
from tkinter import ttk
z=Tk()
z.title("Countries and their Capitals")
z.geometry('400x400')
combo = ttk.Combobox(z, values=["INDIA", "JAPAN" , "AMERICA" , "CHINA"])
combo.pack()
combo1= ttk.Combobox(z)
combo1.pack()


def option_selected(event):
   selected_option = combo.get()
   print("You selected:", selected_option)
   if selected_option=="INDIA":
      combo1.config(values=["New delhi"])

   if selected_option=="AMERICA":
      combo1.config(values=["Washington D.C"])

   if selected_option=="CHINA":
      combo1.config(values=["Beijing"])

   if selected_option=="JAPAN":
      combo1.config(values=["Tokyo"])
      
   
combo.bind("<<ComboboxSelected>>", option_selected)
   
combo.bind("<<ComboboxSelected>>", option_selected)
   
combo.bind("<<ComboboxSelected>>", option_selected)
   
combo.bind("<<ComboboxSelected>>", option_selected)


z.mainloop()



