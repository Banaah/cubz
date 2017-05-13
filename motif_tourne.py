import RPi.GPIO as GPIO
import time
low = GPIO.LOW
high = GPIO.HIGH
GPIO.setmode(GPIO.BCM)
layer = [27,18,17]
pos = [12,6,5,13,21,20,26,16,19]
for l in layer:
    GPIO.setup(l, GPIO.OUT)
    GPIO.output(l,high)
for l in pos:
    GPIO.setup(l, GPIO.OUT)
    GPIO.output(l,low)

for i in range(100):
    GPIO.output(18,low)
    for led_lay in pos:
        if led_lay == 19:
            pass
        else:
            for temp in range(10000):
                GPIO.output(led_lay,high)
                GPIO.output(led_lay,low)
    GPIO.output(18,high)
GPIO.cleanup()
