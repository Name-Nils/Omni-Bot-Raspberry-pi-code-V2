import base64
from tkinter import E
from picamera import PiCamera
import RPi.GPIO as GPIO

cam = PiCamera()
#cam.rotation = 0
cam.resolution = (250, 150)
cam.framerate = 80

servoPIN = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

servo = GPIO.PWM(servoPIN, 50)
servo.start(7) # origin angle should be around 90 deg to the ground

def tilt(angle):
    servo.ChangeDutyCycle((angle/180 * 10) + 2)

def get_base64():
    cam.capture("/mnt/usb/image.jpg", use_video_port=True)
    
    with open("/mnt/usb/image.jpg", "rb") as img:
        base_64 = str(base64.b64encode(img.read()))[2:-1]
    return base_64

