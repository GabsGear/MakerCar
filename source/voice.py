import sys
import pyttsx3

class Voice():

	def sayHello(self, name):
		engine = pyttsx3.init()
		rate = engine.getProperty('rate')
		engine.setProperty('voice', b'brazil')	
		engine.setProperty('rate',rate-30)
		engine.setProperty('volume',1.0) 	
		string = ('Hello ' + str(name) + ', you ok?')
		engine.say(string)
		engine.runAndWait()

	def sayWellcome(self):
		engine = pyttsx3.init()
		rate = engine.getProperty('rate')
		engine.setProperty('voice', b'brazil')	
		engine.setProperty('rate',rate-30)
		engine.setProperty('volume',1.0) 	
		string = ('Hi stranger, I do not know you. Welcome to Maker Space, what is your name?')
		engine.say(string)
		engine.runAndWait()
