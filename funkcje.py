#funkcja wypisująca ruch. Zwraca ruch wybrany przez gracza po kliknięciu odpowiedniego klawisza
import random
def wypisz_ruch(wybierz):
    if wybierz == '1':
        return "Kamień"
    if wybierz == '2':
        return "Papier"
    if wybierz == '3':
        return "Nożyce"


#funkcja losująca. Losuje jako komputer między konkretnym ruchem.

def komputer_losuje():
    losowanie = ["Kamień", "Papier", "Nożyce"]
    wynik = (random.choice(losowanie))
    return wynik

# funkcja sprawdzająca płeć po wpisaniu imienia. Zwraca wartość True gdy kobieta i False gdy mężczyzna. 

def czy_kobieta(imie):
    if imie == "Kuba":
        return False
    elif imie[-1] == "a":
        return True
    else:
        return False

# funkcja sprawdzająca końcowy wynik. Zwraca wartość w postaci wyniku. 

def sprawdzwynik(wybierz,wynik):
    if wybierz == "1" and wynik == "Kamień":
        x = "Jest remis"
        return x
    elif wybierz == "1" and wynik == "Papier":
        x = "Przegrywasz"
        return x
    elif wybierz == "1" and wynik == "Nożyce":
        x = "Wygrywasz"
        return x
   
    
