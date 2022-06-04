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
    def __init__(self, angle, dist, robot_x = 0, robot_y = 0, acc = 1):
        self.angle = angle
        self.dist = dist
        self.acc = acc

        self.robot_x = robot_x
        self.robot_y = robot_y
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

    def translate(self, x, y, r): # rotates first then adds the offset
        for point in self.points:
            new_x = (point.x * math.cos(r)) - (point.y * math.sin(r))
            new_y = (point.x * math.sin(r)) + (point.y * math.cos(r))
            
            point.x = new_x + x
            point.y = new_y + y

    def noise_point_grouping(self):
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

    def noise_point_movement(self, sets):
        # check the similarity with previous point and translate the points according to movement
        # an array of sets is passed and the length of that array is what dictates the amount of history checked
        for set in sets:
            # translate this point to x=0 y=0
            set.translate(-set.robot_x, -set.robot_y, 0) # negative because we want to remove the translation
        
        # now we need to compare the sets and give all points a value based on the distance or offset from the closest point
        # if the point doesnt have a close point then it will receive a low acc score even though this may be due to other lidar issues
        
        

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
