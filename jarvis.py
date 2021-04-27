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
engine.setProperty('voice', voices[0].id)
terminate = ['bye', 'buy', 'shutdown', 'exit', 'quit', 'gotosleep', 'goodbye']

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis. Please tell me how may I help you?")


def takeCommand(i):
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        try:
            audio = r.listen(source,timeout=5)
        except:
            if(i>=2):
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

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
        i+=1
    return query

if __name__ == "__main__":
    wishMe()
    i=0
    while True:
        print("Listening...")
        query = takeCommand(i).lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

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
                #print("i have learnt")
                kernel.loadBrain("brain.dump")
            else:
                kernel.bootstrap(learnFiles = "startup.aiml", commands = "load aiml b")
                kernel.saveBrain("brain.dump")
                #print("i am learning")
            #kernel.learn("sample.aiml")
            response = kernel.respond(query)
            print(response)
            speak(response)
