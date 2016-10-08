import time
import os
import requests
import datetime
from dateutil.parser import *
from dateutil.tz import tzlocal

sonidos =['aplay /usr/share/sounds/alsa/Side_Right.wav']

level =0
while True:
	
	r = requests.get('http://172.17.214.24:3000/schedule')
	print(r.json())
	datavec=r.json()
	now = datetime.datetime.now(tzlocal())
	for each in datavec:
		alarma = parse(each["time"])
		
		if alarma < now:
			os.system(sonidos[level])
			print("menor")
		else:
			print("mayor igual")

		time.sleep(2)
