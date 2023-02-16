import speech_recognition as sr
r=sr.Recognizer()
mic=sr.Microphone()

speech= sr.AudioFile('harvard.wav')
with mic as source:
#    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
output=r.recognize_sphinx(audio)
print(output)
