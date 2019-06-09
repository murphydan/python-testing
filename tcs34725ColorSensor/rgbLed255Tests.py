from gpiozero import RGBLED
from time import sleep

led = RGBLED(red=9, green=10, blue=11)

def rgbConversion( red ):
    return red / 255

redInt = rgbConversion( 5 )
greenInt = rgbConversion( 215 )
blueInt = rgbConversion( 100 )
print( redInt, greenInt, blueInt )
led.color = ( redInt, greenInt, blueInt )

sleep(1)
led.color = (0, 0, 0)

'''
led.red = 1  # full red
sleep(1)

led.color = (., .84, 1 )
sleep(1)

led.color = (0, 0, 0)  # off
'''