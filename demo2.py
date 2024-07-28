from tkinter import font
import speech_recognition as sr
def main1():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("say something....")
        audio=r.listen(source)
    try:
        print("Reconizing Now...")
        text=str(r.recognize_google(audio))
        label_font = font.Font(weight="bold",family='Times New Roman',size=10)
        Label(r1,text=text,font=label_font).place(relx=0.5,rely=0.35)
    except Exception as e:
        print("Error :"+str(e))


from tkinter import *
r1=Tk()
r1.geometry("600x400")
label_font = font.Font(weight="bold",family='Helvetica',size=30)
l1=Label(r1,text="Speech Recognition",font=label_font, bg='#0052cc', fg='#ffffff')
l1.place(anchor="center",relx=0.5,rely=0.1)

label_font = font.Font(weight="bold",family='Times New Roman',size=20)
l2=Label(r1,text="This is Example of Speech Recognition and GUI",font=label_font, bg='red', fg='#ffffff')
l2.place(anchor="center",relx=0.5,rely=0.25)

label_font = font.Font(weight="bold",family='Times New Roman',size=10)
b=Button(r1,text="It's Just a print what you Say",command=lambda:main1(),font=label_font)
b.place(relx=0.1,rely=0.35)

r1.mainloop()