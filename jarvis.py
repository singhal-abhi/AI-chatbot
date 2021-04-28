import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyaudio
import aiml


kernel = aiml.Kernel()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
terminate = ['bye', 'buy', 'shutdown', 'exit', 'quit', 'gotosleep', 'goodbye']

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
    speak("I am Jarvis. Please tell me how may I help you?")

def takeCommand(i):
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        try:
            audio = r.listen(source,timeout=10)
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

if __name__ == "__main__":
    i=0
    s="Please enter your username"
    print(s)
    speak(s)
    print("Listening...")
    #sessionid='abhi'
    sessionid=takeCommand(0)
    wishMe(sessionid)
    while True:
    #if(1):
        print("Listening...")
        query = takeCommand(i).lower()
        #query='open msedge'
        if 'visit' in query:
            s=query.split()
            msedge.open(s[s.index("visit")+1]+'.com')

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
            if os.path.isfile("brain.brn"):
                #print("i have learnt")
                kernel.bootstrap(brainFile='brain.brn')
                kernel.loadBrain("brain.brn")
            else:
                kernel.bootstrap(learnFiles = "startup.aiml", commands = "load aiml b")
                kernel.saveBrain("brain.brn")
                #print("i am learning")
            #kernel.learn("sample.aiml")
            kernel.saveBrain("brain.brn")
            kernel.setPredicate("site",'google')
            site=kernel.getPredicate("site")
            #print(site)
            response = kernel.respond(query)
            print(response)
            speak(response)
