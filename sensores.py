import RPi.GPIO as GPIO


class Button:
	def __init__(self, channel):
		self.channel = channel
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

	def wait(self, timeout):
		return GPIO.wait_for_edge(self.channel, GPIO.RISING, timeout=timeout)


if __name__ == '__main__':
	import time
	b1 = Button(22)

	c = b1.wait(2000)
	print('b1 - ' + str(c))
