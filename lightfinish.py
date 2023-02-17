import serial
import time
import matplotlib.pyplot as plt
import numpy as np
import speech_recognition as sr
import re

ser = serial.Serial('COM3', 9600)
time.sleep(2)

def lightTurn(var):      
    if (var == '1'): #if the value is 1
        ser.write(b'1') #send 1
        print ("Light turned ON")
        time.sleep(1)
        
    if (var == '0'): #if the value is 0
        ser.write(b'0') #send 0
        print ("Light turned OFF")
        time.sleep(1)



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

output=interpret(r,mic)
#output="turn lights off"
print(output)

lightresult1=re.search("turn lights on",output)
if lightresult1 == None:
    pass
else:
    var = '1'
    lightTurn(var)
lightresult2=re.search("turn lights off",output)
if lightresult2 == None:
    pass
else:
    var = '0'
    lightTurn(var)