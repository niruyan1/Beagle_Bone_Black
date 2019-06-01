import Adafruit_BBIO.GPIO as GPIO
import datetime
import sys
from time import sleep

GPIO.cleanup()
	
def lightswitch(digit, num):	
	
	GPIO.output(digit1, GPIO.LOW)
	GPIO.output(digit2, GPIO.LOW)
	GPIO.output(digit3, GPIO.LOW)
	GPIO.output(digit4, GPIO.LOW)
	
	GPIO.output(sega, GPIO.HIGH)
	GPIO.output(segb, GPIO.HIGH)
	GPIO.output(segc, GPIO.HIGH)
	GPIO.output(segd, GPIO.HIGH)
	GPIO.output(sege, GPIO.HIGH)
	GPIO.output(segf, GPIO.HIGH)
	GPIO.output(segg, GPIO.HIGH)
	
	if num == 1:
		GPIO.output(segb, GPIO.LOW)
		GPIO.output(segc, GPIO.LOW)
	elif num == 2:
		GPIO.output(sega, GPIO.LOW)
		GPIO.output(segb, GPIO.LOW)
		GPIO.output(segd, GPIO.LOW)
		GPIO.output(sege, GPIO.LOW)
		GPIO.output(segg, GPIO.LOW)
	elif num == 3:
		GPIO.output(sega, GPIO.LOW)
		GPIO.output(segb, GPIO.LOW)
		GPIO.output(segc, GPIO.LOW)
		GPIO.output(segd, GPIO.LOW)
		GPIO.output(segg, GPIO.LOW)
	elif num == 4:
		GPIO.output(segb, GPIO.LOW)
		GPIO.output(segc, GPIO.LOW)
		GPIO.output(segf, GPIO.LOW)
		GPIO.output(segg, GPIO.LOW)
	elif num == 5:
		GPIO.output(sega, GPIO.LOW)
		GPIO.output(segc, GPIO.LOW)
		GPIO.output(segd, GPIO.LOW)
		GPIO.output(segf, GPIO.LOW)
		GPIO.output(segg, GPIO.LOW)
	elif num == 6:
		GPIO.output(sega, GPIO.LOW)
		GPIO.output(segc, GPIO.LOW)
		GPIO.output(segd, GPIO.LOW)
		GPIO.output(sege, GPIO.LOW)
		GPIO.output(segf, GPIO.LOW)
		GPIO.output(segg, GPIO.LOW)
	elif num == 7:
		GPIO.output(sega, GPIO.LOW)
		GPIO.output(segb, GPIO.LOW)
		GPIO.output(segc, GPIO.LOW)
	elif num == 8:
		GPIO.output(sega, GPIO.LOW)
		GPIO.output(segb, GPIO.LOW)
		GPIO.output(segc, GPIO.LOW)
		GPIO.output(segd, GPIO.LOW)
		GPIO.output(sege, GPIO.LOW)
		GPIO.output(segf, GPIO.LOW)
		GPIO.output(segg, GPIO.LOW)
	elif num == 9:
		GPIO.output(sega, GPIO.LOW)
		GPIO.output(segb, GPIO.LOW)
		GPIO.output(segc, GPIO.LOW)
		GPIO.output(segf, GPIO.LOW)
		GPIO.output(segg, GPIO.LOW)
	elif num == 0:
		GPIO.output(sega, GPIO.LOW)
		GPIO.output(segb, GPIO.LOW)
		GPIO.output(segc, GPIO.LOW)
		GPIO.output(segd, GPIO.LOW)
		GPIO.output(sege, GPIO.LOW)
		GPIO.output(segf, GPIO.LOW)
	else:
		GPIO.output(sega, GPIO.HIGH)
		GPIO.output(segb, GPIO.HIGH)
		GPIO.output(segc, GPIO.HIGH)
		GPIO.output(segd, GPIO.HIGH)
		GPIO.output(sege, GPIO.HIGH)
		GPIO.output(segf, GPIO.HIGH)
		GPIO.output(segg, GPIO.HIGH)		

	if digit == 1:
		GPIO.output(digit1, GPIO.HIGH)
	elif digit == 2:
		GPIO.output(digit2, GPIO.HIGH)
	elif digit == 3:
		GPIO.output(digit3, GPIO.HIGH)
	elif digit == 4:
		GPIO.output(digit4, GPIO.HIGH)
	else:
		GPIO.output(digit1, GPIO.LOW)
		GPIO.output(digit2, GPIO.LOW)
		GPIO.output(digit3, GPIO.LOW)
		GPIO.output(digit4, GPIO.LOW)



digit1="P9_12"
GPIO.setup(digit1,GPIO.OUT)
digit2="P9_23"
GPIO.setup(digit2, GPIO.OUT)
digit3="P9_30"
GPIO.setup(digit3, GPIO.OUT)
digit4="P9_27"
GPIO.setup(digit4, GPIO.OUT)

sega="P8_8"
GPIO.setup(sega,GPIO.OUT)
segb="P8_10"
GPIO.setup(segb,GPIO.OUT)
segc="P8_12"
GPIO.setup(segc,GPIO.OUT)
segd="P8_14"
GPIO.setup(segd,GPIO.OUT)
sege="P8_16"
GPIO.setup(sege,GPIO.OUT)
segf="P8_18"
GPIO.setup(segf,GPIO.OUT)
segg="P8_7"
GPIO.setup(segg,GPIO.OUT)

while 1:
	current_time=datetime.datetime.now()
	lightswitch(1,current_time.hour/10)
	sleep(0.001)
	lightswitch(2,current_time.hour%10)
	sleep(0.001)
	lightswitch(3,current_time.minute/10)
	sleep(0.001)
	lightswitch(4,current_time.minute%10)
	sleep(0.001)

GPIO.cleanup()
