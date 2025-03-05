n = int(input("Enter the number of terms: "))
fib1 = 0
fib2 = 1
i = 1

print(fib1)
print(fib2)

while i <= n-2:
    fib3 = fib1 + fib2
    print(fib3)
    fib1 = fib2
    fib2 = fib3
    #  fib1, fib2 = fib2, fib3
    i += 1

