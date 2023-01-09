import pyttsx3
import os

engine = pyttsx3.init('sapi5')
voice =  engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)

def speak( words):

	engine.say(words)
	engine.runAndWait()
