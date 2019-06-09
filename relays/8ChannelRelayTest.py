#!/usr/bin/python

# A simple Python application for controlling a relay board from a Raspberry Pi
# The application uses the GPIO Zero library (https://gpiozero.readthedocs.io/en/stable/)
# The relay is connected to one of the Pi's GPIO ports, then is defined as an Output device
# in GPIO Zero: https://gpiozero.readthedocs.io/en/stable/api_output.html#outputdevice

import sys
import time

import gpiozero

# change this value based on which GPIO port the relay is connected to
pinList = [2,3,4,17,27,22,10,9]

for _ in range(3):
    for idx, val in enumerate(pinList):

        # create a relay object.
        # Triggered by the output pin going low: active_high=False.
        # Initially off: initial_value=False
        relay = gpiozero.OutputDevice(val, active_high=False, initial_value=False)

        def set_relay(status):
            if status:
                print("Setting relay: ON")
                relay.on()
            else:
                print("Setting relay: OFF")
                relay.off()

        set_relay(False)
        set_relay(True)
        time.sleep(.1)
        set_relay(False)
