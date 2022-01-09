from django.shortcuts import render
import speech_recognition as sr
import webbrowser
from selenium import webdriver
from time import sleep

'''
r=sr.Recognizer()
str_speech=""
with sr.Microphone() as source:
    print('speak anything')
    audio=r.listen(source)
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
    
webbrowser.open(str_cmd,2)
'''

def homepage(request):
    return render(request,'index.html')

def analysispage(request):
    r=sr.Recognizer()
    mess=''

    if request.method=='POST':
        myfile = request.FILES['input_voice']

    with sr.AudioFile(myfile) as source:
    #with sr.Microphone() as source:
        #print('speak anything')
        #audio=r.listen(source)
        r.adjust_for_ambient_noise(source)
        audio = r.record(source)
        str_cmd = ""
        
        try:
            mess = r.recognize_sphinx(language="en-US", audio_data=audio)
            #text2=r.recognize_sphinx(language="en-IN", audio_data=audio)
            '''
            if(text=="on" or text2=="on"):
                print("on")
                mess="On, probably works."
                str_cmd=str_cmd+"https://api.thingspeak.com/update?api_key=0JTSQNS4J5D11WB0&field1=1&field2=0&field3=1"
                browser = webdriver.Firefox(executable_path = <geckodriver_driver_path>)
                browser.get(str_cmd)  
                sleep(1)
                browser.close()
            elif(text=="off" or text2=="off"):
                print("off")
                mess="Off, elif probably works."
                str_cmd=str_cmd+"https://api.thingspeak.com/update?api_key=0JTSQNS4J5D11WB0&field1=0&field2=0&field3=0"
                browser = webdriver.Firefox(executable_path = <geckodriver_driver_path>)
                browser.get(str_cmd)
                sleep(1)
                browser.close()                       
            else:
                print("speak again")
                mess="You'll have to speak again."
            '''
                
        except Exception as e:
            print('Exception found: ',e)
            mess='Sorry! Could not recognize your voice.'

    return render(request,'apage.html',{'message':mess})