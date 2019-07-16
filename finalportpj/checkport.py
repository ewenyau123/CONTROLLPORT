import json
import socket
import struct
import crcmod

def comparison(x):
    if readstatus[x] == '0':
        status.append('0')
    else:
        status.append('1')

def add0():
    status.append('0')

with open('configfile.json') as json_file:  
    data = json.load(json_file)
devices=data["devices"]
device_port=devices["port"]
for item in device_port:
    status=[]
    realstatus=[]
    statusinverse = []
    i=x[item]
    TCP_IP=i["device_ip"]
    DATA = i["StatusMessage"]
    multicommand = i["multicommand"]
    TCP_PORT = 10000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(DATA)
    data = s.recv(4096)
    s.close()
    a = data.hex()
    binarytestresult = [a[i:i+2] for i in range(0, len(a), 2)]
    scale = 16
    num_of_bits = 8
    returnstatus=[bin(int(binarytestresult[3], scale))[2:].zfill(num_of_bits)[i:i+1] for i in range(0, len(bin(int(binarytestresult[3], scale))[2:].zfill(num_of_bits)), 1)]
    if DATA == bytes.fromhex('FE 01 00 00 00 10 29 C9'):
        [returnstatus.append(bin(int(binarytestresult[4], scale))[2:].zfill(num_of_bits)[i:i+1]) for i in range(0, len(bin(int(binarytestresult[4], scale))[2:].zfill(num_of_bits)), 1)]
        text_file = open("16portstatus.txt", "r")
        readstatus = text_file.read().split(",")
        text_file.close()
    else:
        text_file = open("8portstatus.txt", "r")
        readstatus = text_file.read().split(",")
        text_file.close()

    for x in range(len(returnstatus)):
        realstatus.append(returnstatus[len(returnstatus)-x-1])
    if readstatus != realstatus: 
        for x in range(len(readstatus)):
            if readstatus[x] != realstatus[x]:
                comparison(x)
            else:
                add0()
        for x in range(len(status)):
            statusinverse.append(status[len(status)-x-1])
        checkedstatus = '{:0{}X}'.format(int(''.join(statusinverse), 2), len(statusinverse)// 4)
        checkedstatusarray = [checkedstatus[i:i+2] for i in range(0, len(checkedstatus), 2)]
        multicommand[7]=checkedstatusarray[0]
        multicommand[8]=checkedstatusarray[1]
        crc16 = crcmod.mkCrcFun(0x18005, rev=True, initCrc=0xFFFF, xorOut=0x0000)
        crc = [hex(crc16(bytes.fromhex(''.join(multicommand))))[i:i+2] for i in range(0, len(hex(crc16(bytes.fromhex(''.join(multicommand))))), 2)]
        multicommand.append(crc[2])
        multicommand.append(crc[1])
        sendcommand = bytes.fromhex(''.join(multicommand))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        s.send(sendcommand)
        data = s.recv(4096)
        s.close()
        print(data)
