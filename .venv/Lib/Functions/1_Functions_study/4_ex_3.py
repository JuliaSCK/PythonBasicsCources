def find_max(numbers):

    if not numbers:   # שיפור: בדיקה אם הרשימה ריקה
        print("Error!!! Your list doesn't have date!!!")
        return

    max_num = numbers[0]

    for num in numbers:  # לולאה שעוברת על כל המספרים ברשימה
        if num > max_num:
            max_num = num  # עדכון המספר המקסימלי אם נמצא מספר גדול יותר


    return  max_num  # החזרת המספר המקסימלי שנמצא

max_num_example = find_max([10, 3, 20, -5, 8, -20, 5])
print(max_num_example)



