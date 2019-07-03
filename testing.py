import sys
import threading
from time import gmtime, strftime
from datetime import datetime
datetime.strftime  

i=0
counter = 1
def printit():
    threading.Timer(5.0, printit).start()
    ctime = datetime.now().strftime('%H:%M')
    global i
    global counter
    i+=1
    while i==4:
        break;
    arr = sys.argv[counter]
    print(ctime>arr)
    


printit()

