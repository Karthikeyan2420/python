import speech_recognition as sr
import webbrowser as wb
from tkinter import *
from tkinter import Tk
import tkinter


def sp():
 r=sr.Recognizer()
 url1="https://www.google.co.in/search?q="
 url="https://www.youtube.com/results?search_query="
 with sr.Microphone() as source:
     print("say something.....")
     audio=r.listen(source)
 try:
     print("Reconizing now.....")
     text=str(r.recognize_google(audio))
     print(text)
     wb.get().open_new(url+text) 
     wb.get().open_new(url1+text)
 except Exception as e:
     print("Error :"+str(e)) 
           



n=Tk()
n.geometry("300x300")
b=tkinter.Button(n,text="speak now",command=sp)
b.place(relx=0.1,rely=0.1)
n.mainloop()
