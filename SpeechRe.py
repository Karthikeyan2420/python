import speech_recognition as sr
# def main():
#      r=sr.Recognizer()
#      with sr.Microphone() as source:
#         print("say something....")
#         audio=r.listen(source)
#      try:
#       print("Reconizing Now...")
#       text=r.recognize_google(audio)
#       print(text)
#      except Exception as e:
#         print("Error :"+str(e))

# if __name__=="__main__":
#     main()
#
# import webbrowser as wb
# import speech_recognition as sr
# r = sr.Recognizer()
# url="https://www.google.co.in/search?q="
# with sr.Microphone() as source:
#         r.adjust_for_ambient_noise(source=source)
#         audio = r.listen(source,timeout=3)
#         data = ''
#         try :
#             data = r.recognize_google(audio)
#             print(data)
#             wb.get().open_new(url+data)
#         except sr.UnknownValueError:
#             print(" Error")
#
#         except sr.RequestError as e:
#             print("Request Error")








#
# from tkinter import *
# r1=Tk()
# r1.geometry("400x400")
# import speech_recognition as sr
# def main1():
#      r=sr.Recognizer()
#      with sr.Microphone() as source:
#         print("say something....")
#         audio=r.listen(source)
#      try:
#       print("Reconizing Now...")
#       text=str(r.recognize_google(audio))
#       Label(r1,text=text).grid(row=4,column=3)
#      except Exception as e:
#         print("Error :"+str(e))
#
#
#
# l1=Label(r1,text="Speech Recognition")
# l1.grid(row=0,column=1)
# l2=Label(r1,text="Click the Button and Speak")
# l2.grid(row=1,column=1)
# b=Button(r1,text="Speak",command=lambda:main1())
# b.grid(row=3,column=3)
#
# r1.mainloop()


#
# import pyttsx3
# engine = pyttsx3.init()
# engine.say("Welcome to Live wire")
# engine.runAndWait()
# print("yes")

#
import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 100)
volume = engine.getProperty('volume')
engine.setProperty('volume',1.0) #o to 1
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("Welcome to Live wire, I am New Program , pyttsx3 is my Package,")
engine.runAndWait()
engine.stop()

# """Saving Voice to a file"""
# # engine.save_to_file('Hello World', 'test.mp3')
# #engine.runAndWait()
