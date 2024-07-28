from tkinter import font
import webbrowser as wb
import speech_recognition as sr
import pyttsx3

def main1():
     r=sr.Recognizer()
     with sr.Microphone() as source:
        print("say something....")
        audio=r.listen(source)
     try:
      print("Recognizing Now...")
      text=str(r.recognize_google(audio))
      print(text)
      if "google" in text.lower():
          print("1")
          url="https://www.google.com/search?q="
          wb.get().open_new(url+text)  
      if "youtube" in text.lower():
          url="https://www.youtube.com/results?search_query="
          wb.get().open_new(url+text)
        
      if "how are you" in text:
            engine = pyttsx3.init()
            engine.setProperty('rate', 100)
             
            engine.setProperty('volume',1.0) #o to 1
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
            engine.say("yes i am fine and you!")
            engine.runAndWait()
            engine.stop()
        
        
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
