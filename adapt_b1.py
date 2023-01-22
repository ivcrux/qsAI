def greet_user():
    """Greets the user according to the time"""

    hour = datetime.datetime.now().hour
    if (hour >= 6) and (hour < 12):
        m.speak(f"Good Morning {USERNAME}")

    elif (hour >0)and (hour<5):
    	m.speak(f"its ealry morning hours")
    elif (hour >= 12) and (hour < 16):
        m.speak(f"Good afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        m.speak(f"Good Evening {USERNAME}")
    m.speak(f"I am {BOTNAME}. How may I assist you?")

from chatterbot.logic import logic_adapters

class TimeGreetBased(LogicAdapter):
	def __init__(self, chatbot, **kwargs):
		super().__init__(chatbot, **kwargs)

	def can_process(self, statement):
		return True


	def procss(self, input_statement, addaitional_response_selection_parameters):
		pass
