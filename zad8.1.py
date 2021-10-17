'''Przygotować skrypt, w którym użytkownik będzie wprowadzał do listy wartości używając pętli,
a następnie wartości z tej zostanią zrzutowane do krotki.
'''

list = []
list.append(int(input("Wprowadz wartosc do listy, jesli nie chcesz juz ich wprowadzac wprowadz 0: ")))
while list[len(list)-1] is not 0:
    list.append(int(input("Wprowadz wartosc do listy, jesli nie chcesz juz ich wprowadzac wprowadz 0: ")))
list.remove(0)
krotka = tuple(list)
print(krotka)
