def find_common_elements (list_1, list_2):
    common_elements = []

    for num1 in list_1:  # לולאה חיצונית על הרשימה הראשונה
        for num2 in list_2:  # לולאה פנימית על הרשימה השנייה
            if num1 == num2:  # בדיקת שוויון
                if num1 not in common_elements:  # אם נמצא אלמנט משותף - הוספה לרשימת התוצאות ונבדוק קודם אם הוא כבר שם, כדי למנוע כפילויות
                    common_elements.append(num1)
    return common_elements  # החזרת הרשימה החדשה עם האלמנטים המשותפים

l2 = [4, 5, 9, 20, 8]
l2 = [3, 6, 8, 20, 10]
print(find_common_elements(l1, l2))
