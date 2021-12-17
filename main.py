import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import time
import pyaudio
soundObj = pyaudio.PyAudio()

# Learn what your OS+Hardware can do
# defaultCapability = soundObj.get_default_host_api_info()
# print (defaultCapability)

# # See if you can make it do what you want
# isSupported = soundObj.is_format_supported(input_format=pyaudio.paInt8, input_channels=1, rate=22050, input_device=0)
# print (isSupported)
engine=pyttsx3.init("sapi5")
voices=engine.getProperty('voices')

engine.setProperty('voices' , voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour>12:
        speak("Good morning sir . How may i help you?")

    elif hour<12 and hour>18:
        speak("Good afternoon sir . How may i help you?")

    else:
        speak("Good evening sir . How may i help you?")

def takecommand():
   
    r= sr.Recognizer()
    with sr.Microphone() as source:
            print("Listening.....")
            r.pause_threshold=1
            audio=r.listen(source)
            
    try:
        print("Recognising.......")
       
        query = r.recognize_google(audio,language="en-in")
        print(f"user said : {query}\n")
        
    
    except Exception as e:
        print(e)
        print("say that again !")
        return "none"
    return query
if __name__ == "__main__":
    wish()
    while True:
        query=takecommand().lower()
        
        if "wikipedia" in query:
            try:
                speak("searching wikipedia .....")
                query=query.replace("wikipedia" , " ")
                results=wikipedia.summary(query,sentences=2)
                print(results)
                speak(results)
            except Exception as e:
                print(e)
                speak("sorry sir i am unable to find") 
        elif 'open google' in query:
            speak("ok sir opening google")
            webbrowser.open("google.com")

        elif "open youtube" in query:
            speak("ok sir opening")
            webbrowser.open("youtube.com")

        elif "open stack overflow" in query:
            speak("ok sir opening")
            webbrowser.open("stackoverflow.com")


        elif "open github" in query:
            speak("ok sir ")
            webbrowser.open("github.com")
        
        elif "open whatsapp" in query:
            speak("ok sir")
            webbrowser.open("web.whatsapp.com")
        
        elif "open sololearn" in query:
            speak("ok sir")
            webbrowser.open("sololearn.com")

        elif "search" in query:
            query=query.replace("search" , " ")
            webbrowser.open(f"{query}")
            speak("This is what i got from the search")

        elif "who is " in query:
            try:
                query=query.replace("who is " , " ")
                about=wikipedia.summary(query,sentences=1)
                speak(about)
            except Exception as e:
                details=(f"who is  {query}?")
                speak("this is what i got from search")
                webbrowser.open(f"{details}")

        # elif "play music " in query:
        #     music_dir=""
        #     songs =os.listdr(music_dir)
        #     print(songs)
        #     os.startfile(os.path.join(music_dir,songs[0]))
    
        elif "time" in query:
            

  
  
            curr_time = time.localtime() 
            curr_clock = time.strftime("%H:%M:%S", curr_time) 
  
            speak(F"Sir the time is {curr_clock}")
            
        elif "open visual" in query:
            codepath="C:\\Users\\SKYNET\\AppData\\Local\\Programs\\Microsoft VS Code\Code.exe"
            os.startfile(codepath) 
        elif "close" in query:
            speak("ok sir closing have a good day")
            break

        elif "who are you" in query:
            speak("i am your assistant Jarvis sir")
            print("i am your assistant Jarvis sir")
        elif "download" in query:
            speak("ok sir wait a second ")
            try:
                from pytube import YouTube
                speak("sir please Enter the link of youtube video which you want to download")
                link=input("enterr link")
                videos=YouTube(link).streams.all()
                speak("showing all available video qualities. please choose one")

                i=1
                for stream in videos:
                    if stream.type=="video":
                        print(str(i) + " "+ str(stream.resolution))
                        i+=1

                stream_number=int(input("Enter number from above list"))

                video=videos[stream_number-1]
                video.download("C:\\Users\\aditya\\downloads")
                speak("downloading")
                print("Downloading.......")
                speak("congratulation sir your video has been downloaded")
                print("downloaded !!")
                
            except Exception as e:
                speak("sorry sir")
                print(e)




        # except Exception    #     print("sorry sir i am unable to find it")
        #     speak("sorry sir i am unable to find it")
        
            
    