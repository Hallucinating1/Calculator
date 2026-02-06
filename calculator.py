try: # taking the input
    a = float(input("Enter the first number")) # num1
    b = float(input("Enter the second number")) # num2
except: # if the input is non-numerical
    print("Invalid input! Please enter a number.")
    exit();
action = input("Enter the action (eg. +,-,*,/)") # the operator
if action in "+"  : # addition
    c = a + b
    print (c);
elif action in "-"  : # subtraction
    c = a - b
    print (c);
elif action in ["×", "*"]  : # multiplication
    c = a * b
    print (c);
elif action in ["÷", "/"] : # division
    if a == 0 or b == 0: # --divisibility by 0
        print("divisibility is not possible with 0");
    elif a % b == 0: # --when there is no remainder
        c = a / b
        print(c)
    else: # --when there is a remainder
        c = a / b
        print(c)
        remainder = a % b
        print('Remainder', remainder);
elif action in ["^", "**"]  : # power
    c = a ** b
    print (c);
else :
    print("You haven't entered a supported action");