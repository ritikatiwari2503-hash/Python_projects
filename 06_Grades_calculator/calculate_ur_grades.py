marks = int(input("Enter your marks: "))

if marks>=90:
    print("wowww! Your grade is A+")
elif 80 <= marks < 90:
    print("great! Your grade is A")
elif 70 <= marks < 80:
    print("good! Your grade is B")
elif 60 <= marks < 70:
    print("Your grade is C","you need to work hard")
elif 50 <= marks < 60:
    print("Your grade is D","you really need to work hard")
else:
    print("Your grade is F","You are failed","Try better next time")
