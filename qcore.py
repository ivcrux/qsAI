from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import qcomms as cm

#lcc= logic comms center: group mouth and ear together under this
# {'import_path':'chatterbot.logic.TimeLogicAdapter'},
brain = ChatBot('quantstone',
logic_adapters=[
{'import_path':'chatterbot.logic.MathematicalEvaluation'},

{'import_path':'chatterbot.logic.BestMatch'},
{'import_path':'adapt_name.QuantGemStone'},

{'import_path':'chatterbot.logic.SpecificResponseAdapter',
'input_text':'what is your name',
'output_text': 'i am Quant Gem Stone'},
])
trainer = ListTrainer(brain)


trainer.train([
"hi",
"welcome, friend",
'that is good to hear.',
'Thank you',
'You are welcome.',
])
trainer.train([
"are you an AI",
"what do you think, human?"
])

def comm(*arg):
	exit_condition = (':q','quit', 'exit', 'bye','bye bye','goodbye','later' )
	while True:
		query = input ('> ')
		if query in exit_condition:
			cm.speak('goodbye, till we meet again to ear you')
			break
		else:
			res = brain.get_response(query)
			cm.speak(res)
			print(f"{ res}")
