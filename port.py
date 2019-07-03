import sys
import socket
import time
from apscheduler.schedulers.background import BackgroundScheduler
from time import gmtime, strftime
from datetime import datetime
datetime.strftime  

i=0
stutuscounter=1
starttimecounter=2
endtimecounter=3
TCP_IP = '172.16.8.225'
TCP_IP2 = '172.16.8.140'
TCP_PORT = 10000
BUFFER_SIZE = 1024
boolean=True;
REFRESH_INTERVAL = 60 #seconds
 
scheduler = BackgroundScheduler()
scheduler.start()

def function(TCP,TCPPORT,BUFFER,MESSAGEx,PORTMESSAGEx):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP, TCPPORT))
    s.send(MESSAGEx)
    data = s.recv(BUFFER)
    s.close()
    record(data,PORTMESSAGEx)
    return;

def function2(TCP,TCP2,TCPPORT,BUFFER,MESSAGEx,PORTMESSAGEx):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP, TCPPORT))
    s.send(MESSAGEx)
    data = s.recv(BUFFER)
    s.close()
    record(data)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP2, TCPPORT))
    s.send(MESSAGEx)
    data = s.recv(BUFFER)
    s.close()
    record(data,PORTMESSAGEx)
    return;

def record(data,meassage):
    print ("received data:", data)
    a=datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    file = open("record.txt", "a")
    file.write(meassage)
    file.write(" at :   ")
    file.write(a)
    file.write("\n")
    file.close()
    return;

def electronic():
    global stutuscounter
    global starttimecounter
    global endtimecounter
    global i
    ctime = datetime.now().strftime('%H:%M')
    while i<len(sys.argv):
        status=sys.argv[stutuscounter]
        starttime=sys.argv[starttimecounter]
        endtime=sys.argv[endtimecounter]
        stutuscounter=stutuscounter+3
        starttimecounter=starttimecounter+3
        endtimecounter=endtimecounter+3
        i=i+3
        x=status
        if ctime>starttimecounter and ctime<endtimecounter:
            if x == 'on' :
                PORTMESSAGE = 'All PORT open'
                MESSAGE = (b'\xFE\x0F\x00\x00\x00\x08\x01\xFF\xF1\xD1')
                function2(TCP_IP,TCP_IP2,TCP_PORT,BUFFER_SIZE,MESSAGE)
                break;
            elif x == 'off' :
                PORTMESSAGE= 'ALL PORT close'
                MESSAGE = (b'\xFE\x0F\x00\x00\x00\x08\x01\x00\xB1\x91')
                function2(TCP_IP,TCP_IP2, TCP_PORT , BUFFER_SIZE,PORTMESSAGE,MESSAGE)
                break;
            elif x == '1on':
                PORTMESSAGE= 'PORT 1 open'
                MESSAGE = (b'\xFE\x05\x00\x00\xFF\x00\x98\x35')
                function(TCP_IP, TCP_PORT , BUFFER_SIZE,MESSAGE,PORTMESSAGE)
                break;
            elif x == '1off' :
                PORTMESSAGE= 'PORT 1 close'
                MESSAGE = (b'\xFE\x05\x00\x00\x00\x00\xD9\xC5')
                function(TCP_IP, TCP_PORT , BUFFER_SIZE,MESSAGE,PORTMESSAGE)
                break;
            elif x == '2on':
                PORTMESSAGE='PORT 2 open'
                MESSAGE = (b'\xFE\x05\x00\x01\xFF\x00\xC9\xF5')
                function(TCP_IP, TCP_PORT , BUFFER_SIZE,MESSAGE,PORTMESSAGE)
                break;
            elif x == '2off' :
                PORTMESSAGE='PORT 2 close'
                MESSAGE = (b'\xFE\x05\x00\x01\x00\x00\x88\x05')
                function(TCP_IP, TCP_PORT , BUFFER_SIZE,MESSAGE,PORTMESSAGE)
                break;
            elif x == '3on':
                PORTMESSAGE='PORT 3 open'
                MESSAGE = (b'\xFE\x05\x00\x02\xFF\x00\x39\xF5')
                function(TCP_IP, TCP_PORT , BUFFER_SIZE,MESSAGE,PORTMESSAGE)
                break;
            elif x == '3off' :
                PORTMESSAGE='PORT 3 close'
                MESSAGE = (b'\xFE\x05\x00\x02\x00\x00\x78\x05')
                function(TCP_IP, TCP_PORT , BUFFER_SIZE,MESSAGE,PORTMESSAGE)
                break;
            elif x == '4on':
                PORTMESSAGE='PORT 4 open'
                MESSAGE = (b'\xFE\x05\x00\x03\xFF\x00\x68\x35')
                function(TCP_IP, TCP_PORT , BUFFER_SIZE,MESSAGE,PORTMESSAGE)
                break;
            elif x == '4off' :
                PORTMESSAGE='PORT 4 close'
                MESSAGE = (b'\xFE\x05\x00\x03\x00\x00\x29\xC5')
                function(TCP_IP, TCP_PORT , BUFFER_SIZE,MESSAGE,PORTMESSAGE)
                break;
            elif x == '5on':
                PORTMESSAGE='PORT 5 open'
                MESSAGE = (b'\xFE\x05\x00\x04\xFF\x00\xD9\xF4')
                function(TCP_IP, TCP_PORT , BUFFER_SIZE,MESSAGE,PORTMESSAGE)
                break;
            elif x == '5off' :
                PORTMESSAGE='PORT 5 close'
                MESSAGE = (b'\xFE\x05\x00\x04\x00\x00\x98\x04')
                function(TCP_IP, TCP_PORT , BUFFER_SIZE,MESSAGE,PORTMESSAGE)
                break;
            elif x == '6on':
                PORTMESSAGE='PORT 6 open'
                MESSAGE = (b'\xFE\x05\x00\x05\xFF\x00\x88\x34')
                function(TCP_IP, TCP_PORT , BUFFER_SIZE,MESSAGE,PORTMESSAGE)
                break;
            elif x == '6off' :
                PORTMESSAGE='PORT 6 close'
                MESSAGE = (b'\xFE\x05\x00\x05\x00\x00\xC9\xC4')
                function(TCP_IP, TCP_PORT , BUFFER_SIZE,MESSAGE,PORTMESSAGE)
                break;
            elif x == '7on' :
                PORTMESSAGE='PORT 7 open'
                MESSAGE = (b'\xFE\x05\x00\x06\xFF\x00\x78\x34')
                function(TCP_IP, TCP_PORT , BUFFER_SIZE,MESSAGE,PORTMESSAGE)
                break;
            elif x == '7off' :
                PORTMESSAGE='PORT 7 close'
                MESSAGE = (b'\xFE\x05\x00\x06\x00\x00\x39\xC4')
                function(TCP_IP, TCP_PORT , BUFFER_SIZE,MESSAGE,PORTMESSAGE)
                break;
            elif x == '8on':
                PORTMESSAGE='PORT 8 open'
                MESSAGE = (b'\xFE\x05\x00\x07\xFF\x00\x29\xF4')
                function(TCP_IP, TCP_PORT , BUFFER_SIZE,MESSAGE,PORTMESSAGE)
                break;
            elif x == '8off' :
                PORTMESSAGE='PORT 8 close'
                MESSAGE = (b'\xFE\x05\x00\x07\x00\x00\x68\x04')
                function(TCP_IP, TCP_PORT , BUFFER_SIZE,MESSAGE,PORTMESSAGE)
                break;
            elif x == '9on':
                PORTMESSAGE='PORT 9 open'
                MESSAGE = (b'\xFE\x05\x00\x00\xFF\x00\x98\x35')
                function(TCP_IP2, TCP_PORT , BUFFER_SIZE,MESSAGE,PORTMESSAGE)
                break;
            elif x == '9off' :
                PORTMESSAGE='PORT 9 close'
                MESSAGE = (b'\xFE\x05\x00\x00\x00\x00\xD9\xC5')
                function(TCP_IP2, TCP_PORT , BUFFER_SIZE,MESSAGE,PORTMESSAGE)
                break;
            elif x == '10on' :
                PORTMESSAGE='PORT 10 open'
                MESSAGE = (b'\xFE\x05\x00\x01\xFF\x00\xC9\xF5')
                function(TCP_IP2, TCP_PORT , BUFFER_SIZE,MESSAGE,PORTMESSAGE)
                break;
            elif x == '10off' :
                PORTMESSAGE='PORT 10 close'
                MESSAGE = (b'\xFE\x05\x00\x01\x00\x00\x88\x05')
                function(TCP_IP2, TCP_PORT , BUFFER_SIZE,MESSAGE,PORTMESSAGE)
                break;
            elif x == '11on' :
                PORTMESSAGE='PORT 11 open'
                MESSAGE = (b'\xFE\x05\x00\x02\xFF\x00\x39\xF5')
                function(TCP_IP2, TCP_PORT , BUFFER_SIZE,MESSAGE,PORTMESSAGE)
                break;
            elif x == '11off' :
                PORTMESSAGE='PORT 11 close'
                MESSAGE = (b'\xFE\x05\x00\x02\x00\x00\x78\x05')
                function(TCP_IP2, TCP_PORT , BUFFER_SIZE,MESSAGE,PORTMESSAGE)
                break;
            elif x == '12on' :
                PORTMESSAGE='PORT 12 open'
                MESSAGE = (b'\xFE\x05\x00\x03\xFF\x00\x68\x35')
                function(TCP_IP2, TCP_PORT , BUFFER_SIZE,MESSAGE,PORTMESSAGE)
                break;
            elif x == '12off' :
                PORTMESSAGE='PORT 12 close'
                MESSAGE = (b'\xFE\x05\x00\x03\x00\x00\x29\xC5')
                function(TCP_IP2, TCP_PORT , BUFFER_SIZE,MESSAGE,PORTMESSAGE)
                break;
            elif x == '13on' :
                PORTMESSAGE='PORT 13 open'
                MESSAGE = (b'\xFE\x05\x00\x04\xFF\x00\xD9\xF4')
                function(TCP_IP2, TCP_PORT , BUFFER_SIZE,MESSAGE,PORTMESSAGE)
                break;
            elif x == '13off' :
                PORTMESSAGE='PORT 13 close'
                MESSAGE = (b'\xFE\x05\x00\x04\x00\x00\x98\x04')
                function(TCP_IP2, TCP_PORT , BUFFER_SIZE,MESSAGE,PORTMESSAGE)
                break;
            elif x == '14on' :
                PORTMESSAGE='PORT 14 open'
                MESSAGE = (b'\xFE\x05\x00\x05\xFF\x00\x88\x34')
                function(TCP_IP2, TCP_PORT , BUFFER_SIZE,MESSAGE,PORTMESSAGEE)
                break;
            elif x == '14off' :
                PORTMESSAGE='PORT 14 close'
                MESSAGE = (b'\xFE\x05\x00\x05\x00\x00\xC9\xC4')
                function(TCP_IP2, TCP_PORT , BUFFER_SIZE,MESSAGE,PORTMESSAGE)
                break;
            elif x == '15on' :
                PORTMESSAGE='PORT 15 open'
                MESSAGE = (b'\xFE\x05\x00\x06\xFF\x00\x78\x34')
                function(TCP_IP2, TCP_PORT , BUFFER_SIZE,MESSAGE,PORTMESSAGE)
                break;
            elif x == '15off' :
                PORTMESSAGE='PORT 15 close'
                MESSAGE = (b'\xFE\x05\x00\x06\x00\x00\x39\xC4')
                function(TCP_IP2, TCP_PORT , BUFFER_SIZE,MESSAGE,PORTMESSAGE)
                break;
            elif x == '16on' :
                PORTMESSAGE='PORT 16 open'
                MESSAGE = (b'\xFE\x05\x00\x07\xFF\x00\x29\xF4')
                function(TCP_IP2, TCP_PORT , BUFFER_SIZE,MESSAGE,PORTMESSAGE)
                break;
            elif x == '16off' :
                PORTMESSAGE='PORT 16 close'
                MESSAGE = (b'\xFE\x05\x00\x07\x00\x00\x68\x04')
                function(TCP_IP2, TCP_PORT , BUFFER_SIZE,MESSAGE,PORTMESSAGE)
                break;
            else :
                break;
        else:
            global boolean
            boolean = False

def main():
    electronic()
    scheduler.add_job(electronic, 'interval', seconds = REFRESH_INTERVAL)
    while boolean:
        time.sleep(5)

if __name__ == "__main__":
    main()
