import speech_recognition as sr
import re
#import sensor

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
    #==change to google for demonstration==

#output=interpret(r,mic)
#print(output)

#==for testing reasons only:==
output="what is the temperature"
#==remove for demonstration==

#tempresult=re.search("temperature",output)
if output == "what is the temperature":
    #====
    print("kinda warm idk")
    #==replace with actual temperature==
    
    #    temperature =sensor.temperature
    #    print (temperature)
elif output=="turn the light off" or output=="turn the lights off":
    #====
    print ("idk how yet sry")
    #==replace with actually turning off lights==