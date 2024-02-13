import speech_recognition as sr
import pyttsx3
import platform
import os
from time import sleep

title = """
              ___           ___           ___         ___           ___           ___                         ___     
             /__/\         /__/\         /  /\       /__/\         /  /\         /  /\                       /  /\    
             \  \:\        \  \:\       /  /::\      \  \:\       /  /::|       /  /::|                     /  /:/_   
              \  \:\        \  \:\     /  /:/\:\      \  \:\     /  /:/:|      /  /:/:|     ___     ___    /  /:/ /\  
          ___  \  \:\   _____\__\:\   /  /:/~/:/  ___  \  \:\   /  /:/|:|__   /  /:/|:|__  /__/\   /  /\  /  /:/ /:/_ 
         /__/\  \__\:\ /__/::::::::\ /__/:/ /:/  /__/\  \__\:\ /__/:/ |:| /\ /__/:/ |:| /\ \  \:\ /  /:/ /__/:/ /:/ /\
         \  \:\ /  /:/ \  \:\~~\~~\/ \  \:\/:/   \  \:\ /  /:/ \__\/  |:|/:/ \__\/  |:|/:/  \  \:\  /:/  \  \:\/:/ /:/
          \  \:\  /:/   \  \:\  ~~~   \  \::/     \  \:\  /:/      |  |:/:/      |  |:/:/    \  \:\/:/    \  \::/ /:/ 
           \  \:\/:/     \  \:\        \  \:\      \  \:\/:/       |  |::/       |  |::/      \  \::/      \  \:\/:/  
            \  \::/       \  \:\        \  \:\      \  \::/        |  |:/        |  |:/        \__\/        \  \::/   
             \__\/         \__\/         \__\/       \__\/         |__|/         |__|/                       \__\/    
"""

# Initialize the recognizer
r = sr.Recognizer()
mic = sr.Microphone(device_index=0)

speech_error = "Could not understand audio. Please try again."

# Initialize the speech engine
engine = pyttsx3.init()

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def speech_text_speech():
    try:
        # Use the microphone as source for input
        detected = False
        while detected == False:
            with mic as source:
                print("Say something...")
                audio = r.listen(source)
            try:
                result = r.recognize_google(audio)
                print(result)
                detected = True
            except sr.exceptions.UnknownValueError as e:
                print(speech_error)
                engine.say(speech_error)
                
        # Use pyttsx3 to convert the text into speech
        engine.say(result)
        engine.runAndWait()

    except KeyboardInterrupt as e:
        clear_screen()
        print("Exiting...")
        exit(0)
        
if __name__ == "__main__":
    clear_screen()
    print(title)
    sleep(2)
    clear_screen()
    speech_text_speech()