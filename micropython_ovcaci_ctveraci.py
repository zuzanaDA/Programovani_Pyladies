from machine import Pin, PWM
from time import sleep
pin = Pin(15, Pin.OUT)

while True:
	for i in range(2):
		pwm = PWM(pin, freq=32, duty=50)
		sleep(1.5)
		pwm = PWM(pin, freq=40, duty=50)
		sleep(1.5)
		pwm = PWM(pin, freq=50, duty=50)
		sleep(1.5)
	for a in range(2):
		pwm = PWM(pin, freq=41, duty=50)
		sleep(0.75)
		pin.value(0)
		sleep(1)
		pin.value(1)
		pwm = PWM(pin, freq=41, duty=50)
		sleep(0.75)
		pwm = PWM(pin, freq=36, duty=50)
		sleep(0.75)		
		pwm = PWM(pin, freq=41, duty=50)
		sleep(0.75)
		pwm = PWM(pin, freq=43, duty=50)
		sleep(1.5)		
		pwm = PWM(pin, freq=36, duty=50)
		sleep(1.5)
	pwm = PWM(pin, freq=41, duty=50)
	sleep(1.5)
	pwm = PWM(pin, freq=36, duty=50)
	sleep(1.5)		
	pwm = PWM(pin, freq=32, duty=50)
	sleep(1.5)