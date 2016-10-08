
import RPi.GPIO as GPIO
import time
import os
import requests
import datetime
from dateutil.parser import *
from dateutil.tz import tzlocal

sonidos =['aplay /usr/share/sounds/alsa/Side_Right.wav','aplay /usr/share/sounds/alsa/Side_Right.wav']
espero=2
level =0
while True:
	
	r = requests.get('http://172.17.214.24:3000/schedule')
	print(r.json())
	datavec=r.json()
	now = datetime.datetime.now(tzlocal())
	print(now )
	for each in datavec:
		alarma = parse(each["time"])
		t =  now - alarma
		if -30< t.total_seconds() < espero :
			#channel = GPIO.wait_for_edge(channel, GPIO_RISING, timeout=30)
			os.system(sonidos[level])
			time.sleep(espero)
			
			print("mayor igual")

	time.sleep(espero)
