import pyttsx3
import random
import funkcje
import speech_recognition as sr


engine = pyttsx3.init()
engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PL-PL_PAULINA_11.0")
engine.setProperty("rate", 140)
engine.setProperty('age', 20)

engine.say("Jak masz na imię?")
engine.runAndWait()
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Słucham...")
    audio = r.listen(source)
    imie = r.recognize_google(audio,language="pl-PL")
print("Cześć", imie)
engine.say("Cześć" + imie)
engine.say("Zagrajmy w kamień,papier,nożyce")


def graj():
    engine.say("Powiedz co wybierasz")
    engine.runAndWait()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Słucham...")
        audio = r.listen(source)
        wybierz = r.recognize_google(audio,language="pl-PL")
        print(wybierz)
   
    wynik_wypisz_ruch = funkcje.wypisz_ruch(wybierz)
    wynik = funkcje.komputer_losuje()
    sprawdzam = funkcje.sprawdzwynik(wybierz,wynik)
    print ("Ty wybrałeś",wynik_wypisz_ruch,"Ja wybrałem",wynik,"Ty",sprawdzam)
    engine.say("Ty wybrałeś" + wynik_wypisz_ruch + "Ja wybrałem" + wynik + "Ty" + sprawdzam)
    engine.runAndWait()

def ponow():
    ponownie = input("Jeżeli chcesz zagrać ponownie wciśnij 1. Jeżeli chcesz zakończyć wciśnij 2") 
    if ponownie == "1":
        return ponownie == "1"
    if ponownie == "2":
        exit()
isNewGame = True
while isNewGame:
   graj()
   isNewGame = ponow()
else: print("Dziekuję za grę")
#dsdsd