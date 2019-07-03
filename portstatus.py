import socket
from time import gmtime, strftime

TCP_IP = '172.16.88.193'
TCP_PORT = 10000
BUFFER_SIZE = 1024
MESSAGE = (b'\xFE\x01\x00\x00\x00\x10\x29\xC9')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()
print ("received data:", data)
data = MESSAGE.read().split("\x")