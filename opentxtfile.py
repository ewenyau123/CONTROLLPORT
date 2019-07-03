import sys
text_file = open("123.txt", "r")
lines = text_file.read().split(",")
text_file.close()

def changeststus():
    file = open("123.txt","w")
    i=1
    for line in lines:
        file.write(" ".join(line))
        if i < len(lines):
            file.write(",")
            i += 1

for x in range(len(sys.argv)):
    if sys.argv[x-1]== '1on':
        lines[0] ='1'
        changeststus()
    if sys.argv[x-1]== '1off':
        lines[0] ='0'
        changeststus()
    if sys.argv[x-1]== '2on':
        lines[1] ='1'
        changeststus()
    if sys.argv[x-1]== '2off':
        lines[1] ='0'
        changeststus()
    if sys.argv[x-1]== '3on':
        lines[2] ='1'
        changeststus()
    if sys.argv[x-1]== '3off':
        lines[2] ='0'
        changeststus()
    if sys.argv[x-1]== '4on':
        lines[3] ='1'
        changeststus()
    if sys.argv[x-1]== '4off':
        lines[3] ='0'
        changeststus()
    if sys.argv[x-1]== '5on':
        lines[4] ='1'
        changeststus()
    if sys.argv[x-1]== '5off':
        lines[4] ='0'
        changeststus()
    if sys.argv[x-1]== '6on':
        lines[5] ='1'
        changeststus()
    if sys.argv[x-1]== '6off':
        lines[5] ='0'
        changeststus()
    if sys.argv[x-1]== '7on':
        lines[6] ='1'
        changeststus()
    if sys.argv[x-1]== '7off':
        lines[6] ='0'
        changeststus()
    if sys.argv[x-1]== '8on':
        lines[7] ='1'
        changeststus()
    if sys.argv[x-1]== '8off':
        lines[7] ='0'
        changeststus()
    if sys.argv[x-1]== '9on':
        lines[8] ='1'
        changeststus()
    if sys.argv[x-1]== '9off':
        lines[8] ='0'
        changeststus()
    if sys.argv[x-1]== '10on':
        lines[9] ='1'
        changeststus()
    if sys.argv[x-1]== '10off':
        lines[9] ='0'
    if sys.argv[x-1]== '11on':
        lines[10] ='1'
        changeststus()
    if sys.argv[x-1]== '11off':
        lines[10] ='0'
        changeststus()
    if sys.argv[x-1]== '12on':
        lines[11] ='1'
        changeststus()
    if sys.argv[x-1]== '12off':
        lines[11] ='0'
        changeststus()
    if sys.argv[x-1]== '13on':
        lines[12] ='1'
        changeststus()
    if sys.argv[x-1]== '13off':
        lines[12] ='0'
        changeststus()
    if sys.argv[x-1]== '14on':
        lines[13] ='1'
        changeststus()
    if sys.argv[x-1]== '14off':
        lines[13] ='0'
        changeststus()
    if sys.argv[x-1]== '15on':
        lines[14] ='1'
        changeststus()
    if sys.argv[x-1]== '15off':
        lines[14] ='0'
        changeststus()
    if sys.argv[x-1]== '16on':
        lines[15] ='1'
        changeststus()
    if sys.argv[x-1]== '16off':
        lines[15] ='0'
        changeststus()
    if sys.argv[x-1]== '2.1on':
        lines[16] ='1'
        changeststus()
    if sys.argv[x-1]== '2.1off':
        lines[16] ='0'
        changeststus()
    if sys.argv[x-1]== '2.2on':
        lines[17] ='1'
        changeststus()
    if sys.argv[x-1]== '2.2off':
        lines[17] ='0'
        changeststus()
    if sys.argv[x-1]== '2.3on':
        lines[18] ='1'
        changeststus()
    if sys.argv[x-1]== '2.3off':
        lines[18] ='0'
        changeststus()
    if sys.argv[x-1]== '2.4on':
        lines[19] ='1'
        changeststus()
    if sys.argv[x-1]== '2.4off':
        lines[19] ='0'
        changeststus()
    if sys.argv[x-1]== '2.5on':
        lines[20] ='1'
        changeststus()
    if sys.argv[x-1]== '2.5off':
        lines[20] ='0'
        changeststus()
    if sys.argv[x-1]== '2.6on':
        lines[21] ='1'
        changeststus()
    if sys.argv[x-1]== '2.6off':
        lines[21] ='0'
        changeststus()
    if sys.argv[x-1]== '2.7on':
        lines[22] ='1'
        changeststus()
    if sys.argv[x-1]== '2.7off':
        lines[22] ='0'
        changeststus()
    if sys.argv[x-1]== '2.8on':
        lines[23] ='1'
        changeststus()
    if sys.argv[x-1]== '2.8off':
        lines[23] ='0'
        changeststus()