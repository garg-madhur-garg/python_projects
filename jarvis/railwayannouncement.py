import pyaudio
import pandas as pd
from gtts import gTTS
from pydub import AudioSegment


def text_to_speech(text, filename):
    text = str(text)
    speech = gTTS(text=text, lang="hi")
    speech.save(filename)


def generating_skeleton():
    audio = AudioSegment.from_file("railway.mp3")

    # 1 - Generate Kripya Dhyan dijiye

    start = 88000
    finish = 90200
    audio_process = audio[start:finish]
    audio_process.export("1_hindi.mp3", format="mp3")

#    2 - Generate from-city

#    3 - generate se chalkar
    start = 91000
    finish = 92200
    audio_process = audio[start:finish]
    audio_process.export("3_hindi.mp3", format="mp3")

#    4 - via-city

#    5 - ke raste
    start = 94000
    finish = 95000
    audio_process = audio[start:finish]
    audio_process.export("5_hindi.mp3", format="mp3")

#    6 - destination

#    7 - generate ko jane bali gari sankhya
    start = 96000
    finish = 98800
    audio_process = audio[start:finish]
    audio_process.export("7_hindi.mp3", format="mp3")

#    8 - Generating train number and name

#    9 - generating kuch hi samay mai platform sankhya
    start = 105500
    finish = 108200
    audio_process = audio[start:finish]
    audio_process.export("9_hindi.mp3", format="mp3")

#    10 - platform number

#    11 - generating par a rhi hai
    start = 109000
    finish = 112250
    audio_process = audio[start:finish]
    audio_process.export("11_hindi.mp3", format="mp3")


def merge_mp3(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined


def generate_announcement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
        # 2 - Generate from-city
        text_to_speech(item['from'], "2_hindi.mp3")

        # 4 - via-city
        text_to_speech(item['via'], "4_hindi.mp3")

        # 6 - destination
        text_to_speech(item['to'], "6_hindi.mp3")

        # 8 - Generating train number and name
        text_to_speech(item['train_no'] + " " + item['train_name'], "8_hindi.mp3")

        # 10 - platform number
        text_to_speech(item['platform'], "10_hindi.mp3")

        audios = [f"{i}_hindi.mp3" for i in range(1, 12)]

        announcement = merge_mp3(audios)
        announcement.export(f"announcement_{item['train_no']}_{index+1}.mp3", format="mp3")


if __name__ == '__main__':
    print("Generating skeleton...")
    generating_skeleton()
    print("generating announcement")
    generate_announcement("announce_hindi.xlsx")