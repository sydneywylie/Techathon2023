import serial
import time
import matplotlib.pyplot as plt
import numpy as np
import speech_recognition as sr
import re

ser = serial.Serial('COM3', 9600)
time.sleep(2)

def tempratureFinder():
    temperatureList = []
    timeList = []
    #timeRange = int(input("How many seconds would you like to observe for? "))
    timeRange = 10

    for i in range(timeRange):
        line = ser.readline()  
        if line:
            string = line.decode()  
            temperature = float(string[:5])
            touch = float(string[5:])
            temperatureList.append(temperature)
            timeList.append(i+1)
            print(temperature)
    

r=sr.Recognizer()
mic=sr.Microphone()
speech= sr.AudioFile('harvard.wav')
def interpret(r,mic):
    with mic as source:
        r.adjust_for_ambient_noise(source,duration=0.5)
        print("ready")
        audio = r.listen(source)
    #====
    return r.recognize_sphinx(audio)
    #return r.recognize_google(audio)
    #==change to google for demonstration==

#output=interpret(r,mic)
output="what is the temperature"
print(output)

tempresult=re.search("what is the temperature",output)
if tempresult == None:
    pass
else:   
    tempratureFinder()








