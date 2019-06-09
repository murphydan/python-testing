from picamera import PiCamera
from time import sleep
camera = PiCamera()

'''
camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()
'''

'''
camera.start_preview()
sleep(2)
camera.start_recording('/home/pi/Desktop/video.h264')
sleep(10)
camera.stop_recording()
camera.stop_preview()
'''

camera.start_preview()
sleep(5)
camera.image_effect = 'cartoon'
sleep(5)
camera.image_effect = 'colorswap'
sleep(5)
camera.image_effect = 'emboss'
sleep(5)
camera.image_effect = 'film'
sleep(5)
camera.image_effect = 'negative'
sleep(5)
camera.image_effect = 'oilpaint'
sleep(5)
camera.image_effect = 'pastel'
sleep(5)
camera.image_effect = 'posterise'
sleep(5)
camera.image_effect = 'sketch'
sleep(5)
camera.image_effect = 'solarize'
sleep(5)
camera.stop_preview()