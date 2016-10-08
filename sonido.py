import tts
import sensores
import RPi.GPIO as GPIO
import time
import os
import subprocess
import requests
import datetime
from dateutil.parser import *
from dateutil.tz import tzlocal
from brazo import Brazo
import random
botonsuave = sensores.Button(22)

sonidos_zen =[['mplayer', 'dos.wav'],['mplayer', 'uno.wav']]
sonidos_enojados =[['mplayer', 'puteada_for_men.wav'],['mplayer', 'puteada_for_her.mp3']]
espero=2
level =0
brazo = Brazo()
brazo.mover(90)
while True:
	
	r = requests.get('http://172.17.214.24:3000/schedule')
	print(r.json())
	datavec=r.json()
	#now = datetime.datetime.now(tzlocal())
	now =datetime.datetime(year=2016, month=10, day=8, hour=17,minute=54,tzinfo=tzlocal())
	print(now )
	for each in datavec:
		alarma = parse(each["time"])
		t =  now - alarma
		if -30< t.total_seconds() < espero :
			sp = subprocess.Popen(random.choice(sonidos_zen))
			sp.wait()
			print("apagaaaaaaaaaa")
			if botonsuave.wait(3000) is None:
				tts.speak(each)
				sp = subprocess.Popen(random.choice(sonidos_enojados))
				for cada in range(24):
					brazo.mover(0)
					time.sleep(0.5)	
					brazo.mover(170)
					time.sleep(0.5)	
				sp.wait()
				
			else:
				print("alarma apagada")
				
			time.sleep(espero)
			
			print("mayor igual")

	time.sleep(espero)
