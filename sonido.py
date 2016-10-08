import time
import os
import requests
import datetime
sonidos =['aplay /usr/share/sounds/alsa/Side_Right.wav']
d = datetime.datetime.now()

level =0
while True:
	
	r = requests.get('http://172.17.214.24:3000/schedule')
	print(r.json())
	datavec=r.json()
	now = datetime.datetime.now()
	for each in datavec:
		if each['time']<		
	#parseo json
	os.system(sonidos[level])
	time.sleep(2)
	if d < now:
		print("menor")
	else:
		print("mayor igual")
