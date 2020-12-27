import time
import sys
import socket
import os

s = socket.socket()
host = "192.168.0.106"
print(host)
port = 8080
s.bind((host, port))
print("")
print("Waiting for incoming connections...")
print("")
s.listen(1);
conn, addr = s.accept()
print("")
print(addr,"- Has connected to the server")
print("")


command = input(str("Command : "))
conn.send(command.encode())

print("Command has been sent successfully, waiting for confirmation...")
print("")


data = conn.recv(1024)

if data:
    print("Shutdown Command has been received and executed")
    print("")
