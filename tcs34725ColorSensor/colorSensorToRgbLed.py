# Will change the RGB LED to the color recognized by the Color Sensor
from time import sleep
from gpiozero import RGBLED

import board
import busio

import adafruit_tcs34725

led = RGBLED(red=9, green=10, blue=11)

def rgbInt( sensorColors ):
    print ( sensorColors )
    red = sensorColors[0] / 255
    green = sensorColors[1] / 255
    blue = sensorColors[2] / 255
    return ( red, green, blue )


# Initialize I2C bus and sensor.
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tcs34725.TCS34725(i2c)

sensor.integration_time = 200
sensor.gain = 16

# Main loop reading color and printing it every second.
while True:
    rgbNew = rgbInt( sensor.color_rgb_bytes )
    led.color = ( rgbNew )
    print (rgbNew)
    sleep(.5)