import base64
from picamera import PiCamera
import RPi.GPIO as GPIO

cam = PiCamera()
#cam.rotation = 0
cam.resolution = (250, 150)
cam.framerate = 80

servo_pin = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

servo = GPIO.PWM(servo_pin, 50)
servo.start(7) # origin angle should be around 90 deg to the ground

angle = 90
def tilt(delta_angle):
    global angle
    
    if angle > 180:
        angle = 180
    elif angle < 0:
        angle = 0

    angle += delta_angle
    servo.ChangeDutyCycle((angle/180 * 10) + 2)

def get_base64():
    cam.capture("/mnt/usb/image.jpg", use_video_port=True)
    
    with open("/mnt/usb/image.jpg", "rb") as img:
        base_64 = str(base64.b64encode(img.read()))[2:-1]
    return base_64

