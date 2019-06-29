#!/usr/bin/env python3
from time import sleep
import RPi.GPIO as GPIO
from RPLCD import CharLCD

lcd = CharLCD(cols=16, rows=2,
                pin_rw=None,
                pin_rs=37,
                pin_e=35,
                charmap="A00",
                pins_data=[33,31,29,23],
                numbering_mode=GPIO.BOARD)

try:
    lcd.write_string('Hello Dana')
    lcd.cursor_pos = (1, 0)
    sleep(3)
    #lcd.write_string('Hi')
    for x in range(0, 9):
        #print("We're on time %d" % (x))
        lcd.cursor_pos = (1, 0)
        lcd.write_string("Self Destruct " + str(9 - x))
        sleep(1)

except KeyboardInterrupt:
    print("Keyboard Interrupt")

except:
    print("some error")

finally:
    lcd.clear()
    GPIO.cleanup()