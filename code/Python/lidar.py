import PyLidar3
import time
import math
import helper


port = "/dev/ttyUSB0"
Obj = PyLidar3.YdLidarX4(port)
Obj.Connect()
gen = Obj.StartScanning()

def get_data():
    return Set(next(gen))


class Point:
    def __init__(self, angle, dist, acc = 1):
        self.angle = angle
        self.dist = dist
        self.acc = acc

        self.x = None
        self.y = None

class Set:
    def __init__(self, data):
        self.points = []
        
        for i in range(len(data)):
            self.points.append(Point((math.pi * (i + 90)) / 180, float(data[i])))
    
    def cartesian(self):
        for point in self.points:
            point.x = math.cos(point.angle) * point.dist
            point.y = math.sin(point.angle) * point.dist

    def calc_acc(self):
        min_dist = 120
        max_close = 5
        # calculate the quality of points based on their distance from other points
        for point in self.points:
            amount_within = 0
            for check in self.points:
                if amount_within >= max_close: break
                if helper.dist(point, check) < min_dist:
                    amount_within += 1
            percent = max_close / amount_within
            point.acc = point.acc * percent

        # check the similarity with previous point and translate the points according to movement
                    

    def string(self):
        string = ""
        for point in self.points:
            string += "X"
            string += str(point.x)
            string += " Y"
            string += str(point.y)
            string += " P"
            string += str(point.acc)
            string += ", "
        return string
