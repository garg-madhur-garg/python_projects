import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listing...")
        r.adjust_for_ambient_noise(source, duration=4)
        audio = r.listen(source)
    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said {query}\n")

    except Exception as e:
        print("Please speak again")
        return "None"
    return query

if __name__ == '__main__':
    # speak("My name is madhur")
    query = takecommand().lower()
    
