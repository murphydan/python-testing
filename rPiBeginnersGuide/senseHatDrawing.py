from sense_emu import SenseHat
from time import sleep
sense = SenseHat()

sense.clear()
sense.set_pixel(2, 2, (0, 0, 255))
sense.set_pixel(4, 2, (0, 0, 255))
sense.set_pixel(3, 4, (100, 0, 0))
sense.set_pixel(1, 5, (255, 0, 0))
sense.set_pixel(2, 6, (255, 0, 0))
sense.set_pixel(3, 6, (255, 0, 0))
sense.set_pixel(4, 6, (255, 0, 0))
sense.set_pixel(5, 5, (255, 0, 0))

sleep(3)
sense.clear()
sleep(1)

g = (0, 255, 0)
b = (0, 0, 0)

creeper_pixels = [
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, b, b, g,
    g, g, g, g, g, b, b, g,
    g, g, g, b, b, g, g, g,
    g, g, b, b, b, b, g, g,
    g, g, b, b, b, b, g, g,
    g, g, b, g, g, b, g, g
]

sense.set_pixels(creeper_pixels)

while True:
    sleep(1)
    #sense.flip_h()
    sense.set_rotation(90)
    sleep(1)
    #sense.flip_h()
    sense.set_rotation(180)
    sleep(1)
    #sense.flip_h()
    sense.set_rotation(270)
    sleep(1)
    #sense.flip_h()
    sense.set_rotation(0)