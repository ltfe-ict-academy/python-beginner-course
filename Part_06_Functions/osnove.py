# Defining Functions in Python
# len(), sum(), print(), type(), id()

print(dir())


def vsota(stevilo_1, stevilo_2, stevilo_3):
    print("Ta funkcija je vsota.")
    print("To je konec funkcije")
    print(stevilo_1 + stevilo_2 + stevilo_3)


print("Začetek našega programa")
vsota(4, 6, 45)
vsota(29, 45, 76)


def izracun_cene(izdelek, kolicina, cena_izdelka):
    cena = kolicina * cena_izdelka
    print(f"Izračunavam ceno za vse {izdelek}. Cena za vse izdelke je: {cena}€")
    return cena


izracun_cene("banane", 34, 0.45)
# izracun_cene(0.45, "banane", 30)

izracun_cene(izdelek="banane", kolicina=34, cena_izdelka=0.45)
izracun_cene(kolicina=34, izdelek="banane", cena_izdelka=0.45)
cena = izracun_cene("banane", kolicina=34, cena_izdelka=0.45)
print(cena)


def izracunaj_koordinate(x_start, y_start, premik_x, premik_y):
    x_kon = x_start + premik_x
    y_kon = y_start + premik_y
    return x_kon, y_kon


koncna_x, koncna_y = izracunaj_koordinate(3, 4, 6, 7)
print(koncna_x, koncna_y)


def izracun_cene_2(
    izdelek: str,
    kolicina: int,
    cena_izdelka: float,
    *,
    davek: float = 0.22,
) -> float:
    cena = (kolicina * cena_izdelka) * (1 + davek)
    print(
        f"Izračunavam ceno za vse {izdelek}. Cena za vse izdelke je: {cena}€ z DDV: {davek * 100}%",
    )
    return cena


izracun_cene_2("banane", 22, 0.54)
izracun_cene_2("banane", 22, 0.54, davek=0.55)


print("-------------------------------------------")

krog = True


def square(value: int) -> None:
    """Funkcija za izracun kvadrata stevila."""
    result = value**2
    # global krog
    krog = result**2
    print(f"The square of {value} is {result}. Krog: {krog}")
    print(f"INNER DIR: {dir()}")
    print(krog)


square(435)
print(f"OUTER krog: {krog}")
print(dir())
