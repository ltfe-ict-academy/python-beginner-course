red = (255, 0, 0)
print(red[0])

# red[0] = 0 # error

simple = (4,)

# Tuple packing and unpacking
point = (45, 67, 90)
x = point[0]
y = point[1]
z = point[2]

x, y, z = point
print(x, y, z)

a = [200, 100, 500]
b = [56, 78, 99]

# zamenjava vrednsoti
a, b = b, a
print(a, b)

vresdnosti = ("rdece", "belo", "modro")
print("belo" in vresdnosti)
print("zeleno" in vresdnosti)
