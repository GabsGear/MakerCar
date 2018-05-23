import sys
from os import path
import pyttsx3
import pyaudio
import wave
import speech_recognition as sr

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


class Record():

	def startRecord(self):
		CHUNK = 1024
		FORMAT = pyaudio.paInt16
		CHANNELS = 2
		RATE = 44100
		RECORD_SECONDS = 5
		WAVE_OUTPUT_FILENAME = "/home/gabs/reconhecimento facial/audios/nome.wav"

		p = pyaudio.PyAudio()

		stream = p.open(format=FORMAT,
						channels=CHANNELS,
						rate=RATE,
						input=True,
						frames_per_buffer=CHUNK)

		print("* recording")

		frames = []

		for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
			data = stream.read(CHUNK)
			frames.append(data)

		print("* done recording")

		stream.stop_stream()
		stream.close()
		p.terminate()

		wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
		wf.setnchannels(CHANNELS)
		wf.setsampwidth(p.get_sample_size(FORMAT))
		wf.setframerate(RATE)
		wf.writeframes(b''.join(frames))
		wf.close()
