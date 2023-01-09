# reserved word bank
import qsmouth as m
import qsbrain as b
import wikipedia
import webbrowser


greetings=['hello','good morning', 'hi'   ,  'good afternoon', 'whats up' , 'good evening']
# make a dict of greeting split into morning afternoon n night
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


def wordbank(q):
	if q[0] in greetings:
		#m.speak('its a greetings')
		m.speak(g_dict[q[0]])
		print('testing yes')

	elif q[0] in goodbye:
		m.speak('goodbye, till we meet again to ear you')
		exit()
	elif q[0].split(' ')[0] in webword:
		wikiFun(q[0].split(' ')[1:])
	elif q[0] in actword:
		m.speak('this is an advance section to be filled, thus nothing within my programme yet')
	else:
		m.speak('something is not clicking right')
		
def wikiFun(query, *arg):
	m.speak("Checking the wikipedia ")
	try:
		result = wikipedia.summary(query, sentences=4)
		m.speak("According to wikipedia")
		m.speak(result)
	except :
		m.speak(' i do not have access to the internet')
# for opening app or the web
def actRep(a):
	if a in act_res.offline:
		m.speak(' this is for offline')
	else:
		m.speak('going online')		
		
						
def wordBank(query, *args):
	if query[0] in greetings:
		m.speak(g_dict[query[0]])
		print(1)
		#continue
	
	elif "open geeksforgeeks" in str(query):
		m.speak("Opening GeeksforGeeks ")
		webbrowser.open("www.geeksforgeeks.com")
		print(2)
		#continue         
	elif "open google" in str(query):
		m.speak("Opening Google ")
		webbrowser.open("www.google.com")
		print(3)
		#continue             
	elif "which day" in str(query):
		b.tellDay()
		print(4)
		#continue
	elif "tell me the time" in str(query):
		b.tellTime()
		#continue
        # this will exit and terminate the program
	elif 'exit' or 'bye bye' in str(query):
		m.speak("Bye bye, till we meet again")
		exit()     
	elif "from wikipedia" in str(query):
		m.speak("Checking the wikipedia ")
		query = query.replace("wikipedia", "")
		result = wikipedia.summary(query, sentences=4)
		m.speak("According to wikipedia")
		m.speak(result)
	elif "tell me your name" in str(query):
		m.speak("I am lion Quant Stone. Your  Assistant in training")

	else:
		#add here to tramsfer to the advance section
		print(type(query))
		m.speak('nothing is matching in the programme')





 