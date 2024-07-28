q
# import  speech_recognition as sr
# import webbrowser as wb
# r=sr.Recognizer()
# url="https://www.google.co.in/search?q="
# # url="https://www.youtube.com/results?search_query="
# with sr.Microphone()as source:
#     print("speak.....,it is the google search...'what do you want to search..")
#     audio=r.listen(source)
#     try:
#         get=r.recognize_google(audio)
#         print(get)
#         wb.get().open_new(url+get)
#     except sr.unknownvalueError:
#         print("error")
#
# import pyttsx3
# engine=pyttsx3.init()
# engine.setProperty('rate',200)
# engine.setProperty('volume',1.0)
# voices=engine.getProperty('voices')
# engine.setProperty('voices',voices[0].id)
# engine.say("welcome to livewire")
# engine.runAndWait()
# engine.stop()


import pyttsx3
engine=pyttsx3.init()
engine.save_to_file("hello world","test.mp3")
engine.runAndWait()
