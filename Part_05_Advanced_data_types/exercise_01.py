all_values = []

while True:
    value = input("Enter value: ")
    if not value:
        break
    all_values.append(int(value))


print(f"Values sum is: {sum(all_values)}")
print(f"Sorted values: {sorted(all_values)}")
print(f"Original values: {all_values}")
