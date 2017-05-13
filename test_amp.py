import RPi.GPIO as GPIO
import time
led = [19,26,19,20,17]
GPIO.setmode(GPIO.BCM)
for i in led:
    GPIO.setup(i, GPIO.OUT)
#GPIO.output(26, GPIO.HIGH)
GPIO.output(17, GPIO.LOW)
for i in range(100000):
    GPIO.output(19, GPIO.HIGH)
    GPIO.output(19, GPIO.LOW)
GPIO.cleanup()
