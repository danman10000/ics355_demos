import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40,GPIO.OUT)
GPIO.output(40,GPIO.HIGH)
time.sleep(5)
GPIO.output(40,GPIO.LOW)
