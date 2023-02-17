import serial
import time
 
ser = serial.Serial('COM3', 9600)
time.sleep(2)

def lightTurn(var):
    var = ''
    while True:      #Do this in loop
        if (var == '1'): #if the value is 1
            ser.write(b'1') #send 1
            print ("Light turned ON")
            time.sleep(1)
        
        if (var == '0'): #if the value is 0
            ser.write(b'0') #send 0
            print ("Light turned OFF")
            time.sleep(1)