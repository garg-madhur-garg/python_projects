import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1])
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = datetime.datetime.now().hour
    if 0 < hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am jarvis sir, please tell me  how may i help you")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining....")
        r.pause_threshold = 0.6
        # r.energy_threshold = 300
        # r.operation_timeout = 5
        r.adjust_for_ambient_noise(source, duration=4)
        audio = r.listen(source)
    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said {query}\n")

    except Exception as e:
        print(e)
        print("Please speak again")
        return "None"
    return query


if __name__ == '__main__':
    # speak(f"My name is madhur")
    wishme()
    while True:
        query = takecommand().lower()
        if "wikipedia" in query:
            speak("Searching wikipedia..")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "exit" in query:
            quit()

        elif "quit" in query:
            quit()

        