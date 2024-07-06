import tkinter
from tkinter import*
from tkinter import ttk,font
from PIL import ImageTk,Image


def customerlog(r):
    r.destroy()
    r=Tk()
    r.geometry("1500x720")
    r.title("Bank")
    frame=Frame(r,width=1500,height=50,bg="yellow")
    frame.pack()
    f=font.Font(weight="bold",family="times new roman",size=25)
    x=Label(frame,text="Madhan Bank",font=f)
    x.configure(bg="yellow",fg="black")
    x.place(relx=.45,rely=.1)

    frame=Frame(r,width=500,height=250,bg="#4FD6F7").place(relx=.35,rely=.3)
    f=font.Font(r,weight="bold",family="times new roman",size=20)
    l=Label(frame,text="CUSTOMER LOGIN",font=f,bg="#4FD6F7").place(relx=.45,rely=.3)
    
    e=font.Font(r,weight="bold",family="times new roman",size=15)
    l=Label(frame,text="Customer ID:",font=e,bg="#4FD6F7").place(relx=.38,rely=.4)
    l=Label(frame,text="Password:",font=e,bg="#4FD6F7").place(relx=.38,rely=.5)
    
    l1=Entry(frame)
    l1.place(relx=.48,rely=.41)
    l2=Entry(frame)
    l2.place(relx=.48,rely=.51)
    b=Button(frame,text="Login",font=e,bg="red").place(relx=.48,rely=.57)

    frame=Frame(r,width=1500,height=50,bg="yellow")
    frame.pack()
    frame.place(relx=.0,rely=.94)
    f=font.Font(r,weight="bold",family="times new roman",size=15)
    x=Label(frame,text=" © CopyRight 2024 Madhan",font=f)
    x.configure(bg="yellow",fg="black")
    x.place(relx=.40,rely=.1)
    r.mainloop()
def file(a,b,c,d,r):
    n=a+" "+b+" "+c+" "+d+"\n"
    f=open("myfile.txt","a")
    f.write(n)

def customer_reg(r):
    r.destroy()
    r=Tk()
    r.geometry("1500x720")
    r.title("Bank")
    frame=Frame(r,width=1500,height=50,bg="yellow")
    frame.pack()
    f=font.Font(weight="bold",family="times new roman",size=25)
    x=Label(frame,text="Madhan Bank",font=f)
    x.configure(bg="yellow",fg="black")
    x.place(relx=.45,rely=.1)

    frame=Frame(r,width=500,height=590,bg="#4FD6F7").place(relx=.33,rely=.1)
    f=font.Font(r,weight="bold",family="times new roman",size=20)
    l=Label(frame,text="CUSTOMER REGISTER",font=f,bg="#4FD6F7").place(relx=.40,rely=.12)

    e=font.Font(r,weight="bold",family="times new roman",size=17)
    l=Label(frame,text="Name:",font=e,bg="#4FD6F7").place(relx=.38,rely=.23)
    l=Label(frame,text="Aadhar No:",font=e,bg="#4FD6F7").place(relx=.38,rely=.32)
    l=Label(frame,text="PAN No:",font=e,bg="#4FD6F7").place(relx=.38,rely=.43)
    l=Label(frame,text="Phone No:",font=e,bg="#4FD6F7").place(relx=.38,rely=.54)


   
    l1=Entry(frame)
    l1.place(relx=.50,rely=.24)
    l2=Entry(frame)
    l2.place(relx=.50,rely=.33)
    l3=Entry(frame)
    l3.place(relx=.50,rely=.44)
    l4=Entry(frame)
    l4.place(relx=.50,rely=.55)

    b=Button(frame,text="Register",font=e,bg="#de9e4b",command=lambda:file(l1.get(),l2.get(),l3.get(),l4.get(),r))
    b.place(relx=.47,rely=.65)

    
    frame=Frame(r,width=1500,height=50,bg="yellow")
    frame.pack()
    frame.place(relx=.0,rely=.94)
    f=font.Font(r,weight="bold",family="times new roman",size=15)
    x=Label(frame,text=" © CopyRight 2024 Madhan",font=f)
    x.configure(bg="yellow",fg="black")
    x.place(relx=.40,rely=.1)
    r.mainloop()


def adminpage(r):

    r.destroy()
    r=Tk()
    r.geometry("1500x720")
    r.title("Bank")
    frame=Frame(r,width=1500,height=50,bg="yellow")
    frame.pack()
    f=font.Font(weight="bold",family="times new roman",size=25)
    x=Label(frame,text="Madhan Bank",font=f)
    x.configure(bg="yellow",fg="black")
    x.place(relx=.45,rely=.1)

    frame=Frame(r,width=500,height=590,bg="#4FD6F7").place(relx=.01,rely=.1)
    f=font.Font(r,weight="bold",family="times new roman",size=20)
    l=Label(frame,text="CUSTOMER REGISTER",font=f,bg="#4FD6F7").place(relx=.07,rely=.12)

    e=font.Font(r,weight="bold",family="times new roman",size=17)
    l=Label(frame,text="Name:",font=e,bg="#4FD6F7").place(relx=.05,rely=.23)
    l=Label(frame,text="Aadhar No:",font=e,bg="#4FD6F7").place(relx=.05,rely=.32)
    l=Label(frame,text="PAN No:",font=e,bg="#4FD6F7").place(relx=.05,rely=.43)
    l=Label(frame,text="Phone No:",font=e,bg="#4FD6F7").place(relx=.05,rely=.54)
    l=Label(frame,text="Mail ID :",font=e,bg="#4FD6F7").place(relx=.05,rely=.65)
    l=Label(frame,text="Address:",font=e,bg="#4FD6F7").place(relx=.05,rely=.75)

    b=Button(frame,text="Register",font=e,bg="#de9e4b").place(relx=.14,rely=.85)

    l1=Entry(frame)
    l1.place(relx=.17,rely=.24)
    l2=Entry(frame)
    l2.place(relx=.17,rely=.33)
    l3=Entry(frame)
    l3.place(relx=.17,rely=.44)
    l4=Entry(frame)
    l4.place(relx=.17,rely=.55)
    l5=Entry(frame)
    l5.place(relx=.17,rely=.66)
    l6=Entry(frame)
    l6.place(relx=.17,rely=.76)

    frame=Frame(r,width=1500,height=50,bg="yellow")
    frame.pack()
    frame.place(relx=.0,rely=.94)
    f=font.Font(r,weight="bold",family="times new roman",size=15)
    x=Label(frame,text=" © CopyRight 2024 Madhan",font=f)
    x.configure(bg="yellow",fg="black")
    x.place(relx=.40,rely=.1)
    r.mainloop()
def admin(a,b,r):
    if(a=="admin" and b=="admin"):
        adminpage(r)
    else:
        adminlog(r)

def adminlog(r):
    r.destroy()
    r=Tk()
    r.geometry("1500x720")
    r.title("Bank")
    frame=Frame(r,width=1500,height=50,bg="yellow")
    frame.pack()
    f=font.Font(weight="bold",family="times new roman",size=25)
    x=Label(frame,text="Madhan Bank",font=f)
    x.configure(bg="yellow",fg="black")
    x.place(relx=.45,rely=.1)

    frame=Frame(r,width=500,height=250,bg="#4FD6F7").place(relx=.35,rely=.3)
    f=font.Font(r,weight="bold",family="times new roman",size=20)
    l=Label(frame,text="ADMIN LOGIN",font=f,bg="#4FD6F7").place(relx=.45,rely=.3)
    
    e=font.Font(r,weight="bold",family="times new roman",size=15)
    l=Label(frame,text="Admin ID:",font=e,bg="#4FD6F7").place(relx=.38,rely=.4)
    l=Label(frame,text="Password:",font=e,bg="#4FD6F7").place(relx=.38,rely=.5)
    
    l1=Entry(frame)
    l1.place(relx=.48,rely=.41)
    l2=Entry(frame)
    l2.place(relx=.48,rely=.51)
    b=Button(frame,text="Login",font=e,bg="red",command=lambda:admin(l1.get(),l2.get(),r)).place(relx=.48,rely=.57)

    frame=Frame(r,width=1500,height=50,bg="yellow")
    frame.pack()
    frame.place(relx=.0,rely=.94)
    f=font.Font(r,weight="bold",family="times new roman",size=15)
    x=Label(frame,text=" © CopyRight 2024 Madhan",font=f)
    x.configure(bg="yellow",fg="black")
    x.place(relx=.40,rely=.1)
    r.mainloop()


def Home():
    #Home page
    r=Tk() 
    r.geometry("1500x720")
    r.title("Bank")
    frame=Frame(r,width=1500,height=50,bg="yellow")
    frame.pack()
    f=font.Font(weight="bold",family="times new roman",size=25)
    x=Label(frame,text="Madhan Bank",font=f)
    x.configure(bg="yellow",fg="black")
    x.place(relx=.45,rely=.1)

    frame=Frame(r,width=100,height=100)
    frame.place(anchor="s",relx=.05,rely=.3)
    """ img=ImageTk.PhotoImage(Image.open("bank1.jpg"))
    label=Label(frame,image=img)
    label.pack()  """

    f=font.Font(weight="bold",family="times new roman",size=20)
    t="""A bank is a financial institution that accepts deposits from the public
    and creates a demand deposit while simultaneously making loans.
    Lending activities can be directly performed by the bank or indirectly through capital markets."""
    l=Label(r,text=t,font=f).place(relx=.13,rely=.2)

    b=Button(r,text="Customer Login",font=f,bg="skyblue",activebackground="#FC92C4",command=lambda:customerlog(r)).place(relx=.10,rely=.5)
    c=Button(r,text="Customer Register",font=f,bg="skyblue",activebackground="#FC92C4",command=lambda:customer_reg(r)).place(relx=.40,rely=.5)
    d=Button(r,text="Admin Login",font=f,bg="skyblue",activebackground="#FC92C4",command=lambda:adminlog(r)).place(relx=.71,rely=.5)
    
    frame=Frame(r,width=1500,height=50,bg="yellow") 
    frame.pack()
    frame.place(relx=.0,rely=.94)
    f=font.Font(r,weight="bold",family="times new roman",size=15)
    x=Label(frame,text=" © CopyRight 2024 Madhan",font=f)
    x.configure(bg="yellow",fg="black")
    x.place(relx=.40,rely=.1)
    r.mainloop()



Home()

