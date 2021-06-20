import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.OUT)
try:
	while(True):
		GPIO.output(10, 0)
		time.sleep(0.5)
		GPIO.output(10, 1)
		time.sleep(0.5)
except KeyboardInterrupt:
	GPIO.cleanup()
