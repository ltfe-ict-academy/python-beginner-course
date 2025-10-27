import time

print("Start")

number = int(input("Vnesi stevilo večje od 0: "))

while number > 0:
    number -= 1
    if number % 2 == 1:
        continue

    print(number)
    time.sleep(0.2)
    if number == 10:
        print("Prekinemo zanko pri 10")
        break

print("End")
