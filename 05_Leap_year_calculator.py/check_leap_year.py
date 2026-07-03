y = int(input("Enter a year: "))

if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):    #divides 4 and 400 but not 100 ->then leap year
    print(f"{y} is a leap year.")
else:
    print(f"{y} is not a leap year.")
