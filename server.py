#!/usr/bin/python3
import socket

s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 7777))
s.listen(1)

while True:
    sc, a = s.accept()
    print("new client:", a)
    while True:
        msg = sc.recv(1500)
        print("[server] received:" + msg.decode())
        if len(msg) == 0:
            print("[server] client disconnected")
            sc.close()
            break
        sc.sendall(msg)

s.close()
