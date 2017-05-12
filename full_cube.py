import RPi.GPIO as GPIO
import time
low = GPIO.LOW
high = GPIO.HIGH
GPIO.setmode(GPIO.BCM)
layer = [27,18,17]
pos = [5,6,12,13,19,16,21,20,26]
for l in layer:
    GPIO.output(l,low)
for i in range(100)
    for led in pos:
        GPIO.output(led,high)
        time.sleep(0,0006)
        GPIO.output(led, low)

GPIO.cleanup()
