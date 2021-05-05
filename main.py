import pyttsx3
import random

# engine = pyttsx3.init()
# engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PL-PL_PAULINA_11.0")
# engine.setProperty("rate", 140)
# engine.setProperty('age', 20)
# engine.say("Jak masz na imię?")
# engine.runAndWait()
# imie = input("Jak masz na imię?: ")
# print("Cześć", imie)
# engine.say("Cześć" + imie)
# engine.runAndWait()
# engine.say("Zagrajmy w kamień,papier,nożyce")
# engine.runAndWait()
# engine.say("Wybierz jedną z opcji z menu")
# engine.runAndWait()
# engine.say(imie + "Jeżeli chcesz wybrać Kamień wciśnij jeden. Papier wciśnij dwa. Nożyce wciśnij trzy. ")
# engine.runAndWait()
wybierz = input("Wybierz jedną z opcji: Kamień (1),Papier(2), Nożyce(3)")


def wypisz_ruch(wybierz):
    if wybierz == '1':
        return "Kamień"
    if wybierz == '2':
        return "Papier"
    if wybierz == '3':
        return "Nożyce"

wynik_wypisz_ruch = wypisz_ruch(wybierz)
print ("Wybierasz",wynik_wypisz_ruch)

def komputer_losuje():
    losowanie = ["Kamień", "Papier", "Nożyce"]
    wynik = (random.choice(losowanie))
    if wynik == "Kamień":
        return "Kamień"
    if wynik == "Papier":
        return "Papier"
    if wynik == "Nożyce":
        return "Nożyce"

wypisz = komputer_losuje()
print ("Ja wybrałem",wypisz)

# if wynik == "Kamień":
#     print("Ja wybrałem Kamień")
#     engine.say("Ja wybrałem Kamień")
#     engine.runAndWait()

# if wynik == "Papier":
#     print("Ja wybrałem Papier")
#     engine.say("Ja wybrałem Papier")
#     engine.runAndWait()

# if wynik == "Nożyce":
#     print("Ja wybrałem Nożyce")
#     engine.say("Ja wybrałem Nożyce")
#     engine.runAndWait()

# if wynik == "Papier" and wybierz == "2":
#     print("Jest Remis")
#     engine.say(imie + "Jest Remis")
#     engine.runAndWait()

# if wynik == "Papier" and wybierz == "3":
#     print("Wygrywasz")
#     engine.say(imie + "Wygrywasz")
#     engine.runAndWait()

# if wynik == "Papier" and wybierz == "1":
#     print("Przegrywasz")
#     engine.say(imie + "Przegrywasz")
#     engine.runAndWait()

# if wynik == "Kamień" and wybierz == "2":
#     print("Wygrywasz")
#     engine.say(imie + "Wygrywasz")
#     engine.runAndWait()

# if wynik == "Kamień" and wybierz == "3":
#     print("Przegrywasz")
#     engine.say(imie + "Przegrywasz")
#     engine.runAndWait()

# if wynik == "Kamień" and wybierz == "1":
#     print("Jest Remis")
#     engine.say(imie + "Jest Remis")
#     engine.runAndWait()

# if wynik == "Nożyce" and wybierz == "1":
#     print("Wygrywasz")
#     engine.say(imie + "Wygrywasz")
#     engine.runAndWait()

# if wynik == "Nożyce" and wybierz == "2":
#     print("Przegrywasz")
#     engine.say(imie + "Przegrywasz")
#     engine.runAndWait()

# if wynik == "Nożyce" and wybierz == "3":
#     print("Remis")
#     engine.say(imie + "Jest Remis")
#     engine.runAndWait()
#     print("Dziękuję za grę")
#     engine.say(imie + "Dziękuję za grę")
#     engine.runAndWait()