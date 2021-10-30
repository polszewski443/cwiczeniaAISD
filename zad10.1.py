def czypalindrom(napis):
    return napis == napis[::-1]


napis1 = input("Podaj napis: ")
print(f"\033[93mCzy napis ten jest palindromem: {czypalindrom(napis1)}")
