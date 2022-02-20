import datetime
import os

import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(a):
    engine.say(a)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("hi i'm javed")

def take():
    r = sr.Recognizer()
    query = ""
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recogninzing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")

    except Exception as e:
        print("Say that agian please....")

    return query

if __name__ == "__main__":
    wishme()
    run = True
    while run is True:
        query = take().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            print('searching in wikipedia')
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(result)
            speak(result)

        elif "open youtube" in query:
            # chrome=webbrowser.get("Chrome")
            # chrome.open("youtube.com",new=1)
            webbrowser.open_new_tab("youtube.com")

        elif "open google" in query:
            # chrome=webbrowser.get("Chrome")
            # chrome.open("youtube.com",new=1)
            webbrowser.open_new_tab("google.com")

        elif "open github" in query:
            # chrome=webbrowser.get("Chrome")
            # chrome.open("youtube.com",new=1)
            webbrowser.open_new_tab("github.com")

        elif "open facebook" in query:
            # chrome=webbrowser.get("Chrome")
            # chrome.open("youtube.com",new=1)
            webbrowser.open_new_tab("facebook.com")

        elif 'play music' in query:
            pass

        elif 'open vs code' in query:
            codePath= "C:\\Users\\Sumit Kumar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'send email to amit' in query:
            # try:
            #     speak("what should i say")
            #     content= take()
            pass

        elif "what's the time now" in query:
            strtime  = datetime.datetime.now().strftime("%H:%M:%S")
            print(strtime)
            speak(f"the time is {strtime}")

        elif "by javed" in query:
            run = False

        


