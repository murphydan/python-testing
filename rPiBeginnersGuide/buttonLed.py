from gpiozero import Button
from gpiozero import LED
from time import sleep

button = Button(2)
led = LED(25)

while True:
    button.wait_for_press()
    led.on()
    sleep(3)
    led.off()