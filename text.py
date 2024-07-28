from tkinter import *
def onclick():
    pass
root=Tk()
text=Text(root,height=2,width=30)
text.insert(INSERT,"Hello....")
text.insert(END,"Bye Bye.....")
text.pack()
b=Button(root,text="submit")
b.pack()
text.tag_add("here","1.2","1.5")
text.tag_add("start","1.7","1.13")
text.tag_config("here",background="orange",foreground="blue")
text.tag_config("start",background="black",foreground="violet")
root.mainloop()
