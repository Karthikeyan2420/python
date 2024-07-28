import speech_recognition as sr
import webbrowser as wb
# r=sr.Recognizer()
# url="https://www.google.co.in/search?q="
# #url="https://www.youtube.com/results?search_query="
# with sr.Microphone() as source:
#         print("speak....., It is the Google Search..., what do you want to Search..")
#         audio=r.listen(source)
#         try:
#             get=r.recognize_google(audio)
#             print(get)
#             wb.get().open_new(url+get)
#         except sr.UnknownValueError:
#             print("error")
#         except sr.RequestError as e:
#             print('failed'.format(e))
#         except:
#             print("Microphone not detected")


""" import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
 print("say something....")
 audio=r.listen(source)
try:
 print("Reconizing Now...")
 text=str(r.recognize_google(audio))
 print(text)
except Exception as e:
 print("Error :"+str(e)) """

""" 
r=sr.Recognizer()
with sr.Microphone() as source:
    print("say something....")
    audio=r.listen(source)
    try:
        print("Reconizing Now...")
        text=str(r.recognize_google(audio))
        print(text)
    except Exception as e:
        print("Error :"+str(e)) """