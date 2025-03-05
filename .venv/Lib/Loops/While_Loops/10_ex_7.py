a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

def multiply (a,b):
    result = 0
    sign = 1
    if (a < 0 and b >= 0) or (b < 0 and a >= 0):
        sign = -1
    for i in range(abs(b)):
        result += abs(a)
    print(sign * result)

#  multiply(-5, 6)