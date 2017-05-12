import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
led = [19,26,16,20]
for i in led:
    GPIO.setup(i, GPIO.OUT)
GPIO.output(20, GPIO.HIGH)
GPIO.output(16, GPIO.HIGH)

for j in range(100):
    GPIO.output(20, GPIO.LOW)
    time.sleep(0.05)
    GPIO.output(20, GPIO.HIGH)
    GPIO.output(16, GPIO.LOW)
    time.sleep(0.05)
    GPIO.output(16, GPIO.HIGH)
GPIO.cleanup()
