hex_colors = {"bela", "zelena", "modra", 345, 455.6, True}
print(hex_colors)
print(hex_colors)

b = ["a", "b", "c", "c", "a", "b"]
a = list(set(b))
print(a)

# Set operations - union
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.union(b))
print(a | b)

# Intersection
print(a.intersection(b))
print(a & b)

# Difference
print(a.difference(b))
print(a - b)
