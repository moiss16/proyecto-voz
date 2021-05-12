import speech_recognition as sr
import time 
import webbrowser
import playsound
import os
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            alexa_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)

        except sr.UnknownValueError:
            alexa_speak('Lo siento, no te entendi')
        except sr.RequestError:
            alexa_speak('Lo siento, error de conexion')
        return voice_data

def alexa_speak(audio_string):
    tts = gTTS(text=audio_string, lang= 'es')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'como te llamas' in voice_data:
        alexa_speak('Mi nombre es cuentacuentos')
    if 'tiempo' in voice_data:
        alexa_speak(ctime())

    if 'cuento' in voice_data:
        buscar = record_audio('Que cuento buscar?')
        url = 'https://www.youtube.com/results?search_query=' + buscar
        webbrowser.get().open(url)
        alexa_speak('Esto fue lo que encontre para: ' + buscar)

    if 'buscar' in voice_data:
        buscar = record_audio('Que cuento ?')
        url = 'https://arbolabc.com/cuentos-clasicos-infantiles/' + buscar #pinocho, 
        webbrowser.get().open(url)
        alexa_speak('Esto fue lo que encontre para: ' + buscar)

    if 'callate' in voice_data:
        exit()



#print('Como te puedo ayudar?')
#voice_data = record_audio()
#respond(voice_data)


time.sleep(1)
alexa_speak('Como te puedo ayudar?')
while 1:
    voice_data = record_audio()
    respond(voice_data)