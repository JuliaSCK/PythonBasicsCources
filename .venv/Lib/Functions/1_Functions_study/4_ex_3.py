def find_max(numbers):
    max_num = numbers[0]

    for num in numbers:
        if num > max_num:
            max_num = num

    return  max_num

max_num_example = find_max([10, 3, 1, -5, 8, -20, 5])
print(max_num_example)



