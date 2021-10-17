'''Przygotować funkcję, która przyjmie 2 argumenty, a następnie zwróci wynik ich dzielenia.
Należy sprawdzić w jednej
instrukcji if (bez użycia elif i else), czy obydwie liczby są dodatnie oraz czy druga liczba
jest różna od 0.'''

a = int(input("Podaj liczbe a: "))
b = int(input("Podaj liczbe b: "))

def zwrocDzielenie(a, b):
    if b==0:
        return "Nie mozna dzielic przez 0"
    if a<0 or b<0:
        return "Obydwie liczby musza byc dodatnie"
    return a/b

print(zwrocDzielenie(a, b))