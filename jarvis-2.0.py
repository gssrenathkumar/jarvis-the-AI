import random
import pyttsx3
import datetime
import speech_recognition as sr
import pyautogui
import webbrowser as wb
import smtplib
from time import sleep
import wikipedia
import pywhatkit
import requests
from newsapi import NewsApiClient
import clipboard
import os
import pyjokes
import time as tt
import psutil
from nltk.tokenize import word_tokenize


engine = pyttsx3.init()


# This pyttsx3 helps to convert the text into speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M")
    speak("The time is:")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is:")
    speak(date)
    speak(month)
    speak(year)


def getvoices(voice):
    voices = engine.getProperty('voices')
    if voice == 1:
        engine.setProperty('voice', voices[1].id)
        speak("Hello this is Jarvis")

    if voice == 2:
        engine.setProperty('voice', voices[1].id)
        speak("Hello this is Friday")


def wishme():
    greeting()
    speak("Jarvis at your service, how can i help you")


def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon Sir!")
    elif hour >= 18 and hour < 24:
        speak("Good Everning Sir!")
    else:
        speak("Good Night Sir")


def takeCommandCMD():
    query = input("Please tell me how can i help you")
    return query


def takeCommandMic():
    r = sr.Recognizer()
    print("Please Talk")
    with sr.Microphone() as source:
        print("Listerning you....")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=4)



    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language="en-IN")
        print(query)
    except Exception as e:
        print(e)
        return "None"
    return query

def sendEmail(content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("jarvisai@gmail.com", "srenath2002")
    server.sendmail("jarvisai@gmail.com", "srenathcoursera2002@gmail.com", content)
    server.close()

def sendwhatsmsg(phone_no,message):
    Message=message
    wb.open("https://web.whatsapp.com/send?phone="+phone_no+'&text='+Message)
    sleep(10)
    pyautogui.press("enter")

def searchgoogle():
    speak("What should I Search Sir")
    search = takeCommandMic()
    wb.open('https://www.google.com/search?q='+search)

def news():
    newsapi=NewsApiClient(api_key="")
    speak("Topic of the news Sir ")
    topic=takeCommandMic()
    data = newsapi.get_top_headlines(q=topic,
                                     language="en",
                                     page_size=5)
    newsdata = data["articles"]
    for x,y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak(f'{x}{y["description"]}')
    speak("That's all about the news i will update in some time")

def text2speech():
    text=clipboard.paste()
    print(text)
    speak(text)

def screenshot():
    name_img = tt.time()
    name_img = "C:\\Users\\srena\\Pictures\\Screenshots\\{}.png".format(name_img)
    img =pyautogui.screenshot(name_img)
    speak("Screenshot taken successfully")
    img.show()

def flip():
    speak("Ok sir,Flipping a coin for you")
    coin = ["heads","tails"]
    toss = []
    toss.extend(coin)
    random.shuffle(toss)
    toss=("".join(toss[0]))
    speak("I flipped the coin and you got "+toss)

def cpu():
    usage =str(psutil.cpu_percent())
    speak("CPU is at"+usage)
    battery=psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)



if __name__ == "__main__":
    speak("Hello this is jarvis")
    #getvoices(1)
    #wishme()
    wakeword="jarvis"
    while True:
        query = takeCommandMic().lower()
        query = word_tokenize(query)
        print(query)

        if wakeword  in query:

            if 'time' in query:
                time()

            elif 'date' in query:
                date()
            elif 'email' in query:
                try:
                    speak('What is the message should i say ')
                    content= takeCommandMic()
                    sendEmail(content)
                    speak("Email has been send successfully")
                except Exception as e:
                    print(e)
                    speak("Unable to send the Email I , am , Sorry")
            elif "message" in query:
                user_name={
                    "your_name":"your_number"
                }
                try:
                    speak("To whom you want to send the whats app message")
                    name=takeCommandMic()
                    print(name)
                    phone_no=user_name[name]
                    speak("What is the message")
                    message=takeCommandMic()
                    sendwhatsmsg(phone_no,message)
                    speak("Message has been sent")

                except Exception as e:
                    print(e)
                    speak("unable to send the message")

            elif "wikipedia" in query:
                speak("Searching on wikipedia...")
                query= query.replace("wikipedia","")
                result=wikipedia.summary(query,sentences=2)
                print(result)
                speak(result)

            elif "search" in query:
                searchgoogle()

            elif "youtube" in query:
                speak("What should i want to play sir")
                topic=takeCommandMic()
                pywhatkit.playonyt(topic)

            elif "weather" in query:

                url =""

                res=requests.get(url)
                data=res.json()

                weather = data["weather"] [0] ['main']
                temp=data['main']['temp']
                desp=data['weather'][0]["description"]
                temp = round((temp - 32)* 5/9)
                print(weather)
                print(temp)
                print(desp)
                speak("The current temperature in Sriperumbudur is")
                speak('{} degree celcius'.format(temp))
                speak("Weather is  {}".format(desp))

            elif "news" in query:
                news()

            elif  "read" in query:
                text2speech()

            elif "vs" in query:
                codepath="C:\\Users\\srena\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codepath)
                print("Opened")
            elif "learning" in query:
                codepath1="D:\Learning"
                os.startfile(codepath1)
                print("opened")

            elif "joke" in query:
                speak(pyjokes.get_joke())

            elif "screenshot" in query:
                screenshot()

            elif "remember that" in query:
                speak("What should i Remember Sir")
                data=takeCommandMic()
                speak("You said me to remember that"+data)
                remember=open("D:\\\Learning\\data.txt",'a')
                remember.write(data)
                remember.close()

            elif "do you know anything" in query:
                remember=open("File path","r")
                speak("You told me to remember that" + remember.read())

            elif "flip" in query:
                flip()

            elif "cpu" in query:
                cpu()





            elif "exit" in query:
                exit()













