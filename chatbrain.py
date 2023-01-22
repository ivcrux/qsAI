from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import qcomms as cm

brain = ChatBot('quantstone')

trainer = ListTrainer(brain)
trainer.train([
"hi",
"welcome, friend"
])
trainer.train([
"are you an AI",
"what do you think, human?"
])
def comm(*arg):

	exit_condition = (':q','quit', 'exit' )
	while True:
		query = input ('> ')
		if query in exit_condition:
			break
		else:
			#print(f"{ brain.get_response(query)}")
			cm.speak(brain.get_response(query))
