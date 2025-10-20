"""Pretvornik temperatur med °C in °F."""

print("Pretvornik temperatur med °C in °F")

temperatura_c = float(input("Vpiši temperaturo v °C: "))
temperatura_f = temperatura_c * 9 / 5 + 32

print(f"Temperatura v °F: {temperatura_f}")

temp_vecje_kot_sto = temperatura_f > 100
print(f"Temperatura je večja od 100° F? \n{temp_vecje_kot_sto}")
