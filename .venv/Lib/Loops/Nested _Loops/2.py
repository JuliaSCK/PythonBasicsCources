height = int(input("Enter the height of the pyramid: "))  # 1. קולטים מהמשתמש את גובה הפירמידה

for i in range(1 ,height + 1):  # 2. לולאה חיצונית: רצה על כל שורה בפירמידה
    spaces = height - i   # 3. חישוב מספר הרווחים - מחשבת את מספר הרווחים שצריך להדפיס לפני הכוכביות בשורה הנוכחית
    stars = 2 * i - 1   # 4. חישוב מספר הכוכביות - מחשבת את מספר הכוכביות שצריך להדפיס בשורה הנוכחית.

    print(" " * spaces, end = "")  # מדפיסים רווחים, end="" מונע ירידת שורה
    print("*" * stars)  # מדפיסים כוכביות ויורדים שורה


height_2 = int(input("Enter the height of the pyramid: "))

for i in range(1, height_2 + 1):
    print(" " * (height_2 - i) + "*" * (2 * i - 1))


height_3 = int(input("Enter the height of the pyramid: "))

for i in range(1, height_3 + 1):
    for j in range(height_3 - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

