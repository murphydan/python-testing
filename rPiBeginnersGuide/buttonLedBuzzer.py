from gpiozero import Button
from gpiozero import LED
from gpiozero import Buzzer
from time import sleep

button = Button(2)
led = LED(25)
buzzer = Buzzer(15)

def myLoop(onTime, offTime):
    led.on()
    #buzzer.on()
    sleep(onTime)
    led.off()
    #buzzer.off()
    sleep(offTime)

while True:
    button.wait_for_press()
    #1
    myLoop(.1, .2)
    #2
    myLoop(.1, .1)
    #3
    myLoop(.1, .2)
    #4
    myLoop(.1, .2)
    #5
    myLoop(.4, .4)
    #6
    myLoop(.15, .25)
    #7
    myLoop(.15, .25)