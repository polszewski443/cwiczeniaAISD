def funkcja(x):
    daysofweek = {
        "1": "Poniedzialek",
        "2": "Wtorek",
        "3": "Środa",
        "4": "Czwartek",
        "5": "Piątek",
        "6": "Sobota",
        "7": "Niedziela"
        }

    return daysofweek[x]


a = input("\033[92mPodaj numer dnia tygodnia, a \033[93mprogram zwroci jego nazwe!: ")
print(funkcja(a))
