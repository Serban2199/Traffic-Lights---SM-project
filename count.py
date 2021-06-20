import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

leds = [8, 10, 12]
pins = [3, 5, 7, 11, 13, 15, 19]
digits = [23, 21]

for led in leds:
	GPIO.setup(led, GPIO.OUT)

for pin in pins:
	GPIO.setup(pin, GPIO.OUT)

for digit in digits:
	GPIO.setup(digit, GPIO.OUT)

red_timeout = 16
yellow_timeout = 3
green_timeout = 21

x = True

digit = {
	"0": [1, 1, 1, 1, 1, 1, 0],
	"1": [0, 1, 1, 0, 0, 0, 0],
	"2": [1, 1, 0, 1, 1, 0, 1],
	"3": [1, 1, 1, 1, 0, 0, 1],
	"4": [0, 1, 1, 0, 0, 1, 1],
	"5": [1, 0, 1, 1, 0, 1, 1],
	"6": [1, 0, 1, 1, 1, 1, 1],
	"7": [1, 1, 1, 0, 0, 0, 0],
	"8": [1, 1, 1, 1, 1, 1, 1],
	"9": [1, 1, 1, 1, 0, 1, 1]
}

def set(x):
	GPIO.output(digits[0], x)
	GPIO.output(digits[1], x)

def display_digit(digit, pos):
	#for pin in pins:
	#	GPIO.output(pin, 1)
	#GPIO.output(digits[pos], 0)
	for d in digits:
		GPIO.output(d, 1)
	GPIO.output(digits[pos], 0)
	for pin, state in zip(pins, digit):
                GPIO.output(pin, state)
	#time.sleep(0.001)

TICKS = 240
def display(number, t):
	s = "{:02}".format(number)
	print(s)

	for i in range(TICKS):
		if i % 2:
			display_digit(digit[s[0]], 1)
		else:
			display_digit(digit[s[1]], 0)

		time.sleep(1.0 / TICKS)

def countdown(t, pin):
	GPIO.output(pin, 0)
	while t>0:
		display(t, 1)
		t -= 1
	GPIO.output(pin, 1)

try:
	GPIO.output(8, 1)
	GPIO.output(10, 1)
	GPIO.output(12, 1)
	while True:
		countdown(red_timeout, 8)
		countdown(green_timeout, 12)
		countdown(yellow_timeout, 10)
	#for i in range(99, 0, -1):
		#display(i)
		#time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()
