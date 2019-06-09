#!/usr/bin/python
#--------------------------------------
#    ___  ___  _ ____
#   / _ \/ _ \(_) __/__  __ __
#  / , _/ ___/ /\ \/ _ \/ // /
# /_/|_/_/  /_/___/ .__/\_, /
#                /_/   /___/
#
#           servo2.py
# Basic example script to control a servo
# connected to GPIO17 using the Gpiozero library.
# Allows tweaking of pulse widths to get the full
# range of movement.
#
# Use CTRL-C to break out of While loop.
#
# Author : Matt Hawkins
# Date   : 20/01/2018
#
# https://www.raspberrypi-spy.co.uk/tag/servo/
#
#--------------------------------------
from gpiozero import Servo
from time import sleep

myGPIO=23

# Min and Max pulse widths converted into milliseconds
# To increase range of movement:
#   increase maxPW from default of 2.0
#   decrease minPW from default of 1.0
# Change myCorrection using increments of 0.05 and
# check the value works with your servo.
myCorrection=0.45
maxPW=(2.0+myCorrection)/1000
minPW=(1.0-myCorrection)/1000

myServo = Servo(myGPIO,min_pulse_width=minPW,max_pulse_width=maxPW)

print("Using GPIO17")
print("Max pulse width is set to 2.45 ms")
print("Min pulse width is set to 0.55 ms")

while True:
  myServo.mid()
  print("Set to middle position")
  sleep(1)
  myServo.min()
  print("Set to minimum position")
  sleep(1)
  myServo.mid()
  print("Set to middle position")
  sleep(1)
  myServo.max()
  print("Set to maximum position")
  sleep(1)