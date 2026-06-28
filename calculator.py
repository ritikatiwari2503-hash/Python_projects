#             SIMPLE CALCULATOR

n1 = float(input("enter no. 1:")) # number 1

# operator
O = input("enter operator:")
if O not in ["+", "-" , "*", "/"]:
    print("invalid operator")     # operator validation

n2 = float(input("enter no. 2:")) # number 2

if O == "+": # conditions
    print(n1 + n2)
elif O == "-":
    print(n1 - n2)
elif O == "*":
    print(n1 * n2)
elif O == "/":
    if n2 == 0:
        print("error: denominator can't be zero while dividing ")
    else:
        print(n1 / n2)
        
else:
    print("Invalid operator")  # if no operator is chosen out of those 4
