import sensores
import RPi.GPIO as GPIO
import time
import os
import requests
import datetime
from dateutil.parser import *
from dateutil.tz import tzlocal
from brazo import Brazo

botonsuave = sensores.Button(22)

sonidos =['aplay /usr/share/sounds/alsa/Side_Right.wav','aplay /usr/share/sounds/alsa/Side_Right.wav']
espero=2
level =0
brazo = Brazo()
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
	
			print("apagaaaaaaaaaa")
	
			os.system(sonidos[level])
			if botonsuave.wait(3000) is None:
				brazo.mover(0)
				time.sleep(0.5)	
				brazo.mover(90)
				os.system(sonidos[level+1])
				brazo.mover(170)
			else:
				print("alarma apagada")
			time.sleep(espero)
			
			print("mayor igual")

	time.sleep(espero)
