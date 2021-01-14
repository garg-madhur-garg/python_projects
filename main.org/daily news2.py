def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


if __name__ == '__main__':
    import requests
    import json
    responce = requests.get("http://newsapi.org/v2/top-headlines?"
                            "country=in&category=entertainment&"
                            "apiKey=ff09896459f64308b8cb94248cf85138")

    load = json.loads(responce.text)
    speak("here you listen top 10 news. Lets begin")
    speak("first news is")
    for i in range(10):

        print(load["articles"][i]["title"])
        speak(load["articles"][i]["title"])
        speak("next news is")
