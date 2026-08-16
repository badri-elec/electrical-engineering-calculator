def calculate_power(voltage, current):
    return voltage * current


def calculate_voltage(resistance, current):
    return resistance * current


def calculate_current(voltage, resistance):
    return voltage / resistance


def calculate_resistance(voltage, current):
    return voltage / current


while True:
    print("\n((((((((((((((((((((()))))))))))))))))))))")
    print("|Electrical Engineering Calculator|")
    print("((((((((((((((((((((()))))))))))))))))))))")
    print("1. Power")
    print("2. Voltage")
    print("3. Current")
    print("4. Resistance")
    print("5. Exit")

    try:
        choice = int(input("Choice: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if choice == 1:
        try:
            voltage = float(input("V = "))
            current = float(input("I = "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        result = calculate_power(voltage, current)
        print(f"Power = {result:.2f} W")

    elif choice == 2:
        try:
            resistance = float(input("R = "))
            current = float(input("I = "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        result = calculate_voltage(resistance, current)
        print(f"Voltage = {result:.2f} V")

    elif choice == 3:
        try:
            voltage = float(input("V = "))
            resistance = float(input("R = "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if resistance == 0:
            print("Resistance cannot be zero.")
            continue

        result = calculate_current(voltage, resistance)
        print(f"Current = {result:.2f} A")

    elif choice == 4:
        try:
            voltage = float(input("V = "))
            current = float(input("I = "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if current == 0:
            print("Current cannot be zero.")
            continue

        result = calculate_resistance(voltage, current)
        print(f"Resistance = {result:.2f} Ohm")

    elif choice == 5:
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
        