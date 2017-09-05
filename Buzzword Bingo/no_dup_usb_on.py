import RPi.GPIO as GPIO
import time
import pickle

def runlights():
 GPIO.setmode(GPIO.BOARD)
 GPIO.setup(40,GPIO.OUT)
 GPIO.output(40,GPIO.HIGH)
 time.sleep(5)
 GPIO.output(40,GPIO.LOW)

def writedict():
 myfile=open(state.txt@
