import pyttsx3
import random
import funkcje

engine = pyttsx3.init()
engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PL-PL_PAULINA_11.0")
engine.setProperty("rate", 140)
engine.setProperty('age', 20)

engine.say("Jak masz na imię?")
engine.runAndWait()
imie = input("Jak masz na imię?: ")
print("Cześć", imie)
engine.say("Cześć" + imie)
engine.say("Zagrajmy w kamień,papier,nożyce")

def graj():
    engine.say("Wybierz jedną z opcji z menu")
    engine.say(imie + "Jeżeli chcesz wybrać Kamień wciśnij jeden. Papier wciśnij dwa. Nożyce wciśnij trzy. ")
    engine.runAndWait()
    wybierz = input("Wybierz jedną z opcji: Kamień (1),Papier(2), Nożyce(3)")
    wynik_wypisz_ruch = funkcje.wypisz_ruch(wybierz)
    wynik = funkcje.komputer_losuje()
    sprawdzam = funkcje.sprawdzwynik(wybierz,wynik)
    print ("Ty wybrałeś",wynik_wypisz_ruch,"Ja wybrałem",wynik,"Ty",sprawdzam)
    engine.say("Ty wybrałeś" + wynik_wypisz_ruch + "Ja wybrałem" + wynik + "Ty" + sprawdzam)
    engine.runAndWait()

    print(sprawdzam)
graj()  
ponownie = input("Jeżeli chcesz zagrać ponownie wciśnij 1")
if ponownie == "1":
    graj()
else: print("Dziękuje za grę")