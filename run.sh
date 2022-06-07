#!/bin/bash
#sudo ls /dev > /mnt/usb/Data/ports.txt

while ! ifconfig | grep -F "192.168.8.117" > /dev/null; do
    sleep 1
done

#sudo python /mnt/usb/code/Python/server.py
sudo python /mnt/usb/code/Python/main.py 
#&> /mnt/usb/Data/python.txt