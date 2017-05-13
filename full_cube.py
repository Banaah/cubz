import RPi.GPIO as GPIO
import time
low = GPIO.LOW
high = GPIO.HIGH
GPIO.setmode(GPIO.BCM)
layer = [27,18,17]
pos = [5,6,12,13,19,16,21,20,26]
for l in layer:
    GPIO.setup(l, GPIO.OUT)
    GPIO.output(l,high)
for l in pos:
    GPIO.setup(l, GPIO.OUT)
    GPIO.output(l,low)
for t in range(100):
        for lay in layer:
            GPIO.output(lay,low)
            for led in pos:
                GPIO.output(led,high)
                time.sleep(0.0006)
                GPIO.output(led, low)
            GPIO.output(lay,high)
            time.sleep(1)

GPIO.cleanup()
