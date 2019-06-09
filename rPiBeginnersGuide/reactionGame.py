from gpiozero import LED, Button
from time import sleep
from random import uniform
from os import _exit

left_name = input("Left player name is ")
right_name = input("Right player name is ")

sleep(1)

led = LED(4)
right_button = Button(15)
left_button = Button(14)

led.on()

print ("Great! Let's play!")
sleep(1)
print ("The LED is currently lit up")
sleep(3)
print ("Push your button as soon as the LED turns off")
sleep(4)
print("Ready...Go!")

sleep(uniform(5,10))
led.off()

def pressed(button):
    if button.pin.number == 14:
        print (left_name + " won the game")
    else:
        print (right_name + " won the game")
    _exit(0)

right_button.when_pressed = pressed
left_button.when_pressed = pressed