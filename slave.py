import time
import sys
import socket
import os

s = socket.socket();

host = "192.168.0.106"
port = 8080
s.connect((host, port))

print("")
print("connected to server...")

command = s.recv(1024)
command = command.decode()

if command == "shutdown":
    print("shutdown command")
    s.send("command received".encode())
    os.system("shutdown.bat")
