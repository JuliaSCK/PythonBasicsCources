num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if (num1 % 2) and (num2 % 2) == 0:
    print("Both numbers are  even ")
elif (num1 % 2) and (num2 % 2) != 0:
    print("Both nubers are odd")
else:
    print("The numbers are different")
