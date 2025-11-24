class InternalEmployee:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    def increment_age(self, add_age):
        self.age = self.age + add_age


james = InternalEmployee("James", 34, "programmer")
john = InternalEmployee("John", 22, "ceo")
anna = InternalEmployee("Anna", 34, "cto")


print(james.name)
print(f"ana age {anna.age}")
anna.increment_age(5)
print(f"ana age {anna.age}")


seznam = [1, 2, 3]
seznam.append(4)
print(seznam)
