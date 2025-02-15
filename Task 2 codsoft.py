print(" Simple Calculator ")

Number1 = float(input("Enter first number here: "))
Number2 = float(input("Enter second number here: "))

print("press 1 for addition \npress 2 for subtraction \npress 3 for multiplication \npress 4 for division")

choice = int(input("enter your choice from 1-4: "))

if choice == 1:
    print("The addition of given two number is",Number1 + Number2)
elif choice == 2:
    print("The subtraction of given two number is",Number1 - Number2)
elif choice == 3:
    print("The multiplication of given two number is",Number1 * Number2)
elif choice == 4:
    print("The division of given two number is",Number1 / Number2)
else:
    print("Invalid Input")                