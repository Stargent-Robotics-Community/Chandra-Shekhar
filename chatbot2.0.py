import datetime
import webbrowser
import pyttsx3 as pt
import pyowm
import wikipedia
import math
import cmath
import speech_recognition as sr
import pyaudio

erwin = pt.init()
voices = erwin.getProperty('voices')
erwin.setProperty('voice', voices[1].id)
volume = erwin.getProperty('volume')
erwin.setProperty('volume', 10.0)
rate = erwin.getProperty('rate')
erwin.setProperty('rate', rate - 25)

intro = 'Hello, my name is Erwin Rudolf Josef Alexander Schrödinger. I am here to fulfill your commands.'
erwin.say(intro)
erwin.runAndWait
r = sr.Recognizer()

def func():
    with sr.Microphone as source:
        print("What are my commands?")

        audio = r.listen(source)
        resp = r.recognize_google(audio)
        print(resp)

        try:
            if resp == ('hey there', 'hello', 'hi', 'Hai', 'hey!', 'hey'):
                print('erwin: hi sir!')
                erwin.say("Hi sir! I am erwin, how can I help you today?")
                erwin.runAndWait()

            elif resp == ('How are you?', 'How are you doing?'):
                print('erwin: "I am fine sir."')
                erwin.say('I am fine sir! how are you today?')
                erwin.runAndWait()
            
            elif resp == ('I am fine', "I am fine. thanks for asking!"):
                print('erwin: may god bless you with more health,sir')
                erwin.say('may god bless you with more health,sir')
                erwin.runAndWait()

            elif resp == ('Who are you?' , 'What are you?'):
                print('erwin: I am erwin!')
                erwin.say('I am a to be voice assisstant. My name is Erwin Rudolf Josef Alexander Schrödinger. I am here for your service')
                erwin.runAndWait()
            
            elif resp == ('who made you', 'who created you'):
                print('erwin:C.S.')
                erwin.say('I am created by C.S.')
                erwin.runAndWait()

            elif resp == ('what time is it', 'what is the time', 'time'):
                 print("erwin:Current date and time : ")
                 now = datetime.datetime.now()
                 print(now.strftime("The time is %H:%M"))
                 erwin.say(now.strftime("The time is %H:%M"))
                 erwin.runAndWait()
                 

            elif resp == ('open browser'):
                 print('erwin:Sir! Yes Sir!!')
                 erwin.say('Sir! Yes Sir!!')
                 webbrowser.open('www.google.com')
                 erwin.runAndWait()

            elif resp == ('Tell me a joke'):
                 print('erwin: I failed math so many times at school, I can’t even count')
                 erwin.say('I failed math so many times at school, I can’t even count')
                 erwin.runAndWait

            elif resp == ('open youtube', 'i want to watch a video'):
                 print('erwin: opening sir')
                 erwin.say('Sir! Yes Sir!!')
                 webbrowser.open('www.youtube.com')
                 erwin.runAndWait()

            elif resp == ("'tell me the weather', 'weather', 'what about the weather','What is the weather around'"):
                 owm = pyowm.OWM('c5205f9e69c78beb106762db8aaa82da')
                 observation = owm.weather_at_place('Jaipur, IN')
                 observation_list = owm.weather_around_coords(26.9124, 75.7873)
                 w = observation.get_weather()
                 w.get_wind()
                 w.get_humidity()
                 w.get_temperature('celsius')
                 print(w)
                 print(w.get_wind())
                 print(w.get_humidity())
                 print(w.get_temperature('celsius'))
                 erwin.say(w.get_wind())
                 erwin.runAndWait()
                 erwin.say('humidity')
                 erwin.runAndWait()
                 erwin.say(w.get_humidity())
                 erwin.runAndWait()
                 erwin.say('temperature')
                 erwin.runAndWait()
                 erwin.say(w.get_temperature('celsius'))
                 erwin.runAndWait()

            elif resp == ('thank you'):
                 print('erwin: you are most welcome sir')
                 erwin.say('you are most welcome sir')
                 erwin.runAndWait

            elif resp == ('What can you do?'):
                 print('erwin: I can tell you a joke, I can open your browser, I can open YouTube for you, I can tell you the weather in Jaipur, I can tell you the current local time, I can solve basic trigonometric questions for you to name a few.')
                 erwin.say('I can tell you a joke, I can open your browser, I can open YouTube for you, I can tell you the weather in Jaipur, I can tell you the current local time, I can solve basic trigonometric questions for you to name a few.')
                 erwin.runAndWait
            elif resp == ("'exit', 'close', 'goodbye', 'nothing'"):
                 print('erwin:see you later, sir!')
                 erwin.say('You are most welcome, Sir!!')
                 exit()

            elif resp== ("'whats your color', 'what is your colour', 'your color'"):
                 print('erwin: I am composed of whole VIBGYOR ')
                 erwin.say('I am composed of whole VIBGYOR')
                 erwin.runAndWait

            elif resp == ('What is your favorite color?'):
                 print('erwin:Its Mikado sir!')
                 erwin.say('Its mikado sir!')
                 erwin.runAndWait

            elif resp == ('thank you'):
                 print('erwin:glad i could help you')
                 erwin.say('glad i could help you')
                 erwin.runAndWait

            elif resp == ('play your favorite song'):
                 print('erwin:Playing Sir!')
                 erwin.say('playing sir. just a sec')
                 webbrowser.open('www.youtube.com/watch?v=DiItGE3eAyQ')

            elif resp == ('What can you solve in Trigonometery'):
                 print('erwin: I can convert degrees to radian; I can find cosine, sine, tangent values , I can find arccosine, arcsine, arctangent values  ; I can find hyperboliccosine, hyperbolicsine, hyperbolictangent values ; I can find inverse of hyperboliccosine, hyperbolicsine, hyperbolictangent values ; I can convert ; I can convert ; I can convert ;')
                 
            elif resp == ('convert radian to degree'):
                 cpi=input('enter the value')
                 erwin.say('enter the value')
                 cpi1 = print(math.degrees((cpi)))
                 erwin.say('cpi1')
                 erwin.runAndWait
                 

            elif resp == ('convert degree to radian'):
                 cdeg = input('enter the value')
                 erwin.say('enter the value')
                 cdeg2 = print(math.radians(cdeg))
                 erwin.say(cdeg2)
                 erwin.runAndWait

            elif resp == ('find value of sin,cos,tan','tell value of sin,cos,tan', 'value of sin,cos,tan','sin,cos,tan'):
                 fsin = input('enter the values')
                 fcos = input('enter the values')
                 ftan= input('enter the values')
                 erwin.say('enter the values')
                 fsine=print(math.sin(math.fsin))
                 ftane=print(math.tan(math.ftan))
                 fcose=print(math.cos(math.fcos))
                 erwin.say(fsine)
                 erwin.say(ftane)
                 erwin.say(fcose)


            elif resp == ('find value of arcsin,arccos,arctan','tell value of arcsin,acos,arctan', 'value of arcsin,arccos,arctan','arcsin,arccos,arctan'):
                 farcsin = input('enter the values')
                 farccose = input('enter the values')
                 farctane = input('enter the values')
                 erwin.say('enter the values')
                 farcsine=print(math.asin(farcsin))
                 farccos=print(math.acos(farccose))
                 farctan=print(math.atan(farctane))
                 erwin.say(farcsine)
                 erwin.say(farccos)
                 erwin.say(farctan)

            elif resp == ('find value of hyperbolic sin, hyperbolic tan, hyperbolic cos','tell value of hyperbolic sin, hyperbolic tan, hyperbolic cos', 'value of hyperbolic sin, hyperbolic tan, hyperbolic cos','hyperbolic sin, hyperbolic tan, hyperbolic cos'):
                 fhypsin = input('enter the values')
                 fhypcose = input('enter the values')
                 fhyptane = input('enter the values')
                 erwin.say('enter the values')
                 fhypsine= print (cmath.sinh(fhypsin))
                 fhypcos= print (cmath.cosh(fhypcose)) 
                 fhyptan= print (cmath.tanh(fhyptane))
                 erwin.say(fhypsine)
                 erwin.say(fhypcos)
                 erwin.say(fhyptan)
                 

            elif resp == ('find value of inverse hyperbolic sin, inverse hyperbolic tan, inverse hyperbolic cos','tell value of inverse hyperbolic sin, inverse hyperbolic tan, inverse hyperbolic cos', 'value of inverse hyperbolic sin, inverse hyperbolic tan, inverse hyperbolic cos','inverse hyperbolic sin, inverse hyperbolic tan, inverse hyperbolic cos'):
                 fhypisin = input('enter the values')
                 fhypicose = input('enter the values')
                 fhypitane = input('enter the values')
                 erwin.say('enter the values')
                 fhypisine= print (cmath.asinh(fhypisin))
                 fhypicos= print (cmath.acosh(fhypicose)) 
                 fhypitan= print (cmath.atanh(fhypitane))
                 erwin.say(fhypisine)
                 erwin.say(fhypicos)
                 erwin.say(fhypitan)
                 
            else:
                erwin.say("please wait")
                erwin.runAndWait()
                wikipedia.summary(r.recognize_google(audio))
                erwin.say(wikipedia.summary(r.recognize_google(audio)))
                erwin.runAndWait()
                userInput3 = input("or else search in google")
                webbrowser.open_new('www.google.com/search?q=' + userInput3)
    
            
        except:
            erwin.say("sorry; Try again")
            print(": sorry try again")
            return func()
func()


                 
                 



                