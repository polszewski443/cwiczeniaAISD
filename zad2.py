'''Przygotować funkcję, która przyjmie w parametrach imię i nazwisko, oraz zwróci pierwszą literę
imienia i nazwisko połączone kropką. Funkcja powinna również dbać o poprawność wielkich liter. Przykładowo, wejście:
(jan, kowalski), wyjście: J. Kowalski.'''
a = input("Podaj imie: ")
b = input("Podaj nazwisko: ")

def zwrocWarPolKropka(a, b):
    return (a[0].upper()+'.'+" "+b.capitalize())

print(zwrocWarPolKropka(a, b))