import serial
import time

ser = serial.Serial('COM3', 9600)
time.sleep(2)

while True:
    line = ser.readline()  
    if line:
        string = line.decode()  
        temperature = float(string[-7:])
        print(temperature)
    if temperature > 21.00:
        print("Room is above comfortable levels, heating will be reduced")      