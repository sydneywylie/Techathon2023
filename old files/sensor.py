import serial
import time
import matplotlib.pyplot as plt
import numpy as np

ser = serial.Serial('COM3', 9600)
time.sleep(2)

def tempratureFinder():
    temperatureList = []
    timeList = []
    timeRange = int(input("How many seconds would you like to observe for? "))

    for i in range(timeRange):
        line = ser.readline()  
        if line:
            string = line.decode()  
            temperature = float(string[:5])
            touch = float(string[5:])
            temperatureList.append(temperature)
            timeList.append(i+1)
        #if temperature > 21.00:
            #print("Room is above comfortable levels, heating will be reduced")      

    xpoints = timeList
    ypoints = temperatureList

    plt.plot(xpoints, ypoints)
    plt.show()