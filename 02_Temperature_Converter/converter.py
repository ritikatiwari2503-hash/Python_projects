#                      TEMPERATURE CONVERTER 


Temp = float(input("Enter the Temperature: "))                                     # number or float form
choice = input("Enter the conversion type (c to f or f to c): ").lower()           # choice of conversion



if choice == "c to f":                                                             # "°C to °F"
    formula = (Temp*9/5)+32                                                        # Converted into Fahrenheit
    print("Temperature in Fahrenheit is ",formula)   
elif choice == "f to c":                                                           # "°F to °C"
    formula = (Temp-32)*5/9
    print("Temperature in Celsius is ",formula)                                    #converted into Celsius
else:
    print("Invalid choice! Please enter a valid conversion type!!!")               # Invalid choice
