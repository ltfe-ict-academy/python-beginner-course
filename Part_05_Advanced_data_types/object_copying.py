from copy import copy, deepcopy

a = 42
b = a
print(f"a is b: {a is b}. a ID = {id(a)}, b ID = {id(b)}")

# Int, float, bool (immutable type)
vrednost = 4
nova_vrednost = vrednost
nova_vrednost = 5
print(f"VREDNOST: {vrednost}, NOVA_VREDNOST: {nova_vrednost}")

# Understanding Shallow and Deep Copying
zbrika = {"predmeti": [12, 35, 67, 8], "stevilo": 4}
nova_zbirka = zbrika
nova_zbirka["test"] = 23
print(f"NOVA ZBIRKA=> {nova_zbirka}, ID: {id(nova_zbirka)}")
print(f"ZBIRKA=> {zbrika}, ID: {id(zbrika)}")

# Shallow copy - COPY
zbrika = {"predmeti": [12, 35, 67, 8], "stevilo": 4}
nova_zbirka = copy(zbrika)
nova_zbirka["test"] = 23
print(f"NOVA ZBIRKA=> {nova_zbirka}, ID: {id(nova_zbirka)}")
print(f"ZBIRKA=> {zbrika}, ID: {id(zbrika)}")


zbrika = {"predmeti": [12, 35, 67, 8], "stevilo": 4}
nova_zbirka = copy(zbrika)
nova_zbirka["test"] = 23
predmeti = nova_zbirka["predmeti"]
predmeti.append(56)
print(f"NOVA ZBIRKA=> {nova_zbirka}, ID: {id(nova_zbirka)}")
print(f"ZBIRKA=> {zbrika}, ID: {id(zbrika)}")


zbrika = {"predmeti": [12, 35, 67, 8], "stevilo": 4}
nova_zbirka = deepcopy(zbrika)
nova_zbirka["test"] = 23
predmeti = nova_zbirka["predmeti"]
predmeti.append(56)
print(f"NOVA ZBIRKA=> {nova_zbirka}, ID: {id(nova_zbirka)}")
print(f"ZBIRKA=> {zbrika}, ID: {id(zbrika)}")

print("--------------------------------------")
# Slicing
podatki = [1, 2, [44, 55, 66], 4, 5, 6, 77, 85, 3, 5]
uporabne_vrednsoti = podatki[:5]
uporabne_vrednsoti.append(66)
uporabne_vrednsoti[2].append(32)
print(f"PODATKI: {podatki}, UPORABNE VREDNSOTI: {uporabne_vrednsoti}")
