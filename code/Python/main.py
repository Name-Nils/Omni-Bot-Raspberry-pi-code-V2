import server
import move
import camera
import lidar
import helper

alphabetical = "QWERTYUIOPÅASDFGHJKLÖÄZXCVBNMqwertyuiopåasdfghjklöäzxcvbnm  "

camera_stream = True
lidar_stream = True

import time 

t = time.time()

def main():
    if (camera_stream):
        if len(server.send_queue) < 3:
            server.send_queue.append("cam " + camera.get_base64())
        
    
    global t
    if (lidar_stream):
        if time.time() - t > 0.5:
            lidar_data = lidar.get_data()
            lidar_data.cartesian()
            lidar_data.noise_point_grouping()
            server.send_queue.append("lidar " +  lidar_data.string())
            t = time.time()

    if (len(server.receive_data) > 0):
        data = server.receive_data.pop() 
        if (helper.check("move", data)):
            a = helper.command("A", alphabetical, data)
            s = helper.command("S", alphabetical, data)
            r = helper.command("R", alphabetical, data)
            move.send("A" + str(a) + "S" + str(s) + "R" + str(r))
        elif (helper.check("cam", data)):
            a = helper.command("A", "", data)
            camera.tilt(float(a))



while True:
    main()