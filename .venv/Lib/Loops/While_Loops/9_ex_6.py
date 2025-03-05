number = int(input("Enter the number: "))

print("The prime numbers up to", number, "are: ")

i = 2

while i <= number:
    is_prime = True
    j = 2
    while j < i and is_prime:
        if i % j == 0:
            is_prime = False
        j += 1
    if is_prime:
        print(i)
    i += 1





