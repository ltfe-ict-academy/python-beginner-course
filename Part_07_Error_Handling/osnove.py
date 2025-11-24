# print("Hello")
# print("World")
# value = False
# if value:
#     print(f"Value: {value}")
#     print(4 / 0)

# print("END")
# https://docs.python.org/3/library/exceptions.html#exception-hierarchy

try:
    stevilo1 = int(input("Vnsesi stevilo 1: "))
    stevilo2 = int(input("Vnsesi stevilo 2: "))
    rezultat = stevilo1 / stevilo2
except ValueError as err:
    print("Prosim vstavi število! Napaka pri pretvarjanju:", err)
except ZeroDivisionError:
    print("Deljenje z 0 ni dovoljeno!")
except Exception:
    print("Neznana napaka!")
except KeyboardInterrupt:
    print("Izhod.")
else:
    print(f"{stevilo1}/{stevilo2}={rezultat}")
finally:
    print("Konec programa!")
