
#funkcja wypisująca ruch. Zwraca ruch wybrany przez gracza po kliknięciu odpowiedniego klawisza
import random
def wypisz_ruch(wybierz):
    if wybierz == 'kamień':
        return "kamień"
    if wybierz == '2':
        return "papier"
    if wybierz == '3':
        return "nożyce"


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

# funkcja sprawdzająca końcowy wynik. Zwraca wartość w postaci zmiennej x. 

def sprawdzwynik(wybierz,wynik):
    if wybierz == "kamień" and wynik == "Kamień":
        x = "Jest remis"
        return x
    elif wybierz == "kamień" and wynik == "Papier":
        x = "Przegrywasz"
        return x
    elif wybierz == "kamień" and wynik == "Nożyce":
        x = "Wygrywasz"
        return x
    elif wybierz == "papier" and wynik == "Kamień":
        x = "Wygrywasz"
        return x
    elif wybierz == "papier" and wynik == "Papier":
        x = "Remis"
        return x
    elif wybierz == "papier" and wynik == "Nożyce":
        x = "Przegrywasz"
        return x
    elif wybierz == "nożyce" and wynik == "Kamień":
        x = "Przegrywasz"
        return x
    elif wybierz == "nożyce" and wynik == "Papier":
        x = "Wygrywasz"
        return x
    elif wybierz == "nożyce" and wynik == "Nożyce":
        x = "Remis"
        return x

# funkcja mówiąca
# def mow():
#     lista = ["Zagrajmy w kamień, papier, nożyce","Wybierz jedną z opcji w menu","Jeżeli chcesz wybrać Kamień wciśnij jeden. Papier wciśnij dwa. Nożyce wciśnij trzy. "]
#     return lista

# wywolaj_mowi = mow()
# print(wywolaj_mowi[1])

# pole = ""
# if pole == False:
#     print("nie nie wpisałeś")
# else:
#     pole == True
#     print("wpisałeś")

# pole2 = ""
# if not pole2:
#     print("Nie wpisałeś")
# else: print("cos wpisales")