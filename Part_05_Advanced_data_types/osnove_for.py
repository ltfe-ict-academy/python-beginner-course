colors = ["rumena", "zelena", "bela", "črna"]

for color in colors:
    print(color.upper())
    print("    --------------      ")

print("Konec programa.")


###################
vrednosti = [34, 556, 77, 44, 34, 67, 3]
vrednosti_pow_2 = []
for vrednost in vrednosti:
    vrednosti_pow_2.append(vrednost**2)

print(vrednosti_pow_2)
###################

beseda = "adecedaabrkadabratralala"
nova_beseda = ""
for crka in beseda:
    if crka not in "aeiou":
        nova_beseda = nova_beseda + crka

print(nova_beseda)
###################

stevike = (56, 77, 88, 6, 443, 21, 56, 788, 768, 88, 65, 45)
sode_stevilke = []

for stevilka in stevike:
    if stevilka % 2 == 0:
        sode_stevilke.append(stevilka)

print(sode_stevilke)

###################
expense1 = {"name": "kava", "category": "hrana", "price": 2.5}
for kljuc, vrednost in expense1.items():
    print(f"KLJUC={kljuc}, VREDNSOT={vrednost}")

###################
for _ in range(4, 20, 2):
    print("hello")

###################
data = [
    {"izdelek": "avto", "cena": 23455},
    {"izdelek": "copate", "cena": 45},
    {"izdelek": "tv", "cena": 545},
    {"izdelek": "računalnik", "cena": 3232},
]
cene_sum = 0
for podatek in data:
    cene_sum += podatek["cena"]

print(f"Vsota je {cene_sum}")

###################
vrednosti = [34, 556, 77, 44, 34, 67, 3]
vrednosti_pow_2 = [vrednost**2 for vrednost in vrednosti]
print(vrednosti_pow_2)
###################
stevike = (56, 77, 88, 6, 443, 21, 56, 788, 768, 88, 65, 45)
sode_stevilke = [stevilka for stevilka in stevike if stevilka % 2 == 0]
print(sode_stevilke)
###################
stevike_vse = (56, -77, 88, 6, 443, 21, -56, -788, 768, -88, 65, 45)
negativne_stevilke = [stevilka for stevilka in stevike_vse if stevilka < 0]
print(negativne_stevilke)
