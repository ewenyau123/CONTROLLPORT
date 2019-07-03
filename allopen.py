#!/usr/bin/env python

import socket
from time import gmtime, strftime

TCP_IP = '172.16.8.225'
TCP_PORT = 10000
BUFFER_SIZE = 1024
MESSAGE = (b'\xFE\x0F\x00\x00\x00\x08\x01\xFF\xF1\xD1') #close


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

print ("received data:", data)
a=strftime("%Y-%m-%d %H:%M:%S", gmtime())
file = open("record.txt", "a")
file.write("All the port open at: ")
file.write(a)
file.write("\n")
file.close()