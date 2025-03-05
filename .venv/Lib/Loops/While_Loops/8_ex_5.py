number = int(input("Enter the number: "))
is_prime = True
i = 2
while i < number:
    if number % i == 0:
        is_prime = False
    i += 1

if is_prime:
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")