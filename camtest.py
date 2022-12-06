#!/usr/bin/env python
import time
import sys

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image

import cv2
import numpy as np


def cv2_to_pil(img): #Since you want to be able to use Pillow (PIL)
    return Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

def pil_to_cv2(img):
    return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

cam = cv2.VideoCapture(0) #Define the camera, 0 is which camera, if you have more than 1
ret_val, img = cam.read() #cam.read() returns ret (0/1 if the camera is working) and img, 
#the actual image of the camera in a numpy array

cv2.imshow("Webcam", gray) #if you wanted to open a window to see this picture
cv2.waitKey(0) #waits for the enter key to continue, change to
#0 to X milliseconds to stop for a certain amount of time.

pil_img = cv2_to_pil(img) #convert the image to PIL so you can use it that way.

# Configuration for the matrix
options = RGBMatrixOptions()
options.cols = 64
options.rows = 32
options.chain_length = 1
options.parallel = 1
options.brightness = 80
options.pwm_bits = 11
options.gpio_slowdown = 4.0
options.show_refresh_rate = 1
options.hardware_mapping = 'regular'  # If you have an Adafruit HAT: 'adafruit-hat'

matrix = RGBMatrix(options = options)

# Make image fit our screen.
#img.thumbnail((matrix.width, matrix.height), img.ANTIALIAS)

matrix.SetImage(img.convert('RGB'))

try:
    print("Press CTRL-C to stop.")
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    sys.exit(0)
