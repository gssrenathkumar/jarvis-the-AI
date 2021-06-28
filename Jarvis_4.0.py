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
import pywhatkit as pyt
import requests
from newsapi import NewsApiClient
import clipboard
import os
import pyjokes
import time as tt
import psutil
from nltk.tokenize import word_tokenize
from email.message import EmailMessage
import yfinance as yf 
import playsound
import playsound
import random



engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('volume',1)
wakeword="jarvis"



def there_exists(terms):
    for term in terms:
        if term in query:
            return True

def there_exists1(terms):
    for term in terms:
        if term in query:
            return True






def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print(f"Jarvis: {audio}")


def time():
    Time = datetime.datetime.now().strftime("%I:%M")
    speak("Sir The time is:")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("Sir The current date is:")
    speak(date)
    speak(month)
    speak(year)


def getvoices(voice):
    voices = engine.getProperty('voices')
    if voice == 1:
        engine.setProperty('voice', voices[1].id)

    if voice == 2:
        engine.setProperty('voice', voices[2].id)


def wishme():
    greeting()
    speak("Jarvis at your service, how can i help you")


def wishme1():
    greeting2()
    speak("Friday at your service")
    speak("how can i help you")


def wishme2():
    speak("Jarvis at your service")
    speak("how can i help you")



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

def greeting2():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning Boss!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon Boss!")
    elif hour >= 18 and hour < 24:
        speak("Good Everning Boss!")
    else:
        speak("Good Night Sir")





def takeCommandMic():
    r = sr.Recognizer()
    print("Please Talk")
    with sr.Microphone() as source:
        print("Listerning you....")
        r.pause_threshold = 1
        audio = r.listen(source ,timeout=1, phrase_time_limit=2)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language="en-IN")
        print(f"You: {query}")
        
    except Exception as e:
        print(e)
        return "none"
    return query


def sendEmail(receiver,subject,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("YOUR EMAIL ID", "PASSWORD")
    email=EmailMessage()
    email["From"]="FROM EMAIL ID"
    email["To"]=receiver
    email["Subject"]=subject
    email.set_content(content)
    server.send_message(email)
    server.close()



def sendwhatsmsg(phone_no,message):
    Message=message
    wb.open("https://web.whatsapp.com/send?phone="+phone_no+'&text='+Message)
    sleep(15)
    pyautogui.press("Enter")


def searchgoogle():
    speak("What should I Search Sir")
    search = takeCommandMic()
    if search == "none":
        speak("ok sir")
        wb.open('https://www.google.com/')
    else:
        speak("ok sir")
        wb.open('https://www.google.com/search?q='+search)
   
   



def news():
            newsapi=NewsApiClient(api_key="YOUR API KEY")
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
    name_img = "FILE LOCATION".format(name_img)
    img =pyautogui.screenshot(name_img)
    speak("Screenshot taken successfully")
    img.show()


def flip():
    speak("Ok Sir,Flipping a coin for you")
    coin = ["heads","tails"]
    toss = []
    toss.extend(coin)
    random.shuffle(toss)
    toss=("".join(toss[0]))
    speak("I flipped the coin and you got "+toss)


def cpu():
    usage =str(psutil.cpu_percent())
    speak("CPU is at"+usage)
    




if __name__ == "__main__":
    wishme()
    
    while True:
        query = takeCommandMic().lower()
        query1=query
        query = word_tokenize(query)
        print(query)


       
      
        if there_exists(["date"]):
            date()
        elif there_exists(["thank you","you","thank"]):
            speak("I am Here to Serve you sir")
        
        #elif there_exists(["time","timings"]):
         #   time()

        elif there_exists(["Friday","friday"]):
            speak("Ok Sir Switching to Friday")
            getvoices(2)
            wishme1()
        
        elif there_exists(["jarvis","service","wake up","up","wake"]):
            speak("I am Listening Sir")
        
        elif there_exists(["friday"]):
            speak("Yes Boss")
        
        elif there_exists(["switch to jarvis","24"]):
            wakeword="jarvis"
            speak("OK sir Switching to Jarvis")
            getvoices(1)
            speak("Welcome Back Home")
            wishme2()

        elif there_exists(["personal","personal gmail"]):
            wb.open("https://mail.google.com/mail/u/0/#inbox")
            
        
      
            
        
        elif there_exists(["instagram","status of my instagram page"]):
           
            wb.open("https://www.instagram.com/")
            

        

        elif there_exists(["email"]):
            email_list={
                "LIST1":"YOUR MAIL ID"

            }
            try:
                speak("To whom do you want to send the mail")
                name=takeCommandMic()
                receiver = email_list[name]
                speak("What is the subject do I need to add  it")
                subject=takeCommandMic()
                speak('What is the message should i say ')
                content= takeCommandMic()
                sendEmail(receiver,subject,content)
                speak("Email has been send successfully")
            except Exception as e:
                print(e)
                speak("Unable to send the Email I am  Sorry")
            
        elif there_exists(["whatsapp"]):
            speak("ok sir")
            wb.open("https://web.whatsapp.com/")
            

        
       
           


        elif there_exists(["message"]):
            
            user_name={
                "PHONE NUMBER":"NUMBER"
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

        elif there_exists(["wikipedia"]):
            speak("Searching on wikipedia...")
            query1= query1.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)
            speak("That's End of the Speech")

        elif there_exists(["search","google"]):
            try:
                
                searchgoogle()
                
            except Exception as e:
                       wb.open('https://www.google.com/')
        
        elif there_exists(["linkdin","linkedin"]):
            speak("ok sir")
            wb.open('https://www.linkedin.com/feed/')
            
        
        
            

        elif there_exists(["youtube"]):
            speak("What should i want to play sir")
            topic=takeCommandMic()
            if topic ==  "none":
                speak("ok sir")
                wb.open("https://youtube.com")
                
            else:
                speak("ok sir")
                pywhatkit.playonyt(topic)
                

        elif there_exists(["who","created you "]):
            print("I was created by Srenath Kumar")
            print("My Founder is just a first year student of Sri Ramachandra Institute of Higher Education and Research")
            speak("I was created by Srenath Kumar")
            speak("My Founder is just a first year student of Sri Ramachandra Institute of Higher Education and Research")
        
      
        
       
            
        
  
            
        
        elif there_exists(["switch to edit mode","mode","hardware mode"]):
            codepath="PATH FILE"
            
            speak("Please wait a While")
            sleep(3)   
            speak("Switched to Edit Mode Successfully ")
            os.startfile(codepath)
            

        


        elif there_exists(["weather","temperature","temp"]):

            if there_exists1(["sriperumbudur","home"]):
                url="API URL"

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

            else:
                speak("Which city do you want Sir")
                city=takeCommandMic()

                url =f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=3a6f8ab0baa30a8b0daeee22bf8fc927"

                res=requests.get(url)
                data=res.json()

                weather = data["weather"] [0] ['main']
                temp=data['main']['temp']
                desp=data['weather'][0]["description"]
                temp = round((temp - 32)* 5/9)
                print(weather)
                print(temp)
                print(desp)
                speak(f"The current temperature in {city} is")
                speak('{} degree celcius'.format(temp))
                speak("Weather is  {}".format(desp))

        elif there_exists(["news"]):
            news()

        elif  there_exists(["read"]):
            text2speech()

        elif there_exists(["visual studio","visual","studio","vs code","vs","code"]):
            print("Opened")
            speak("Ok Sir")
            codepath="FILE PATH"
            os.startfile(codepath)
           
            

        elif there_exists(["joke","jokes"]):
            speak(pyjokes.get_joke())

        elif there_exists(["screenshot","screen","shot"]):
            screenshot()


        elif there_exists(["remember","that","remember that"]):
            speak("What should i Remember Sir")
            data=takeCommandMic()
            speak("You said me to remember that"+data)
            remember=open("FILE PATH",'a')
            remember.write(data)
            remember.close()

        elif there_exists(["do you know anything","know","anything"]):
            remember=open("FILE PATH","r")
            speak("You told me to remember that" + remember.read())

        elif there_exists(["flip"]):
            flip()

        elif there_exists(["cpu"]):
            cpu()
        
        

        elif there_exists(["take some notes","notes"]):
            speak("Sir What should i note down")
            notes=takeCommandMic()
            file=open('FILE PATH',"a")
            speak("Sir should I need to inclue data and Time")
            ans=takeCommandMic()
            if there_exists(["yes","sure"]):
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak("Done Taking notes Sir")
            else:
                file.write(notes)
        
        elif there_exists(["track the location","locate","map","maps","track","location"]):
            speak("Which place do you want")
            location=takeCommandMic()
            speak("Tracing the location"+location)
            wb.open("https://www.google.com/maps/place/"+location)
            
        elif there_exists(["show notes","show"]):
            speak("Showing the notes")
            file=open("notes.txt","r")
            print(file.read())
            speak(file.read())

        elif there_exists(["go offline","offline","exit","break","goa","flight"]):
            speak("Have A Nice Day Sir")
            exit()













