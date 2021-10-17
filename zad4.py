'''Przygotować funkcję, która przyjmie 3 parametry: imię, nazwisko i funkcję przetwarzającą te dane,
a następnie zwróci wynik działania funkcji przyjętej
w 3. parametrze. Przykładwo, wejście: (jan, kowalski, funkcja_z_zadania_2), wyjście: J. Kowalski.'''

a = input("Podaj imie: ")
b = input("Podaj nazwisko: ")

def zwrocWarPolKropka(a, b):
    return (a[0].upper()+'.'+" "+b.capitalize())

def przygotowanaFunkcja(a, b, f):
#    return (a + ' ' + b + ' to w skrocie ' + zwrocWarPolKropka)
    return f(a,b)

print(przygotowanaFunkcja(a, b, zwrocWarPolKropka))