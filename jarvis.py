import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyaudio
import aiml,urllib as ul


kernel = aiml.Kernel()

#voice initialization
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#keywords to terminate
terminate = ['bye', 'buy', 'shutdown', 'exit', 'quit', 'gotosleep', 'goodbye']

#web browser initialization
edgepath="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
webbrowser.register('edge',None,webbrowser.BackgroundBrowser(edgepath))

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe(s):
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!",)
    speak(s)
    speak("I am ISAC. Please tell me how may I help you?")

def takeCommand(i):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        try:
            audio = r.listen(source,timeout=8)
        except:
            if(i>=3):
                s="You appear to be working sir, Call me when required!"
                print(s)
                speak(s)
                exit()
            i+=1
            takeCommand(i)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query

    except Exception as e:
        print("Sorry, can you say that again please...\nListening...")
        i+=1
        takeCommand(i)

edgepath="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
webbrowser.register('edge',None,webbrowser.BackgroundBrowser(edgepath))

if __name__ == "__main__":
    i=0
    s="Please enter your username"
    print(s)
    speak(s)
    print("Listening...")
    sessionid='abhi'
    #sessionid=takeCommand(0)
    wishMe(sessionid)
    #while True:
    if(1):
        print("Listening...")
        #query = takeCommand(0).lower()
        query='nkjnono'
        if 'visit' in query or "take me to" in query:
            s=query.split()
            s='https://www.'+s[-1]+'.com'
            webbrowser.get('edge').open(s)

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open file' in query:
            codePath ="C:\\Windows\\explorer"
            os.startfile(codePath)

        elif any([i for i in terminate if i in query]):
            s="Bbye Sir!, Have a nice day."
            print(s)
            speak(s)
            exit(0)

        else:
            if os.path.isfile("brain.dump"):
                kernel.bootstrap("brain.dump")
            else:
                kernel.bootstrap(learnFiles = "startup.aiml", commands = "load aiml b")
                kernel.saveBrain("brain.dump")
            kernel.learn("sample.aiml")
            response = kernel.respond(query)
            print(response)
            speak(response)
