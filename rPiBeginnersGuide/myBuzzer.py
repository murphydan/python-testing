from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(15)


buzzer.on()
sleep(1)
buzzer.off()