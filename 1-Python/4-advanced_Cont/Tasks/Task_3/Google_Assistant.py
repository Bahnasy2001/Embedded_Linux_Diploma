# import library
import webbrowser
from time import ctime
import os
import playsound
from gtts import gTTS
import random
import speech_recognition as sr
import datetime

# Initialize recognizer class (for recoginizing the speech)
r = sr.Recognizer()

# Reading Audio file as source
# Listening the audio file and store in audio_text variable
def Bixby_Speak(audios):
    tts = gTTS(text=audios,lang='en',slow = False)
    audioF = 'audio.mp4'
    tts.save(audioF)
    playsound.playsound(audioF,True)
    print(audios)
    os.remove(audioF)



def record(ask=False):
    with sr.Microphone(device_index=None) as source:
        r.adjust_for_ambient_noise(source)
        if ask:
            Bixby_Speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data= r.recognize_google(audio, language = "en" )
        except sr.UnknownValueError:
            Bixby_Speak("sorry i did not get that")
        except sr.RequestError:
            Bixby_Speak("sorry Service is Down")
        return voice_data.lower()
    
def Respond(voice_data):
    if 'name' in voice_data or 'the name' in voice_data:
        Bixby_Speak("Welcome Mr. Hassan Bahansy")
    if 'time' in voice_data or 'the time' in voice_data:
        Bixby_Speak(ctime())
    if 'date' in voice_data or 'the date' in voice_data:
        Bixby_Speak(datetime.datetime.now().strftime("%A %m/%d/%Y"))
    if 'search' in voice_data or 'the search' in voice_data:
        search = record("what do want to search")
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        Bixby_Speak('Here is what i Found For' + search)
    if 'location' in voice_data or 'where' in voice_data:
        location = record("what is the location do want")
        url = 'https://google.nl/maps/place/' + location + '/&amp'
        webbrowser.get().open(url)
        Bixby_Speak('Here is what i Found For' + location)
    if 'github' in voice_data:
        url = 'https://github.com/Bahnasy2001/Embedded_Linux_Diploma' 
        webbrowser.get().open(url)
        Bixby_Speak("This is your github repository")
    if 'linkedin' in voice_data:
        url = 'https://www.linkedin.com/in/hassan-bahnasy-7b4952253/'
        webbrowser.get().open(url)
        Bixby_Speak("This is your Linkedin Account")
    if 'exit' in voice_data or 'goodbye' in voice_data:
        Bixby_Speak("Good Bye Mr. Hassan")
        exit()
        
Bixby_Speak("Good Morning")
while True:
    voice_data = record()
    print(voice_data)
    Respond(voice_data)