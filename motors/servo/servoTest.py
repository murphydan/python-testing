#5v -> red
#GND -> black
#23 -> white
from gpiozero import Servo
from time import sleep

servo = Servo(23)

servo.value = 0.5

'''
while True:
    servo.min()
    sleep(3)
    servo.mid()
    sleep(3)
    servo.max()
    sleep(3)
'''