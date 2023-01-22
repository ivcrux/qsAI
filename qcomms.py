import speech_recognition as sr
import pyttsx3
import os

engine = pyttsx3.init('sapi5')
voice =  engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)

def speak( words):
# this is the mouth function
	engine.say(words)
	engine.runAndWait()
    
    
def takeCommand():
# this is the ear function
    sp= sr.Recognizer()

    with sr.Microphone() as source:

        print('Listening')
        # seconds of non-speaking audio before
        # a phrase is considered complete
        sp.pause_threshold = 0.7
        audio = sp.listen(source)
        #audio =
        try:
            print("Recognizing")

            Query = sp.recognize_google(audio, language='en')
            print("the command is printed=", Query)
        except Exception as e:
            print(e)
            print("Say that again sir")
            speak('say that again sir')
            return "None"
        return Query
        


