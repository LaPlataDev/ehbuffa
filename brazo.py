import RPi.GPIO as GPIO

class Brazo:
	def __init__(self, pin=21):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(21, GPIO.OUT)

		self.servo = GPIO.PWM(21, 50)
		self.servo.start(7.5)

	def mover(self, angulo):
		# 0 <= angulo <= 180
		dc = angulo / 180.0 * 9 + 3 
		print dc
		self.servo.ChangeDutyCycle(dc)

	def liberar(self):
		self.servo.stop()
		GPIO.cleanup()

if __name__ == '__main__':
	import time
	b = Brazo()
	b.mover(0)
	time.sleep(0.5)
	b.mover(90)
	time.sleep(0.5)
	b.mover(180)
	time.sleep(0.5)
	b.liberar()
