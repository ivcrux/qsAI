# desktop version of quantStone bot version 1.0
# check the requirement.txt before running
'''this should have chatbot but left for the next version, so that everyone can
run this version with any python vrsion they have'''

import speech_recognition as sr

import webbrowser
import datetime
import wikipedia
import qcomms as cm
import qslogic as rwords

import qsbrain as b
import qcore as chb
def greet():
    b.greet_user()
    #cm.speak("Tell me how may I help you")

def queryProcess():
	query=['default']
	greet()
	while(True):
		try :
			query[0] = cm.takeCommand().lower()
		except Exception as e:
			#print(e)
			query[0]= cm.takeCommand()
			print(query)
			#break
		rwords.wordbank(query)

if __name__ == '__main__':
	#while (True):
	#queryProcess()
    chb.comm()
