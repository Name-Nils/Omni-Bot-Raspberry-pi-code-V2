import math
import serial
import time
import helper

class DOF:
    def __init__(self, pos) -> None:
        self.pos = pos
        self.live_pos = pos # will be updated alongside update method but not as accurate
        self.start_time = time.time()
        self.speed = 0

    def speed_change(self, new_speed):
        if (self.speed == new_speed): return # if the speed is the same then nothing should change
        time_diff = time.time() - self.start_time
        dist = time_diff * self.speed
        self.pos += dist
        self.start_time = time.time()
        self.speed = new_speed
    
    def update(self):
        time_diff = time.time() - self.start_time
        dist = time_diff * self.speed
        self.live_pos = self.pos + dist
        return self.live_pos


class Pos:
    def __init__(self, x, y, r) -> None:
        self.x = x
        self.y = y
        self.r = r

    def speed(self, x, y, r):
        self.x.speed_change(x)
        self.y.speed_change(y)
        self.r.speed_change(r)
    def speed_polar(self, a, s, r):
        x = math.cos(a) * s
        y = math.sin(a) * s
        self.speed(x,y,r)
    
    def update(self):
        distances = []
        distances.append(self.x.update())
        distances.append(self.y.update())
        distances.append(self.r.update())
        return distances
        

pos = Pos(DOF(0), DOF(0), DOF(0))


ser = serial.Serial(
    port='/dev/ttyACM0', # arduino every port on the raspberry pi
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)


def send(data):
    ser.write((str(data) + "\n").encode("utf-8"))

"""
last_string = ""
def move_str(string_):
    global last_string
    if (last_string != string_):
        print (string_ + "\n")
        ser.write((string_ + "\n").encode("utf-8"))
    last_string = string_
"""

last_send = ""
def move(a, s, r):
    global last_send
    send = "A" + str(a)
    send += "S" + str(s)
    send += "R" + str(r)
    if (last_send == send): return
    ser.write((send + "\n").encode("utf-8"))
    pos.speed_polar(a, s, r)
    last_send = send