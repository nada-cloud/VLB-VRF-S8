#!/usr/bin/python3
import socket
from time import sleep

hote = "localhost"
port = 7777
data = "hey !"


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print("Connection on {}".format(port))

while True:
    socket.send(data.encode())
    sleep(60)

print("Close")
socket.close()
