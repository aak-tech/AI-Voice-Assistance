import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import datetime





engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices', voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# to convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: { query}")

    except Exception as e:
        speak("say that again please...")
        return "none"
    return query

# to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon ")
    else:
        speak("good evening")


    speak("i am jarvis sir. virtual artificial intelligence. please tell me how can i help you")


#to send email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 535)
    server.ehlo()
    server.starttls()
    server.login('your email id','your password' )
    server.sendmail('your email id', to, content)
    server.close()




if __name__ == "__main__":
    wish()
    while True:
    #if 1:

        query = takecommand().lower()

        #logic buildind for tasks

        if "open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()
        elif "play music" in query:
            music_dir = "E:\\music"
            songs = os.listdir(music_dir)
            #rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))
        elif "Ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")


        elif  "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)


        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")



        elif "open whatsapp" in query:
            webbrowser.open("www.whatsapp.com")

        elif "open google" in query:
            speak("sir, what should i search in google")
            cm = takecommand().lower()
            webbrowser = ("www.google.com")
            webbrowser.open(f"{cm}")

        elif "send message" in query:
            kit.sendwhatmsg("+919710428885","this is testing protocol",8,3)

        elif "search on youtube" in query:
            result = query.replace("search on youtube", '')
            kit.playonyt(result)

        elif "time" in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            speak(f"current time is{time}")

        elif "email to " in query:
            try:
                speak('what should i send? ')
                content = takecommand().lower()
                to = 'dakshnaaakash@gmail.com'
                sendEmail(to, content)
                speak('email has been sent ')

            except Exception as e:
                print(e)
                speak('sorry sir i am unable to send this email')


        elif "no thanks" in query:
            speak("thanks for using me sir, have a good day ")
            sys.exit()

        speak("sir do you have any other work")









