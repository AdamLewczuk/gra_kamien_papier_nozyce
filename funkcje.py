import random
def wypisz_ruch(wybierz):
    if wybierz == '1':
        return "Kamień"
    if wybierz == '2':
        return "Papier"
    if wybierz == '3':
        return "Nożyce"

def komputer_losuje():
    losowanie = ["Kamień", "Papier", "Nożyce"]
    wynik = (random.choice(losowanie))
    return wynik

