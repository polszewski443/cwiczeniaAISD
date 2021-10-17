'''Przygotować skrypt, w którym użytkownik będzie podawał kolejne liczby w pętli,
dopóki suma wszystkich podanych do tej pory liczb nie osiągnie wartości 100.
'''
arrValue = 0
arrOne = []
while arrValue < 100:
    arrOne.append(int(input("Dodaj wartosc: ")))
    arrValue = sum(arrOne)
print("Koniec! Dodano wystarczajaca ilosc liczb!")
