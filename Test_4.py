import RPi.GPIO as GPIO
import time
from motifs_4 import *
dimCube = 4
temps_affi = 0.01
low = GPIO.LOW
high = GPIO.HIGH
Ano = [21,20,26,16,19,13,6,12,5,7,8,25,9,24,23,22]
Cat = [2,3,4,14]

def main():
    setup_gpio()
    animation(mon_motif)
    GPIO.cleanup()

def setup_gpio():
    GPIO.setmode(GPIO.BCM)
    for i in Ano:
        GPIO.setup(i,GPIO.OUT)
        GPIO.output(i,low)
    for i in Cat:
        GPIO.setup(i,GPIO.OUT)
        GPIO.output(i,high)

def gp_state_swap(id, state):
    if state == 0:
        GPIO.output(id, low)
    else:
        GPIO.output(id, high)

def animation(motif):
    xTab = 0
    xled = 0
    for current_motif in motif:
        indAff_cou = current_motif[-1]
        tempsFin = time.clock() + (indAff_cou * temps_affi)
        while tempsFin > time.clock():
            xTab = 0
            for couche in range(dimCube):
                if couche == 0:
                    GPIO.output(Cat[dimCube-1], high)
                else:
                    GPIO.output(Cat[couche - 1], high)
                xled = 0
                for ligLed in range(dimCube):
                    for colLed in range(dimCube):
                        gp_state_swap(Ano[xled],(current_motif[xTab] & (1 << colLed)))
                        xled += 1
                    xTab += 1
                gp_state_swap(Cat[couche],low)
                time.sleep(0.005)
main()
