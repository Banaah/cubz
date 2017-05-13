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

for i in range(10):
    for lay in layer:
        GPIO.output(lay,low)
        for led_lay in pos:
            if led_lay == 19:
                pass
            else:
                for temp in range(10000):
                    GPIO.output(led_lay,high)
                    GPIO.output(led_lay,low)
        GPIO.output(lay,high)
GPIO.cleanup()
