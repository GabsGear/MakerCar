import sys
import pyttsx3

def say(s):
	engine = pyttsx3.init()
	rate = engine.getProperty('rate')
	engine.setProperty('voice', b'brazil')	
	engine.setProperty('rate',rate-30)
	engine.setProperty('volume',1.0) 	
	engine.say(s)	
	a=engine.runAndWait()

say('Olá luan, tudo bem com você?')