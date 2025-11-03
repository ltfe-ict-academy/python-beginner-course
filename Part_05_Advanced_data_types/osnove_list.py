# Ordered
vrednosti = [13, 1, 8, 5, 7, 10]
print(vrednosti)
# Zero-based
print(vrednosti[2])
# Mutable
vrednosti[0] = 17
print(vrednosti)
# Heterogeneous
vrednosti = [True, 34, 54.6, "haha"]
print(vrednosti)
# Growable and dynamic
del vrednosti[2]
print(vrednosti)
# Nestable
vrednosti = [45, [2, 3, 4], 56]
print(vrednosti)
vrednosti = [56, 7, 8, 9, 34, 5, 1]
print(vrednosti[:3])


barve = ["rdeča", "rumena", "bela", "zelena", "črna"]
print(barve[3])
print(len(barve))
# print(barve[7])
print(barve[-2])

print(barve[0:3])
print(barve[:3])
print(barve[2:4])
print(barve[0:5:2])
print([barve[1]] + barve[3:5])
print(barve[3:5])
print(barve[3:])
print(barve[-3:])
print(barve[::-1])  # obrnemo vrednosti v list-u

barve = ["rdeča", "rumena", [2, 3, 4], "zelena", "črna"]
print(barve[2][1])
print(barve)
barve[2] = "roza"
print(barve)

barve.append("bela")
print(barve)

# Method extend
barve_a = ["modra", "črna"]
barve_b = ["bela", "zelena", "modra"]
barve_a.extend(barve_b)
print(barve_a)

# Reverse a list
barve_r = barve_a[::-1]  # opcija 1
barve_r = list(reversed(barve_a))  # opcija 2
print(barve_r)
barve_a.reverse()
print(barve_a)

# Sorting a list
vrednosti = [56, 7, 8, 9, 34, 5, 1]
print(sorted(vrednosti))
vrednosti.sort(reverse=True)
print(vrednosti)
