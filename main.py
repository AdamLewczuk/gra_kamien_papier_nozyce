import pyttsx3
import random
import funkcje

engine = pyttsx3.init()
engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PL-PL_PAULINA_11.0")
engine.setProperty("rate", 140)
engine.setProperty('age', 20)
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

wynik_wypisz_ruch = funkcje.wypisz_ruch(wybierz)
print ("Wybierasz",wynik_wypisz_ruch)

wypisz = funkcje.komputer_losuje()
print ("Ja wybrałem",wypisz)
engine.say("Ja wybrałem" + wypisz)
engine.runAndWait()


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