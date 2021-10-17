'''Przygotować funkcję, która przyjmie w parametrach pierwszą literę imienia, oraz nazwisko,
a następnie zwróci te wartości połączone kropką. Przykładowe wyjście: J. Kowalski.'''
a = input("Podaj imie: ")
b = input("Podaj nazwisko: ")

def zwrocWarPolKropka(a, b):
    return (a[0]+'.'+" "+b)

print(zwrocWarPolKropka(a, b))