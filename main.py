# desktop version of quantStone bot
# check the requirement.txt before running

import speech_recognition as sr

import webbrowser
import datetime
import wikipedia
import qsmouth as cm
import qslogic as rwords
import qsear as ee
import qsbrain as b


def greet():
    b.greet_user()
    #cm.speak("Tell me how may I help you")

def queryProcess():
	query=['default']
	greet()
	while(True):
		try :
			query[0] = ee.takeCommand().lower()
		except Exception as e:
			#print(e)
			query[0]= ee.takeCommand()
			print(query)
			#break
		rwords.wordbank(query)

if __name__ == '__main__':
	#while (True):
	queryProcess()
