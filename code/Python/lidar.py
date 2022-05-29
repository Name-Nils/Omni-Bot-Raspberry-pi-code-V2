import PyLidar3
import time
import math


port = "/dev/ttyUSB0"
Obj = PyLidar3.YdLidarX4(port)
Obj.Connect()
gen = Obj.StartScanning()

def get_data():
    return Set(next(gen))


class Point:
    def __init__(self, angle, dist):
        self.angle = angle
        self.dist = dist

        self.x = None
        self.y = None
        self.acc = None

class Set:
    def __init__(self, data):
        self.points = []
        
        for i in range(len(data)):
            self.points.append(Point(i, float(data[i])))
    
    def cartesian(self):
        for point in self.points:
            point.x = math.cos(point.angle) * point.dist
            point.y = math.sin(point.angle) * point.dist

    def string(self):
        string = ""
        for point in self.points:
            string += str(point.dist)
            string += ", "
        return string
