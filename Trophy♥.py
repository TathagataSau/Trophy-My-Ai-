# -*- coding: utf-8 -*-
"""
Created on sun Apr 17 16:27:07 2022

@author: Tathagata Sau
"""
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import wikipedia
import sys

listener = sr.Recognizer()
engine = pyttsx3.init()
voices= engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
engine.setProperty("rate",150)
#engine.say('I am your trophy dear')
#engine.say('I am at your service')
def talk(text):
    engine.say(text)
    engine.runAndWait()
  
def take_command():
    try:
            with sr.Microphone() as source:
                print('listening...')
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command =command.lower()
                if 'trophy' in command:
                    command = command.replace('trophy','')
                    print(command)
      #              talk(command)
    except:
            print('exiting..... , No inputs given')
            talk('exiting , No inputs given')
            
    return command

def run_trophy(loopCounter):
    if loopCounter == 0:
              talk('Welcome I am Trophy,your virtual assistant. listning?')
    command = take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing'+ song)
        print('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I %M %p')
        print(time)
        talk('current time is'+ time)
    elif'who is' in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person,2)
        print(info)
        talk(info)
    elif'what is' in command and 'your name' not in command:
        thing=command.replace('what is','')
        info=wikipedia.summary(thing,2)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('ya, sure! but first make me a human')
    elif'you single' in command:
        talk('Dont be a jerk, im already in a relationship with wifi')
    elif'marry'in command:
        talk('nope! marriage sucks')
    elif'love'in command:
        talk('ohh thats so sweet')
    elif'how are you'in command:
        talk('I am fine dear, oh you are so careing sweetie!!')
    elif'who are you'in command and 'parents'not in command and 'mother and father' not in command and ' mum and dad'not in command:
        talk('my name is Trophy Dear')
    elif'what is your name'in command:
        talk('my name is Trophy Dear')
    elif'joke'in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())
    elif'your parents'in command or 'your father and mother' in command or 'your dad and mum'in command:
        talk('Tathagata and Ayusmita made me. so technically they are my parents')
    elif'stop'in command or 'exit'in command or 'go to hell'in command:
        talk("I am so sorry! I am incompedent, couldn't satisfy you")
        print(sys.exit())
    else:
        talk('please repeat again, I did not get that')

counter = 0

while True:        
    run_trophy(counter)  
    counter += 1
