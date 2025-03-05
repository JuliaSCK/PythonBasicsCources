x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

gcd = 1
i = 1

while i <= x and i <= y:
    if x % i == 0 and y % i == 0:
        gcd = i
    i += 1
print("The GCD of ", x, "and ", y, "is ", gcd)