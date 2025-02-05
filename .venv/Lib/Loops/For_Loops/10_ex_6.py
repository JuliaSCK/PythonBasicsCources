word  = "Hello"
reversed_word = ""  # Start with an empty string to build the reversed version

for i in range(len(word) -1, -1, -1):
    # range(start, stop, step) - This creates a sequence of numbers.
    #   start:  We start from the last index (length - 1)
    #   stop:  We go until the index -1 (before the first index)
    #   step:  We decrease by 1 each time (-1)
    reversed_word += word[i]  # Add the current character at index 'i' to reversed_string

print(reversed_word)

# Output: olleH

print("-*-*-*-*-*-*-*-*-*-")

input_string = "Hello"
string_length = len(input_string)

for i in range(string_length - 1, -1, -1):
    print(input_string[i], end="")  # Print each character without a newline
print() # Add a newline at the end

# Output: olleH

