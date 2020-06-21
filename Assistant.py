#pip install speechrecognition
#pip install gtts
#pip install wikipedia
#pipwin install pyaudio
#pip install schedule
#import neccassary modules
import os
import speech_recognition as sr
from gtts import gTTS
import wikipedia
import calendar
import random
from time import ctime
import playsound
import sched
from datetime import datetime
import time as time_module
import webbrowser

#Start listening from microphone
def RecordAudio(ask = False):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Please say something:")
        audio = r.listen(source)

    data = ''
    try:
        data = r.recognize_google(audio)
    except sr.UnknownValueError:
        re = random.choice(["I didn't quite undertsand that, please repeat","I was having a little trouble hearing you, please say that again", "Can you repeat what you just said"])
        Assistantspeech(re)
    except sr.RequestError as e:
        Assistantspeech("My services are currently down, please wait")
    return data


def Response(data):
    if "computer" in data:
        if "what time is it" in data:
            Assistantspeech("The time is " + ctime())
        if "what is the time" in data:
            Assistantspeech("The time is " + ctime())
        if "search" in data:
            Assistantspeech("What do you want to search for")
            search = RecordAudio("What do you want to search")
            print(search)
            url = "https://google.com/search?q=" + search
            webbrowser.get().open(url)
            Assistantspeech("Here is what I found for " + search)
        if "open" in data:
            Assistantspeech("What do you want to open")
            openobj = RecordAudio("What do you want to open")
            print(openobj)
            url = "https://www." + openobj
            webbrowser.get().open(url)
            Assistantspeech("Here is what I opened ")
        if "create" in data:
            if "new file" in data:
                Assistantspeech("What is the name of the file")
                filename = RecordAudio("What do you want to create")
                Assistantspeech("What is the extension of the file")
                extension = RecordAudio("What do you want to create")
                print(extension)
                os.chdir(r"C:\Users\pradh\Desktop")
                f = open(filename+"."+extension, "w+")
                f.close()
                Assistantspeech("I have created the file")
            if "new coding project" in data:
                Assistantspeech("ok")
                os.system("code .")
                Assistantspeech("Done")
    if "exit" in data:
        exit()
    if "thank you" in data:
        r = random.choice(["You're welcome","My pleasure"])
        Assistantspeech(r)


def Assistantspeech(string):
    speech = gTTS(text= string, lang='en')
    speech.save("Assistant.mp3")
    playsound.playsound("Assistant.mp3")
    os.remove("Assistant.mp3")
    print(string)






while True:
    data = RecordAudio()
    Response(data)
