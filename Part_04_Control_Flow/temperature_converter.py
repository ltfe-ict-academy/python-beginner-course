"""Convert temperature between °C and °F."""

print("Welcome to temperature converter!")

is_failure = True

while is_failure:
    temperature_input = float(input("Enter the temperature value: "))
    temperature_unit = input("Enter temperature unit [C/F]: ")
    temperature_converted = None
    temperature_unit = temperature_unit.upper()

    if temperature_unit == "C":
        temperature_converted = temperature_input * 9 / 5 + 32
        is_failure = False
    elif temperature_unit == "F":
        temperature_converted = (temperature_input - 32) * 9 / 5
        is_failure = False
    else:
        print(f"Temperature unit should be F or C. Input is: {temperature_unit}")

if temperature_converted is not None:
    print(f"Converted temperature is {temperature_converted}")
