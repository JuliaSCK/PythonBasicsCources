def count_vowels (s):
    vowels = "aeiouyAEIOUY"
    count = 0

    for char in s:
        if char in vowels:
            count += 1

    return count
print(count_vowels("Hey, I am Yuliya"))
