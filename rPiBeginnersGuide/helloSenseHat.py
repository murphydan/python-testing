from sense_emu import SenseHat
from time import sleep
sense = SenseHat()

yellow = (255, 255, 0)
blue = (0, 0, 255)

while True:
    sense.show_message(
            "Hi, Dan!",
            text_colour=yellow,
            back_colour=blue,
            scroll_speed=(.05)
        )

    sense.show_letter("D", text_colour=yellow, back_colour=blue)
    sleep(1)
    sense.show_letter("A", text_colour=yellow, back_colour=blue)
    sleep(1)
    sense.show_letter("N", text_colour=yellow, back_colour=blue)
    sleep(1)
