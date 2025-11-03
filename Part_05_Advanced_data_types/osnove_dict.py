barve = {"bela": (0, 0, 255), "črna": (0, 0, 0), "zelena": (255, 0, 0)}

print(barve)
print(barve["zelena"])

expense1 = ["kava", "hrana", 2.5]
expense2 = ["avto", "gorivo", 25.0]
expense3 = ["stanovanje", "najem", 550.0]
all_expenses = [expense1, expense2, expense3]
print(all_expenses)

expense1 = {"name": "kava", "category": "hrana", "price": 2.5}
print(f"Cena za {expense1['name']} je {expense1['price']}€")
expense1["price"] = 3.0
print(f"Cena za {expense1['name']} je {expense1['price']}€")

expense1["vat"] = 0.2
print(expense1)

expense1 = {"name": "kava", "category": "hrana", "price": 2.5}
expense2 = {"name": "avto", "category": "gorivo", "price": 25}
expense3 = {"name": "stanovanje", "category": "najem", "price": 550}
all_expenses = {
    "kava": expense1,
    "avto": expense2,
    "stanovanje": expense3,
}
print(all_expenses["stanovanje"]["price"])
