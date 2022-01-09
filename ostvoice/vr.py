import speech_recognition as sr

r=sr.Recognizer()
str_speech=""
with sr.Microphone() as source:
    print('speak anything')
    audio=r.listen(source)
    print('hello')
    try:
        text=r.recognize_sphinx(audio_data=audio)
        print('you said: {}'.format(text))
        str_speech=str_speech+format(text)
    except:
        print('sorry could not recognize your voice')
print(str_speech)

str_cmd=""
if(str_speech=="on"):
    str_cmd=str_cmd+"https://api.thingspeak.com/update?api_key=0JTSQNS4J5D11WB0&field1=1&field2=0&field3=1"
elif(str_speech=="off"):
    str_cmd=str_cmd+"https://api.thingspeak.com/update?api_key=0JTSQNS4J5D11WB0&field1=0&field2=0&field3=0"
else:
    print("speak again")

'''
mport speech_recognition as sr

# obtain path to "english.wav" in the same folder as this script
from os import path
#AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "test.wav")
AUDIO_FILE ="Raunak_off_2.wav"
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "french.aiff")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "chinese.flac")

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file

# recognize speech using Sphinx
try:
    #print("Sphinx thinks you said " + r.recognize_sphinx(audio))
    print("" + r.recognize_sphinx(audio_data=audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
'''
