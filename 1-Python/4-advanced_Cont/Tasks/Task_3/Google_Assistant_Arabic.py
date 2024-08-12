# import library
import webbrowser
from time import ctime
import os
import playsound
from gtts import gTTS
import random
import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()


# Reading Audio file as source
# listening the audio file and store in audio_text variable
def Bixby_Speak(audios):
    tts = gTTS(text=audios, lang='ar', slow=False)
    # tts = gTTS(text=audios, lang='en')
    audioF = 'audio.mp3'
    tts.save(audioF)
    playsound.playsound(audioF)
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
            voice_data = r.recognize_google(audio, language="ar")
        except sr.UnknownValueError:
            Bixby_Speak("عفوا لم اسمع طلبك") 
        except sr.RequestError:
            Bixby_Speak("sorry Service is Down")
        return voice_data.lower()


def Respond(voice_data):
    if 'الاسم' in voice_data or 'اسم' in voice_data:
        Bixby_Speak('اهلا بحسن البهنسى')
        # Bixby_Speak('Moatasem Big Boss')
    if 'الوقت' in voice_data or 'الساعه' in voice_data:
        Bixby_Speak(ctime())
    if 'بحث' in voice_data or 'البحث' in voice_data:
        search = record('ما الموضوع الذى تريده للبحث عنه')
        # search = record('what dow want to search')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        # Bixby_Speak('Here is what i Found For' + search)

        Bixby_Speak('هذا ما وجدته فى البحث عن' + search)
    if 'لينكد ان' in voice_data or 'لينكدان' in voice_data:
        url = 'https://www.linkedin.com/in/hassan-bahnasy-7b4952253/'
        webbrowser.get().open(url)
        Bixby_Speak('تفضل ')
    if 'جيت هاب' in voice_data or 'جيت هب' in voice_data:
        url = 'https://github.com/Bahnasy2001/Embedded_Linux_Diploma' 
        webbrowser.get().open(url)
        Bixby_Speak('تفضل')
    if 'المكان' in voice_data or 'فين' in voice_data:
        location = record("ما المكان الذى تسأل عنه")
        # location = record("what is the location do want ")
        url = 'https://google.nl/maps/place/' + location + '/&amp'
        webbrowser.get().open(url)
        # Bixby_Speak('Here is what i Found For' + location)
        Bixby_Speak('هذا ما وجدته لمعرفه مكان' + search)

    if 'شكرا لك' in voice_data:
        Bixby_Speak('العفو الى اللقاء')
        exit()
    # Bixby_Speak('How Can I help You')


Bixby_Speak('صباح الخير')
while 1:
    voice_data = record()
    Respond(voice_data)
