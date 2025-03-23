num = [i for i in range(1, 11)]
even_num = [n ** 2 for n in num if n % 2 == 0]

print(f"list of the numbers:  {num}")
print(even_num)