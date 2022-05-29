import server
import move
import camera
import lidar
import parsing


camera_stream = True
lidar_stream = True

import time 

t = time.time()

def main():
    if (camera_stream):
        if len(server.send_queue) < 3:
            server.send_queue.append("img " + camera.get_base64())
    
    global t
    if (lidar_stream):
        if time.time() - t > 0.5:
            server.send_queue.append("lidar " +  lidar.get_data().string())
            t = time.time()

while True:
    main()