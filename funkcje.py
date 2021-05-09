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

# funkcja sprawdzająca końcowy wynik. Zwraca wartość w postaci zmiennej x. 

def sprawdz_wynik(wybierz,wynik):
    if wybierz == "1" and wynik == "Kamień":
        x = "Jest remis"
     
    elif wybierz == "1" and wynik == "Papier":
        x = "Przegrywasz"
        
    elif wybierz == "1" and wynik == "Nożyce":
        x = "Wygrywasz"
      
    elif wybierz == "2" and wynik == "Kamień":
        x = "Wygrywasz"
       
    elif wybierz == "2" and wynik == "Papier":
        x = "Remis"
      
    elif wybierz == "2" and wynik == "Nożyce":
        x = "Przegrywasz"
   
    elif wybierz == "3" and wynik == "Kamień":
        x = "Przegrywasz"
    
    elif wybierz == "3" and wynik == "Papier":
        x = "Wygrywasz"
     
    elif wybierz == "3" and wynik == "Nożyce":
        x = "Remis"
    return x

# funkcja mówiąca
def mow():
    lista = ["Zagrajmy w kamień, papier, nożyce","Wybierz jedną z opcji w menu","Jeżeli chcesz wybrać Kamień wciśnij jeden. Papier wciśnij dwa. Nożyce wciśnij trzy. "]
    return lista

wywolaj_mowi = mow()
print(wywolaj_mowi[1])