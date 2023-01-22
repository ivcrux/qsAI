
''' this is used to test the adapter creation process and
left to remain if there could be further use for it later'''

from chatterbot.logic import LogicAdapter

class QuantGemStone(LogicAdapter):
	''' this is the bot name adapter'''
	def __init__(self, chatbot, **kwargs):
		super().__init__(chatbot, **kwargs)

	def can_process(self, statement):
		words=['what', 'is', 'your', 'names']
		if all (x in statement.text.split() for x in words):
			return True
		else:
			return False

	def procss(self, input_statement, addaitional_response_selection_parameters):
		from chatterbot.conversation import Statement
		if input_statement == 'what is your name':
			confidence = 1
		else:
			confidence = 0

		response=Statement(text='i am Quant Gem Stone')
		return confidence, response
