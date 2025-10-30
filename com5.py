import serial
import time

WAIT=0.2

ser = serial.Serial('COM8', 9600)
time.sleep(2) # シリアルポートが安定するまで待機
message1 = "\r\n"
message3 = 'LIST\r\n'

import sys

time.sleep(WAIT)
for char in message1:
    ser.write(char.encode('utf-8'))
    time.sleep(WAIT)


for l in sys.stdin:
    print(l)
    time.sleep(WAIT)
    for bs in l.rstrip('\r\n')+"\r\n":
        ser.write(bs.encode('utf-8'))
        time.sleep(WAIT)

time.sleep(WAIT)
for char in message3:
    ser.write(char.encode('utf-8'))
    time.sleep(WAIT)

seq = []
count = 1

while True:
    for c in ser.read():
        seq.append(chr(c)) #convert from ANSII
        joined_seq = ''.join(str(v) for v in seq) #Make a string from array

        if chr(c) == '\n':
            print("Line " + str(count) + ': ' + joined_seq)
            seq = []
            count += 1
            break

ser.close()
print("送信完了")
