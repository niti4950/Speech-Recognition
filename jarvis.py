import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
#print(voices[0])


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning!!")

    elif hour>12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("i am jarvis, how can i help you sir")

def takeCommand():
    # it takes microphone input
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        #r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:

        print("say that again please")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your_email@gmail.com','your-password')
    server.sendmail('your_email@gmail.com', to, content)
    server.close()




if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        # logic for executing task based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 2)
            speak('according to wikipedia..')
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open gmail' in query:
            webbrowser.open('gmail.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stckoverflow.com')

        elif 'open udemy' in query:
            webbrowser.open('udemy.com')

        elif 'play music' in query:
            music_dir = 'G:\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif 'open code' in query:
            codepath = 'C:\\Program Files\Microsoft VS Code\\Code.exe'
            os.startfile(codepath)

        elif 'who are you' in query:
            speak("JARVIS is  Nitin's home computing system, taking care of everything to do with the house, from heating and cooling systems to engine analysis of Nitin's hot rod in the garage")

        elif 'email to nitin' in query:
            try:
                speak('what should i say')
                content = takeCommand()
                to = 'destination_email@gmail.com'
                sendEmail(to, content)
                speak("Email has been sent")

            except Exception as e:
                print(e)
                speak('Sorry, sir unable to send email')

        elif 'exit' in query:
            speak("Thank you sir, have a nice day")
            exit()