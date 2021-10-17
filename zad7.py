'''Przygotować funkcję, która przyjmie 1 argument w postaci listy,
a następnie zwróci te elementy w postaci krotki.
'''
list = [2.3, 41, 24, 64, 42]

def zwrocKrotke(list):
    return tuple(list)

print(zwrocKrotke(list))