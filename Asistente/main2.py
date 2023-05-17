import speech_recognition as sr
import pyttsx3
from main import main
from nivel import obtener_nivel_agua


name = 'alexa'
listener = sr.Recognizer()
engine = pyttsx3.init()


voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

green_color = "\033[1;32;40m"
red_color = "\033[1;31;40m"

def listen():
    try:
        with sr.Microphone() as source:
            print(f"{red_color}Escuchando...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language="es-MX")
            rec = rec.lower()
            status = True
            if name in rec:
                rec = rec.replace(name, '')
                print(rec)
    except:
        pass
    return rec

elementos_seguros = ["Cerveza", "Manzana", "Naranja","Zanahoria","Brocoli","Banano"]
nueva_lista = []

def run():
    rec = listen()
    
    if 'cantidad' in rec:
        nivel = obtener_nivel_agua()
        print(nivel)
        nivelstr = str(nivel)
        talk('Señor, su jarra contiene:' + nivelstr + "porciento de agua")
        if nivel <= 20 and nivel > 0:
            talk('Señor, su nivel de agua esta en el 20 porciento o por debajo de este, por favor llene la jarra nuevamente')
        elif nivel == 0 and nivel <=0:
            talk('Señor, su jarra se encuentra vacia')
        #talk('Buen día señor, no he logrado realizar las conexiones necesarias para ese procesamiento... consulte más tarde')    
    elif'contiene' in rec:
        talk('Buen día señor, su nevera contiene...')
        nevera = main()
        for i in range(len(nevera)):
            if nevera[i] == "bottle":    
                nevera[i] = "Cerveza"
            elif nevera[i] == "apple":
                nevera[i] = "Manzana"
            elif nevera[i] == "orange":
                nevera[i] = "Naranja"
            elif nevera[i] == "carrot":
                nevera[i] = "Zanahoria"
            elif nevera[i] == "broccoli":
                nevera[i] = "Brocoli"
            elif nevera[i] == "banana":
                nevera[i] = "Banano"
                
        for elemento in nevera:
             if elemento in elementos_seguros:
                nueva_lista.append(elemento)
        
        cantidades = {}
        
        for elemento in nueva_lista:
            if elemento in cantidades:
                 cantidades[elemento] += 1
            else:
                 cantidades[elemento] = 1
        
        elementos_cantidades = []
        for elemento, cantidad in cantidades.items():
            elementos_cantidades.append(f"{cantidad} {elemento}")

        StrA = ",  ".join(elementos_cantidades)
        talk('por ahora solo'+ StrA)
    
        
         
        
run()   
    