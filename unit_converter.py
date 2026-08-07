# FUNCTIONS
def km_to_miles(n):
    return n * 0.621371

def miles_to_km(n):
    return n * 1.60934

def cm_to_inches(n):
    return n * 0.393701

def inches_to_cm(n):
    return n * 2.54

def kg_to_lbs(n):
    return n * 2.20462

def lbs_to_kg(n):
    return n * 0.453592

def celsius_to_fahrenheit(n):
    return (n * 9/5) + 32

def fahrenheit_to_celsius(n):
    return (n - 32) * 5/9

# MENU
while True:
    print("\n__________________________________ UNIT CONVERTER____________________________________")
    print("1. km to miles")
    print("2. miles to km")
    print("3. cm to inches")
    print("4. inches to cm")
    print("5. kg to lbs")
    print("6. lbs to kg")
    print("7. celsius to fahrenheit")
    print("8. fahrenheit to celsius")
    print("9. Quit")

    c = input("Enter your choice: ")

    if c == "1":
        n = float(input("Enter km: "))
        print(f"Result: {km_to_miles(n)} miles")
    elif c == "2":
        n = float(input("Enter miles: "))
        print(f"Result: {miles_to_km(n)} km")
    elif c == "3":
        n = float(input("Enter cm: "))
        print(f"Result: {cm_to_inches(n)} inches")
    elif c == "4":
        n = float(input("Enter inches: "))
        print(f"Result: {inches_to_cm(n)} cm")
    elif c == "5":
        n = float(input("Enter kg: "))
        print(f"Result: {kg_to_lbs(n)} lbs")
    elif c == "6":
        n = float(input("Enter lbs: "))
        print(f"Result: {lbs_to_kg(n)} kg")
    elif c == "7":
        n = float(input("Enter celsius: "))
        print(f"Result: {celsius_to_fahrenheit(n)} F")
    elif c == "8":
        n = float(input("Enter fahrenheit: "))
        print(f"Result: {fahrenheit_to_celsius(n)} C")
    elif c == "9":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")