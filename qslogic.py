#this is to replace rwords package
import qsbrain as b
import qcore as m
import wikipedia
import webbrowser
#import qslog
import random as rd

greetings= ['hello','good morning', 'hi'   ,  'good afternoon', 'whats up' , 'good evening']

g_dict={
'hello': 'hello my name is Quant, what is your name',
'good morning': 'this morning will be good, good morning to you too',
'hi':' hello, what shall we do together, we can have fun',
'good afternoon': 'afternoon to you',
'good evening': ' nighty nighty'
}

goodbye=[ 'bye','bye bye',  'exit' ,'goodbye','later']


actword=['open']

webword= ['search', 'about']
act_res = {
'offline':['hello'] ,
'online': ['yes']
}
a_dict={

}
response=['opening it']
otherO=['can we chat', 'lets chat','can you talk', 'let\'s chat']

# for word cross check
def wordbank(q):
	if q[0] in otherO:
		#m.speak('its a greetings')
		m.speak('this will be nice, it will create a learning moment for me')
		#cbt
	elif q[0] in greetings:
		#m.speak('its a greetings')
		m.speak(g_dict[q[0]])

	elif q[0] in goodbye:
		m.speak('goodbye, till we meet again to ear you')
		exit()

	elif "which day" in q[0]:
		b.tellDay()
		#continue

	elif "tell me the time" in q[0]:
		b.tellTime()
		#continue


	elif "tell me your name" in q[0]:
		m.speak("I am Quant Stone Zeta. Your  Assistant in training")

	elif q[0].split(' ')[0] in webword:
		wikiFun(q[0].split(' ')[1:])

	elif q[0] in actword:
		m.speak('this is an advance section to be filled, thus nothing within my programme yet')

	else:
		m.speak('jeez, something is not clicking right')
		#transfer to the complex logics
		qslog.complex()

# to access wikipedia
def wikiFun(query, *arg):
	m.speak("Checking the wikipedia ")
	try:
		result = wikipedia.summary(query, sentences=4)
		m.speak("According to wikipedia")
		m.speak(result)
	except :
		m.speak('shit, i do not have access to the internet')

# for opening app or the web
def actRep(a):
	if a in act_res.offline:
		m.speak(' this is for offline')
	else:
		m.speak('going online')
