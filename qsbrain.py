import qcomms as cm

import qslogic as rwords

import datetime
#import pywhatkit as kit
#from decouple import config

#USERNAME = config('JOHN')
#BOTNAME = config('QUANT STONE')
USERNAME = 'JOHN'
BOTNAME = 'QUANT STONE'
    
def tellDay():
    day = datetime.datetime.today().weekday() + 1
    #this line tells us about the number 
    Day_dict = {1: 'Monday', 2: 'Tuesday', 

                3: 'Wednesday', 4: 'Thursday', 

                5: 'Friday', 6: 'Saturday',

                7: 'Sunday'}     

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        cm.speak("The day is " + day_of_the_week)
 
def tellTime():     
    # This method will give the time
    time = str(datetime.datetime.now())
  #nd then after slicing we can get time
    print(time)
    hour = time[11:13]
    min = time[14:16]
    cm.speak( "The time is " + hour + " " + min + "Minutes")    

def search_google(query) :
 	pass
 	#kit.search(query)
 	
def play_on_youtube(video):
    pass
    #kit.playonyt(video)
def chatter():
	# to communicate continu
	pass    
def greet_user():
    """Greets the user according to the time"""
    
    hour = datetime.datetime.now().hour
    if (hour >= 6) and (hour < 12):
        cm.speak(f"Good Morning {USERNAME}")
        
    elif (hour >0)and (hour<5):
    	cm.speak(f"its ealry morning hours")
    elif (hour >= 12) and (hour < 16):
        cm.speak(f"Good afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        cm.speak(f"Good Evening {USERNAME}")
    cm.speak(f"I am {BOTNAME}. How may I assist you?")


