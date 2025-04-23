def count_vowels (text_input):
    vowels = "aeiouyAEIOUY"  # מגדירים את התנועות לבדיקה
    count = 0  # מאתחלים את הספירה

    for char in text_input:    # עוברים על כל תו במחרוזת הקלט
        if char in vowels:  # # בודקים אם התו הוא תנועה
            count += 1  # # אם כן, מגדילים את הספירה

    return count  # מחזירים את הספירה הסופית
print(count_vowels("Hey, I am Yuliya"))
