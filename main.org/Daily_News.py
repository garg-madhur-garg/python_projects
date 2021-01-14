def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


if __name__ == '__main__':
    import requests
    import json
    r = requests.get("http://newsapi.org/v2/top-headlines?"
                     "country=in&category=entertainment&"
                     "apiKey=ff09896459f64308b8cb94248cf85138")

    under = json.loads(r.text)     # string convert into python object
    for i in range(11):
        speak(under["articles"][i]["title"])
