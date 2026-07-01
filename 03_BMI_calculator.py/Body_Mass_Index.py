#                  BMI {body mass index} Calculator

height = float(input("Enter your height (in meters): "))
weight = float(input("Enter your weight (in kilograms): "))

BMI  = weight / (height ** 2)             # BMI formula

if BMI < 18.5:
    print("you are underweight.")
elif 18.5<= BMI < 25:
    print("You have a normal weight.")
elif 25 <= BMI < 30:
    print("You are overweight.")
else:
    print("You are a bit obese buddy!")
