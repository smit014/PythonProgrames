def CeltoFah(CelTemp):
    return CelTemp * (9 / 5) + 32


def FahtoCel(FahTemp):
    result = 5 / 9 * (FahTemp - 32)
    return result


print("\t*** Temperature Converter ***")
print("================================")
print(" 1. Celsius to Fahrenheit")
print(" 2. Fahrenheit to Celsius")
print(" 3. Exit")

while True:
    TempType = int(input("Enter the type you want to convert (1/2/3): "))

    if TempType == 1:
        CelTemp = float(input("Enter the temperature in Celsius: "))
        print(f"{CelTemp} Celsius = {CeltoFah(CelTemp)} Fahrenheit")
    elif TempType == 2:
        FahTemp = float(input("Enter the temperature in Fahrenheit: "))
        print(f"{FahTemp} Fahrenheit = {FahtoCel(FahTemp)} Celsius")
    elif TempType == 3:
        break
    else:
        print("Invalid option. Please choose 1, 2, or 3.")
