'''Przygotować funkcję, która przyjmie 3 argumenty: 2 pierwsze cyfry aktualnego roku,
2 ostatnie cyfry aktualnego roku,
wiek użytkownika, a następnie zwróci jego rok urodzenia.'''

rok = input("Podaj rok: ")
wiek = int(input("Podaj swoj wiek: "))
arr = list(rok)
pierwDwa = arr[0]+arr[1]
ostDwa = arr[len(arr)-2]+arr[len(arr)-1]

def zwrocRokUrodzenia(pierwDwa, ostDwa, wiek):
    wybranyRok = pierwDwa+ostDwa
    wybranyRok = int(wybranyRok)
    return wybranyRok-wiek

print(zwrocRokUrodzenia(pierwDwa,ostDwa,wiek))
