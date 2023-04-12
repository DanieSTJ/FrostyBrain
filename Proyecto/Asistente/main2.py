import speech_recognition as sr
import pyttsx3
from main import main


name = 'siri'
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language="es-MX")
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
                print(rec)
    except:
        pass
    return rec

def run():
    rec = listen()
    if'contiene' in rec:
        talk('Buen día señor, su nevera contiene')
        nevera = main()
        print(main())
        StrA = "".join(nevera)
        if(StrA == 'bottle'):
            StrA = 'Agua'
            talk('por ahora solo'+ StrA)
        
run()   
    